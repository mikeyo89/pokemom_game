import random
import time
from pokemon import *

class Battle:
    """
    Capture the battle status, turns, damage multiplier, pokemon health, and more.
    Keeping the battle code organized using a seperate .py file.
    """

    def __init__(self, player, enemy):
        super().__init__()
        # Battle conditions.
        self.player = player
        self.enemy = enemy
        self.player_turn = False
        self.first_round = True
        self.multiplier = 1.0
        self.battle_end = False
        self.crit = 1.0
        self.xp = 0

    def assess_turns(self):
        """
        Keep track of whose turn it is.
        """
        if self.first_round:
            if self.player.spd > self.enemy.spd:
                self.player_turn = True
            else:
                self.player_turn = False

            self.first_round = False
        else:
            if self.player_turn:
                self.player_turn = False
            else:
                self.player_turn = True

    def assess_attributes(self):
        """
        Assess the attributes of the pokemons and calculate damage accordingly.
        """
        # Attributes.
        water = 'Water'
        grass = 'Grass'
        fire = 'Fire'
        wind = 'Wind'

        # Pokemons Attributes.
        player = self.player.attribute
        enemy = self.enemy.attribute

        # Cascaded if statements to handle all attribute cases.
        if player == water:
            if enemy == water or grass:
                self.multiplier = 1.0
            elif enemy == wind:
                self.multiplier = 0.5
            elif enemy == fire:
                self.multiplier = 2.0

        elif player == fire:
            if enemy == water:
                self.multiplier = 0.5
            elif enemy == wind or fire:
                self.multiplier = 1.0
            elif enemy == grass:
                self.multiplier = 2.0
        
        elif player == grass:
            if enemy == wind:
                self.multiplier = 2.0
            elif enemy == fire:
                self.multiplier = 0.5
            elif enemy == grass or water:
                self.multiplier = 1.0
        
        elif player == wind:
            if enemy == wind or water:
                self.multiplier = 1.0
            elif enemy == fire:
                self.multiplier = 2.0
            elif enemy == grass:
                self.multiplier = 0.5

    def assess_crits(self):
        """
        Assess the probability of crits and calculate accordingly.
        """
        player_crit_chance = random.randint(1, self.player.spd)
        enemy_crit_chance = random.randint(1, self.enemy.spd)

        if self.player_turn:
            if player_crit_chance > (self.enemy.spd / 2):
                self.crit = 2
            else:
                self.crit = 1
        else:
            if enemy_crit_chance > (self.player.spd / 2):
                self.crit = 2
            else:
                self.crit = 1

    def assess_move(self, player, enemy):
        """
        Assess the outcome of this turns move (Pokemon KO? Like what happened man).
        """
        if player.hp <= 0:
            print(f"{enemy.name} has defeated {player.name} and then proceeds to attack you too!")
            time.sleep(3)
            print("\nGame over :(")
            return (2, 0)
        elif enemy.hp <= 0:
            print(f"\n{enemy.name} has fainted.")
            time.sleep(2)
            print(f"\n{player.name} has defeated {enemy.name}!")
            time.sleep(2)
            return (1, self.xp * 2)
        else:
            return self.commence_battle(player, enemy)
    
    def commence_battle(self, player, enemy):
        """
        Commence the battle!
        """
        self.assess_turns()
        self.assess_attributes()
        self.assess_crits()

        if self.player_turn:
            print('\nNow, what would you like to do?')
            choice = input(f"A - Attack\nB - Rest(Heal)\nC - Run away\n").lower()

            if choice not in ['a', 'b', 'c']:
                print("Invalid choice.")
                time.sleep(1)
            elif choice == 'a':
                if self.crit > 1:
                    damage = int((random.randint(int(player.specAtk / 1.5), int(player.specAtk * 2))/5) * self.multiplier) * self.crit
                else:
                    damage = int((random.randint(int(player.atk / 1.5), int(player.atk * 2))/5) * self.multiplier) * self.crit
                
                damage *= ((100 - (enemy.defense / 8))/100)
                damage = int(damage)
                enemy.hp -= damage
                print(f"\n{player.name} dealt {damage} damage to {enemy.name}.")

                if self.crit > 1:
                    time.sleep(2)
                    print("\nIt was a critical hit!")
                    time.sleep(2)
                
                self.xp += damage
            elif choice == 'b':
                heal = random.randint(10, 20)

                if player.max_hp > player.hp:
                    player.hp += heal

                    if player.hp > player.max_hp:
                        player.hp = player.max_hp
                    
                    print(f"\nYou attempt first-aid, and successfully bring {player.name}'s health up to {player.hp}.")
                else:
                    print(f"\nYou apply a bandaid on {player.name}'s cut, but no health is gained.")
                
                self.xp += heal
            elif choice == 'c':
                print(f"\nYou and {player.name} cowardly run away to safety.")
                return (3, 0)
        else:
            enemy_move = random.randint(1,2)

            if enemy_move == 1:
                if self.crit > 1:
                    damage = int((random.randint(int(enemy.specAtk / 1.5), int(enemy.specAtk * 2))/5) * (1/self.multiplier)) * self.crit
                else:
                    damage = int((random.randint(int(enemy.atk / 1.5), int(enemy.atk * 2))/5) * (1/self.multiplier)) * self.crit

                damage *= ((100 - (player.defense / 8))/100)
                damage = int(damage)
                player.hp -= damage
                print(f"\n{enemy.name} dealt {damage} damage to {player.name}.")

                if self.crit > 1:
                    time.sleep(2)
                    print("It was a critical hit!")
                    time.sleep(2)

                self.xp += damage
            elif enemy_move == 2:
                heal = random.randint(8, 15)

                if enemy.max_hp > enemy.hp:
                    enemy.hp += heal

                    if enemy.hp > enemy.max_hp:
                        enemy.hp = enemy.max_hp
                    
                    print(f"\n{enemy.name}'s health is brought up to {enemy.hp}.")
                else:
                    print(f"\n{enemy.name} decides to heal, even though {enemy.name}'s health is maxed out.")
                
                self.xp += heal

        print('')
        player.show_battle_stats()
        time.sleep(2)
        print('')
        enemy.show_battle_stats()
        time.sleep(2)

        return self.assess_move(player, enemy)
