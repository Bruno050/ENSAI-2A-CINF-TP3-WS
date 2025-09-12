from busniess_object.attack.abstract_attack import AbstractAttack

from business_object.pokemon.abstract_pokemon import AbstractPokemon
from abc import ABC, abstractmethod


class AbstractFormulaAttack(AbstractAttack, ABC):
    def __init__(self, power=0, name=None, description=None):
        super().__init__(power=power, name=name, description=description)

    @abstractmethod
    def compute_damage(pk1: AbstractPokemon, pk2: AbstractPokemon) -> int:
        pass

    @abstractmethod
    def get_attack_stat(pk1: AbstractPokemon) -> float:
        pass

    @abstractmethod
    def get_defense_stat(pk1: AbstractPokemon) -> float:
        pass
