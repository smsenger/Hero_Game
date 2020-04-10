from lib.character import Character

class Goblin(Character):
   def __init__(self, cover_name, char_name, ability, health, power, clothing, weapon, meanness=7, deception=8):
        self.meanness = meanness
        self.deception = deception
        super(Goblin, self).__init__(cover_name, char_name, ability, health, power, clothing, weapon)





