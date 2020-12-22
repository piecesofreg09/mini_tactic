import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from abc import ABC, abstractmethod
from Hero import Hero

class InstantEffect(ABC):
    '''
    base class for instant effect
    effect is when some influence lasts a certain number of rounds
    instance variable:
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