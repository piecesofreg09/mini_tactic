from abc import ABC, abstractmethod
class Stats(ABC):
    
    @abstractmethod
    def __init__(self, hp, cp, defense=None, special_skill_damage=None, 
        special_skill_count=None) -> None:
        super().__init__()
        self.hp = hp
        self.cp = cp
        self.defense = defense
        self.special_skill_damage = special_skill_damage if special_skill_damage else 400
        self.special_skill_count = special_skill_count if special_skill_count else 4

class BaseStats(Stats):
    def __init__(self, hp, cp, defense=None, special_skill_damage=None, 
        special_skill_count=None) -> None:
        super().__init__(hp, cp, defense=None, special_skill_damage=None, 
        special_skill_count=None)

class DynamicStats(Stats):

    def __init__(self, hp, cp, defense=None, special_skill_damage=None, 
        special_skill_count=None) -> None:
        super().__init__(hp, cp, defense=None, special_skill_damage=None, 
        special_skill_count=None)