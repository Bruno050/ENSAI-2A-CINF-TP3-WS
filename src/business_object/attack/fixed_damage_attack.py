from busniess_object.attack.abstract_attack import AbstractAttack

from business_object.pokemon.abstract_pokemon import AbstractPokemon


class FixedDamageAttack(AbstractAttack):
    def __init__(self, power=0, name=None, description=None):
        super().__init__(power=power, name=name, description=description)

    def compute_damage(pk1: AbstractPokemon, pk2: AbstractPokemon) -> int:
        pass
