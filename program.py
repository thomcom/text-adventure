#Now I am in insert mode.
#Text Editors Are Cool
#I am in insert mode by pressing 'i' (You can also get to insert mode 
#by pressing 'r', 'I', 'a', 'A")
#I save a file by typing ESCAPE to put me in command mode.  
#Then I type :w<ENTER>
#
#We aren't going to write a note file, we're going to write a Python program.
#
#Files that end .py are python executables

import random

class Monster:
    def __init__(self, monster_name):
        self.name = monster_name
        self.hitpoints = 10
        self.attacks = [[3,2],[2,3],[4,1]]
    def Summary(self):
        result_string = ""
        result_string += self.name + " has " + str(len(self.attacks)) + " attacks!\n"
        for damage_index in range(len(self.attacks)):
            result_string = result_string + str(self.attacks[damage_index][0]) + " attack with " + str(self.attacks[damage_index][1]) + " after shield points.\n"
        return result_string

class Adventurer(object):
    def __init__(self, class_name, home_name):
        self.hitpoints = 10
        self.the_class = class_name 
        self.spawn_point = home_name
        self.attacks = []
        self.special_attack = []
    def GetClassName(self):
        return self.the_class
    def PrintClassName(self):
        print "You are a " + self.the_class
    def Summary(self):
        result_string = "You can either:\n"
        for damage_index in range(len(self.attacks)):
            result_string = result_string + "Use attack No." + str(damage_index+1) + ":" + str(self.attacks[damage_index][0]) + " attack with " + str(self.attacks[damage_index][1]) + " after shield points.\n"
        result_string = result_string + "Or use your special attack:\n"
        result_string = result_string + str(self.special_attack[0]) + " attack with " + str(self.special_attack[1]) + "\n"
        return result_string

class Barbarian(Adventurer):
    def __init__(self):
        super(self.__class__, self).__init__("Barbarian","Cave")
        self.attacks = [[3,2],[2,3]]
        self.special_attack = [6,0]

class Hero(Adventurer):
    def __init__(self):
        super(self.__class__, self).__init__("Hero", "Home")
        self.attacks = [[3,2],[2,3]]
        self.special_attack = [1,2,3]
    def Summary(self):
       result_string = super(self.__class__, self).Summary()
       result_string = result_string + str(self.special_attack[2]) + " bonus attack on your next turn\n"
       return result_string

class Wizard(Adventurer):
    def __init__(self):
        super(self.__class__, self).__init__("Wizard", "Tower")
        self.attacks = [[3,2],[2,3]]
        self.special_attack = [2,4]

def create_hero(choice):
    if choice == 1:
        character = Barbarian()
    elif choice == 2:
        character = Hero() 
    elif choice == 3:
        character = Wizard()
    return character

def get_input():
    try:
        choice = input("Press Enter")
        return choice
    except SyntaxError, e:
        pass


def do_fight_between(hero, monster):
    print hero.the_class + " prepare to battle a " + monster.name
    print monster.Summary()
    get_input()
    print hero.Summary()
    

def main():
    print "You are an adventurer."
    print "Choose what kind of hero you are:"
    print "1. Barbarian"
    print "2. Hero"
    print "3. Wizard"
    choice = input("Your selection?")
    local_hero = create_hero(choice)
    local_hero.PrintClassName()
    list_of_monsters = [Monster("Troll"), Monster("Goblin"), Monster("Angry Dog")]
    random_monster_position = random.randint(0,2)
    random_monster = list_of_monsters[random_monster_position]
    fight_result = do_fight_between(local_hero, random_monster)

main()

