from lib.character import Character 

class Hero(Character):
    def __init__(self, cover_name, char_name, ability, health, power, clothing, weapon, goodness=12, cunning=7):
        self.goodness = int(goodness)
        self.cunning = int(cunning)
        super(Hero, self).__init__(cover_name, char_name, ability, health, power, clothing, weapon) 



