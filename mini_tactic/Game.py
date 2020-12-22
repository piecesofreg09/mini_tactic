'''
in one turn of game, it should be be processed like this
process and find target for each hero
set the stat before skills and traits: 
    - damage to be dealt to each hero
apply skills: 
    - this step might change stats, including speed, hp, defense
    - one skill only belongs to one hero
    - this skill is basically a simple version of trait
    - skill has cooldown period
apply traits: this traits might belong to multiple heros
    - this step might change stats too
    - attach effects on heroes that are influenced
    - for example:
        - duelist will increase certain hero's speed
        - venomist will decrease other hero's health
apply effects: 
    - (effects that change hp, cp, defense) this step migth change stats too
    - apply the effects
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