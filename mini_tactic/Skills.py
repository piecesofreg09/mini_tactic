import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from abc import ABC, abstractmethod
from Hero import Hero
from heros_list import Juno
from Effects import *


class Skill(ABC):

    @abstractmethod
    def __init__(self, cooldown=None):
        self.cooldown = cooldown
        self.count = self.cooldown
        pass
    
    @abstractmethod
    def apply_skill(self):
        pass

class Berserker(Skill):
    '''
    Increae on attack to other hero, for only one round
    '''
    def __init__(self, cooldown=4):
        super().__init__(cooldown)
    
    def apply_skill(self):
        pass

class Vanisher(Skill):
    '''
    Immune to attack from this round
    '''
    def __init__(self, cooldown=5):
        super().__init__(cooldown)
    
    def apply_skill(self):
        pass
        

class Elephant(Skill):
    '''
    Regenerate hp by 200 points
    '''
    def __init__(self, cooldown=3):
        super().__init__(cooldown)
    
    def apply_skill(self):
        pass
        

class Duplicate(Skill):
    '''
    Attack twice in this round
    '''
    def __init__(self, cooldown=4):
        super().__init__(cooldown)
        