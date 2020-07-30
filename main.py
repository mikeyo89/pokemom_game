# Utility imports.
import random
import time
import sys

# Import other game mechanics.
from pokemon import *
from player import *
from battle import *

# Starter pokemons.
pokemons = [
    ['Bulbasaur', 'Grass', 1, 45, 49, 49, 45, 65, 65],
    ['Charmander', 'Fire', 1, 39, 52, 43, 65, 60, 50],
    ['Squirtle', 'Water', 1, 44, 48, 65, 43, 50, 64]
]

# First-time game event.
stats = pokemons[random.randint(0,2)]
player = Player()
players_pokemon = Pokemon(stats[0], stats[2], stats[1], stats[3], stats[4], stats[5], stats[6], stats[7], stats[8])

def assess_encounter_probability(paces, first_time):
    if paces > random.randint(5, 8):
        print("\nYou hear rustling...")
        time.sleep(1)
        print("From the bushes appears an enemy!\n")
        time.sleep(2)

        if first_time:
            print("Out of fear, you throw the ball to the ground.")
            time.sleep(3)
            print(f"\nFrom the ball, {players_pokemon.name} appears! {players_pokemon.name} will help you fight the enemy!")
        else:
            print(f"You summon {players_pokemon.name} to your aid!")
        
        time.sleep(4)
        
        return True
    
    else:
        return False

def battle():
    # Set enemy characteristics (random).
    enemy_attribute = ['Water', 'Fire', 'Grass', 'Wind'][random.randint(0,3)]
    min_level = 1 if players_pokemon.level < 3 else players_pokemon.level - 2
    enemy_level = random.randint(min_level, (players_pokemon.level + 3))
    enemy_stats = [(random.randint(30, 50) + (random.randint(3,6) * enemy_level)) for x in range(0,4)]
    enemy_stats += [(random.randint(50, 60) + (random.randint(3,6) * enemy_level)) for x in range(0,2)]

    # Set enemy stats.
    enemy = Pokemon('The Enemy', enemy_level, enemy_attribute, enemy_stats[0], enemy_stats[1], enemy_stats[2], enemy_stats[3], enemy_stats[4], enemy_stats[5])

    players_pokemon.show_all_stats()
    time.sleep(3)
    print('')
    enemy.show_all_stats()
    time.sleep(3)
    print('')

    the_battle = Battle(players_pokemon, enemy)
    outcome, xp = the_battle.commence_battle(players_pokemon, enemy)

    # Defeated the enemy.
    if outcome == 1:
        print(f"\n{players_pokemon.name} gained {xp} xp.\n")
        players_pokemon.update_stats(xp)
    # Lost to the enemy.
    elif outcome == 2:
        sys.exit()
    # Ran like a coward.
    elif outcome == 3:
        pass

    return

def main(first_time):
    """
    Runs the main game functions, such as movement and geospatial location of the player, and checks for battle probability.
    """

    print("\nNow, what would you like to do?")
    time.sleep(1)
    movement = input("\nMove forward (f), backward (b), leftward(l), or rightward(r): ").lower()
    paces = random.randint(4,10)
    moved = True

    if players_pokemon.max_hp > players_pokemon.hp:
        players_pokemon.hp += paces

        if players_pokemon.hp > players_pokemon.max_hp:
            players_pokemon.hp = players_pokemon.max_hp

    if movement in 'f':
        moved = player.assess_geospace(1,paces)
    elif movement in 'b':
        moved = player.assess_geospace(1,paces/-1)
    elif movement in 'l':
        moved = player.assess_geospace(0,paces/-1)
    elif movement in 'r':
        moved = player.assess_geospace(0,paces)
    else:
        print("Invalid entry. Try again.\n")
        time.sleep(1)
        return
    
    time.sleep(1)
    
    if moved:
        if assess_encounter_probability(paces, first_time):
            battle()

    return


while True:
    print("You open your eyes... ")
    time.sleep(1)
    print("You are alone in a vast field... and are holding nothing but a red ball.")
    time.sleep(2)

    first_time = True

    while players_pokemon.xp < 20000:
        main(first_time)
        first_time = False

    time.sleep(4)
    print("\nYour pokemon is essentially maxed out. You've finished this game. Congrats!")
    break
