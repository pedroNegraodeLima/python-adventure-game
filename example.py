import sys
import os
import random
import time

def print_slow(str, delay = 0.1):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(delay)
    print('\n')

def reset_console():
    print('\n')
    os.system('cls||clear')

def fprint(str, delay = 0):
    print('\n' + str)
    time.sleep(delay)

def sprint(str, delay = 0):
    print(str)
    time.sleep(delay)

def entry():
    print_slow("Birds will bit your face!", 0.1)
    fprint('You are in a dark cave. The entry has been sealed by falling rocks. There is no way out.', 1)
    print('Ahead, you see a cavern. Will you continue?')
    while True:
        action = input('\n>')
        if action == 'yes':
            cavern()
        elif action == 'no':
            fprint("A bat flies over your head and you hear screetches in the distance.")
        else:
            fprint("You sit in total darkness wondering if there's a way out.")

def cavern():
    fprint("You stumble into a dimly lit cavern.", 1)
    print("You cannont go righ or left but the cave continues ahead. Will you go on?")
    while True:
        action = input('\n>')
        if action == 'yes':
            hallway()
        elif action == 'no':
            fprint("You sit down and eat some food you bought with you.")
        else:
            fprint("You shiver from the cold.")

def hallway():
    fprint("You are in a wide hallway. It continues on indefinitely.", 1)
    print("There is no turning back. Will you go on?")
    while True:
        action = input('\n>')
        if action == 'yes':
            pit()
        elif action == 'no':
            fprint("You try to call for help but there is no one to hear you.")
        else:
            fprint("You wonder what time it is.")

def pit():
    fprint("You fall head first into a ominous and languid pit.", 2)
    sprint("Luckly you only landed on your back. You loose your breath for a while but don't seem to be injuried in any way.", 1)
    print("You can try to clim out. Will you try?")
    while True:
        action = input('\n>')
        if action == 'yes':
            fprint("You try to climb but you slide off of the rocky wall and fall down again", 1)
            print("Game Over.")
            sys.exit()
        elif action == 'no':
            fprint("You sit in utter darkness. Alone.")
        else:
            fprint("You feel hopeless.")

entry()