from abc import ABC, abstractmethod
class Stats(ABC):
    
    @abstractmethod
    def __init__(self, hp, cp, defense, special_skill, 
        special_skill_count) -> None:
        super().__init__()
        self.hp = hp
        self.cp = cp

class BaseStats(Stats):
    def __init__(self) -> None:
        super().__init__()

class DynamicStats(Stats):

    def __init__(self) -> None:
        super().__init__()