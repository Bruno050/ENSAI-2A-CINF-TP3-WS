from abc import ABC, abstractmethod

from business_object.pokemon.abstract_pokemon import AbstractPokemon

# from business_object.statistic import Statistic


class AbstractAttack(ABC):
    def __init__(self, power=0, name=None, description=None):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(pk1: AbstractPokemon, pk2: AbstractPokemon) -> int:
        pass
