import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from abc import ABC, abstractmethod
from Hero import Hero
from Effects import *

class Trait(ABC):

    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
        self.name = None
    
    @abstractmethod
    def apply_trait(self, target_hero: Hero):
        pass


class Duelist(Trait):
    
    def __init__(self) -> None:
        super().__init__()
        

class Motorist(Trait):

    def __init__(self) -> None:
        super().__init__()