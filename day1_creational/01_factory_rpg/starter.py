"""
Factory Method Pattern - RPG Heroes
Zaimplementuj wzorzec Factory Method do tworzenia bohaterów.
"""

import abc


class Character(abc.ABC):
    """Bazowa klasa dla wszystkich bohaterów"""

    def __init__(self, name: str, weapon: str, hp: int):
        self.name = name
        self.weapon = weapon
        self.hp = hp

    @abc.abstractmethod
    def attack(self) -> str:
        """Zwraca opis ataku bohatera"""
        pass

    def get_stats(self) -> dict:
        """Zwraca statystyki bohatera"""
        return {
            "name": self.name,
            "weapon": self.weapon,
            "hp": self.hp
        }


# TODO: Zaimplementuj klasy Warrior, Mage, Archer
class Warrior:
    pass


class Mage:
    pass


class Archer:
    pass


# TODO: Zaimplementuj funkcję factory
def create_hero(hero_type: str) -> Character:
    """
    Factory Method do tworzenia bohaterów

    Args:
        hero_type: Typ bohatera ("warrior", "mage", "archer")

    Returns:
        Obiekt odpowiedniej klasy bohatera

    Raises:
        ValueError: Gdy hero_type jest nieznany
    """
    pass

# Przykład użycia (odkomentuj gdy zaimplementujesz)
# if __name__ == "__main__":
#     warrior = create_hero("warrior")
#     print(f"{warrior.name}: {warrior.attack()}")
