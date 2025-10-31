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


class Warrior(Character):
    def __init__(self):
        super().__init__("Warrior", "sword", 100)

    def attack(self) -> str:
        return f"{self.name} attacks with {self.weapon}!"

class Mage(Character):
    def __init__(self):
        super().__init__("Mage", "staff", 60)

    def attack(self) -> str:
        return f"{self.name} casts spell with {self.weapon}!"

class Archer(Character):
    def __init__(self):
        super().__init__("Archer", "bow", 80)

    def attack(self) -> str:
        return f"{self.name} shoots with {self.weapon}!"

def create_hero(hero_type: str) -> Character:
    hero_type = hero_type.lower()
    if hero_type == "warrior":
        return Warrior()
    elif hero_type == "mage":
        return Mage()
    elif hero_type == "archer":
        return Archer()
    else:
        raise ValueError(f"Unknown hero type: {hero_type}")

# Przykład użycia (odkomentuj gdy zaimplementujesz)
# if __name__ == "__main__":
#     warrior = create_hero("warrior")
#     print(f"{warrior.name}: {warrior.attack()}")
