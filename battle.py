# """
# In this simple RPG game, the hero fights the  goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

# """
from lib.character import Character
from hero import Hero
from goblin import Goblin
from goblin1 import Zombie_Goblin

bob_zombie = Zombie_Goblin('Bob from accounting', 'Bob Zombie', 'he rocks!!!!', 10, 4, 'leather cape', 'virulence', 9, 3)
print(bob_zombie.cover_name, bob_zombie.char_name, bob_zombie.ability, bob_zombie.health, bob_zombie.power, bob_zombie.clothing, bob_zombie.weapon, bob_zombie.meanness, bob_zombie.deception)

hydro = Hero('Basil McHerb', 'hydro', 'open the sky', 15, 5, 'turquoise raincoat', 'bucket of rain', 8, 4)
print(hydro.cover_name, hydro.char_name, hydro.ability, hydro.health, hydro.power, hydro.clothing, hydro.weapon, hydro.goodness, hydro.cunning)


def main(mutant1, mutant2):
    while mutant1.is_alive() > 0 and mutant2.is_alive() > 0:
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. fight zombie")
        print("3. do nothing")
        print("4. flee")
        user_input = input()
        if user_input == "1":
            mutant2.attack(mutant1)     
            mutant2.print_status(mutant1)
        elif user_input == "2":
           mutant1.undead(mutant2)
        elif user_input == "3":
            pass
        elif user_input == "4":
            print("Have you no honor? Git outta here!.")
            break
        else:
            print(f'Your true nemesis is your typos. {user_input} is not a valid selection.')

        if mutant1.health > 0:
            mutant1.attack(mutant2)


main(bob_zombie, hydro)