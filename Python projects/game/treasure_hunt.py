import random
import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You are a brave hero on a quest to find treasure!")
    print_pause("You enter the dungeon and see two doors.")
    print_pause("Which door do you choose? (1 or 2)")

def choose_door():
    door = input()
    if door == "1":
        print_pause("You open the door and see a fierce monster!")
        fight()
    elif door == "2":
        print_pause("You open the door and find a chest full of treasure!")
        print_pause("You win!")
    else:
        print_pause("Please enter a valid option (1 or 2)")
        choose_door()

def fight():
    print_pause("You draw your sword and prepare to fight!")
    monster_hp = random.randint(1, 10)
    while monster_hp > 0:
        print_pause("You attack the monster!")
        damage = random.randint(1, 5)
        monster_hp -= damage
        if monster_hp <= 0:
            print_pause("You defeat the monster and find a key!")
            choose_door()
        else:
            print_pause("The monster attacks you!")
            player_hp = random.randint(1, 5)
            print_pause(f"You take {player_hp} damage!")
            fight()

intro()
choose_door()
