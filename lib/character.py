#create Character class
class Character():
    def __init__(self, cover_name, char_name, ability, health, power, clothing, weapon):
        self.cover_name = cover_name
        self.char_name = char_name
        self.ability = ability
        self.health = health
        self.power = power
        self.clothing = clothing
        self.weapon = weapon

    def is_alive(self):
        return self.health

    def print_status(self, enemy):
        print(f"You have {self.health} health and {self.power} power.")
        print(f"The {enemy.char_name} has {enemy.health} and {enemy.power}")

#self is attacker, enemy is victim
    def attack(self, enemy):
        enemy.health -= self.power
        print(f'{self.char_name} does damage to {enemy.char_name}.')
        if enemy.health <= 0:
            print(f"{enemy.char_name} dead.")
