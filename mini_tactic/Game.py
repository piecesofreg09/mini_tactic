'''
in one turn of game, it should be be processed like this
process and find target for each hero
set the stat before skills and traits: 
    - damage to be dealt to each hero
apply skills: this step might change stats, 
    including speed, hp, defense
apply traits: this step might change stats too
apply effects: (effects that change hp, cp, defense) this step migth change stats too
apply change:
    - set defense
    - deal damage (based on damage level)
    - effect count decrease
check survivors:
    - remove dead heros
'''
class Game:
    def __init__(self) -> None:
        super().__init__()
    
    def run_game(self):
        pass

    def process_target(self):
        pass

    def apply_skills(self):
        pass

    def apply_traits(self):
        pass

    def deal_damage(self):
        pass

    def check_survivors(self):
        pass