import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from abc import ABC, abstractmethod
from Hero import Hero
from heros_list import Juno
from Effects import *

class Trait(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.name = None
    
    @abstractmethod
    def apply_trait(self, target_hero: Hero):
        
        pass

    def print_name(self):
        print('in ' + self.__class__.__name__)


class Duelist(Trait):
    
    def __init__(self) -> None:
        super().__init__()
        self.effects = []
        self.effects.append(None)
    
    def apply_trait(self, target_hero: Hero):
        self.print_name()
        pass


class Motorist(Trait):

    def __init__(self) -> None:
        super().__init__()
    
    def apply_trait(self, target_hero: Hero):
        self.print_name()
        pass

class Venomist(Trait):

    def __init__(self) -> None:
        super().__init__()
    
    def apply_trait(self, target_hero: Hero):
        self.print_name()
        pass

if __name__ == '__main__':
    import importlib, inspect, os

    # get the file name
    file_extenstion_name = os.path.basename(os.path.abspath(__file__))
    file_name = file_extenstion_name.split('.')[0]
    print(file_name)
    base_name = Trait.__name__
    
    for name, obj in inspect.getmembers(importlib.import_module(file_name)):
        if inspect.isclass(obj):
            #print(obj)
            if obj.__bases__[0].__name__ == base_name:
                print(obj)
                new_trait = obj()
                new_hero = Juno()
                new_trait.apply_trait(new_hero)