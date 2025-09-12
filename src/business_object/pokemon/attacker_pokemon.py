from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AttackerPokemon(AbstractPokemon):
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None, type_pk="Attacker"):
        super().__init__(
            stat_max=stat_max, stat_current=stat_current, level=level, name=name, type_pk=type_pk
        )

    def get_pokemon_attack_coef(self) -> float:
        multiplier = 1 + (self.speed_current + self.attack_current) / 200
        return multiplier
