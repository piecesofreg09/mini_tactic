from abc import ABC, abstractmethod


class Effect():
    @abstractmethod
    def __init__(self) -> None:
        super().__init__()
    
    @abstractmethod
    def change_speed(self):
        pass

    @abstractmethod
    def change_defense(self):
        pass

class SlowDown(Effect):

    def __init__(self) -> None:
        super().__init__()