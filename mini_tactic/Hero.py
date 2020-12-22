from __future__ import annotations
from abc import ABC, abstractmethod


class Hero(ABC):
    '''
    Base hero class
    '''
    base_health = 1000
    base_damage = 100

    @abstractmethod
    def __init__(self, current_health=None, current_damage=None):
        self.current_health = current_health if current_health else self.base_health
        self.current_damage = current_damage if current_damage else self.base_damage
        self.target_hero = None
        
        pass
    

    @abstractmethod
    def process_trait(self):
        pass

    @abstractmethod
    def process_skill(self):
        pass

    
    def set_target(self, target_hero: Hero):
        self.target_hero = target_hero
        pass
    def deal_damage_to(self, ):
        self.target_hero.current_health -= self.current_damage
        pass