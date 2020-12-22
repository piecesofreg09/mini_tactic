from abc import abstractmethod, ABC
from .Hero import Hero

class Trait(ABC):

    @abstractmethod
    def __init__(self, name=None) -> None:
        super().__init__()
        self.name = name
    
    @abstractmethod
    def apply_trait(self, target_hero: Hero):
        pass


class Duelist():
    
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name