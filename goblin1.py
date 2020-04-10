from goblin import Goblin

class Zombie_Goblin(Goblin):

    def undead(self, enemy):
        enemy.health -= self.power
        enemy.goodness -= self.meanness             #meanness substracts from hero's goodness
        self.deception -= enemy.cunning         #hero's cunning counteracts villain's deception                    
        if enemy.health <= 0:
            print(f"{enemy.char_name} undead.")
        if self.health <=0:
            print(f'{self.name} is still undead, only nicer now.')



