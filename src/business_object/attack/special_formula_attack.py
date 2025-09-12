from busniess_object.attack.abstract_formula_attack import AbstractFormulaAttack

from business_object.pokemon.abstract_pokemon import AbstractPokemon


class SpecialFormulaAttack(AbstractFormulaAttack):
    def __init__(self, power=0, name=None, description=None):
        super().__init__(power=power, name=name, description=description)

    def compute_damage(pk1: AbstractPokemon, pk2: AbstractPokemon) -> int:
        pass

    def get_attack_stat(pk1: AbstractPokemon) -> float:
        pass

    def get_defense_stat(pk1: AbstractPokemon) -> float:
        pass
