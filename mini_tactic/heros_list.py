import os, sys
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from Hero import Hero

'''
list of all available heros
'''

class Juno(Hero):
    
    def __init__(self):
        super().__init__()

    def process_trait(self):
        pass

    def process_skill(self):
        pass

class Lisa(Hero):
    def __init__(self):
        super().__init__()

    def process_trait(self):
        pass

    def process_skill(self):
        pass


class Pita(Hero):

    def __init__(self):
        super().__init__()

    def process_trait(self):
        pass

    def process_skill(self):
        pass

class Link(Hero):

    def __init__(self):
        super().__init__()

    def process_trait(self):
        pass

    def process_skill(self):
        pass