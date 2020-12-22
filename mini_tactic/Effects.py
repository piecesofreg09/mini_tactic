import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from abc import ABC, abstractmethod
from Hero import Hero

class Effect(ABC):
    '''
    base class for effect
    class variable:
        countdown: the duration of countdown, default to be last forever
    '''

    test_str = 'new'
    

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.countdown = None
    
    @abstractmethod
    def apply_effect(self, target_hero: Hero):
        pass
    
    def __change_speed(self, target_hero: Hero):
        pass

    def __change_defense(self, target_hero: Hero):
        pass
    
    def __change_HP(self, target_hero: Hero):
        pass
    
    def __change_CP(self, target_hero: Hero):
        pass

class SlowDown(Effect):
    
    def __init__(self, countdown=30) -> None:
        super().__init__()
        self.countdown = countdown
    
    def apply_effect(self, target_hero: Hero):
        self.__change_speed(target_hero)

    def __change_speed(self, target_hero: Hero):
        print('Change speed in slow down')
        pass

class IncreaseDefense(Effect):
    
    def __init__(self, countdown=40) -> None:
        super().__init__()
        self.countdown = countdown
    
    def apply_effect(self, target_hero: Hero):
        self.__change_defense(target_hero)

    def __change_defense(self, target_hero: Hero):
        print('Change defense in increase defense')
        pass

class IncreaseAttack(Effect):
    
    def __init__(self, countdown=21) -> None:
        super().__init__()
        self.countdown = countdown
    
    def apply_effect(self, target_hero: Hero):
        self.__change_CP(target_hero)

    def __change_CP(self, target_hero: Hero):
        print('Change attack in increase attack')
        pass

class RegenerateHP(Effect):
    
    def __init__(self, countdown = 15) -> None:
        super().__init__()
        self.countdown = countdown
    
    def apply_effect(self, target_hero: Hero):
        self.__change_HP(target_hero)

    def __change_HP(self, target_hero: Hero):
        print('Change HP in Regenerate HP')
        pass