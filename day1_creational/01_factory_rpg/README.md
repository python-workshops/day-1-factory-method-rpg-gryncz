# 🏭 Factory Method - System Bohaterów RPG

## 🎯 Zadanie
Implementuj wzorzec Factory Method do tworzenia różnych klas bohaterów w grze RPG.

## 📋 Wymagania
- [ ] `create_hero("warrior")` zwraca obiekt Warrior z mieczem i 100 HP
- [ ] `create_hero("mage")` zwraca obiekt Mage z różdżką i 60 HP
- [ ] `create_hero("archer")` zwraca obiekt Archer z łukiem i 80 HP
- [ ] Każdy bohater ma metody `attack()` i `get_stats()`

## 🚀 Jak zacząć
1. Otwórz `starter.py`
2. Zaimplementuj wzorzec Factory Method
3. Uruchom testy: `python -m pytest test_factory.py -v`
4. Commit gdy wszystkie testy przechodzą ✅

## ⏰ Czas: 20 minut

## 💡 Podpowiedź
```python
# Przykład wzorca Factory Method
def create_hero(hero_type: str) -> Character:
   # Twoja implementacja tutaj
   pass
