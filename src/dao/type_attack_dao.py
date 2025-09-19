from typing import List, Optional
from dao.db_connection import DBConnection
from utils.singleton import Singleton
from business_object.attack.abstract_attack import AbstractAttack, AttackFactory


class TypeAttackDAO(metaclass=Singleton):
    """
    Communicate with the attack_type table
    """

    def find_all_attack_type(self) -> List[str]:
        """
        Get all attack type names and return a list

        :return: A list of all types
        :rtype: List of str
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                  "
                    "  FROM tp.attack_type                     "
                )

                # to store raw results
                res = cursor.fetchall()

        # Create an empty list to store formatted results
        type_attack: List[str] = []

        # if the SQL query returned results (ie. res not None)
        if res:
            for row in res:
                type_attack.append(row["attack_type_name"])

                print(row["id_attack_type"])
                print(row["attack_type_name"])
                print(row["attack_type_description"])

        return type_attack

    def find_id_by_label(self, label: str) -> Optional[int]:
        """
        Get the id_attack_type from the label
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_attack_type                     "
                    "  FROM tp.attack_type                     "
                    " WHERE attack_type_name = %(attack_name)s ",
                    {"attack_name": label},
                )
                res = cursor.fetchone()

        if res:
            return res["id_attack_type"]

    def find_attack_by_id(self, id: int) -> str | None:
        """Return the attack name with the given ID or None if not found."""
        
        with DBConnection().connection as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    "SELECT attack_name "
                    "FROM tp.attack "
                    "WHERE id_attack = %(id)s",
                    {"id": id} 
                )
                res = cursor.fetchone()

        if res:
            return res["attack_name"]
        return None



    def find_all_attacks(self, limit: int) -> List[AbstractAttack] | None:
        """Return a list of all attacks, limited by 'limit'."""

        with DBConnection().connection as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(
                    """
                    SELECT a.id_attack, a.power, a.attack_name, a.attack_description, 
                        a.accuracy, a.element, att.attack_type_name
                    FROM tp.attack a
                    JOIN tp.attack_type_name att ON a.id_attack = at.id_attack
                    LIMIT %(limit)s
                    """,
                    {"limit": limit}
                )
                rows = cursor.fetchall()

        if not rows:
            return None

        res = [
            AttackFactory().instantiate_attack(
                a["attack_type_name"],
                a["id_attack"],
                a["power"],
                a["attack_name"],
                a["attack_description"],
                a["accuracy"],
                a["element"],
            )
            for a in rows
        ]

        print(res[0])
        print(type(res[0]))
        return res



if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_types = TypeAttackDAO().find_all_attack_type()
    #print(attack_types)

    print(" --------- ------------- ---------------")
    all_attacks = TypeAttackDAO().find_all_attacks(5)
    #print(all_attacks)
