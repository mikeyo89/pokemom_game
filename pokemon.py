import random
import time

class Pokemon:
    """
    Base Pokemon Master class.
    """
    def __init__(self, name, level, attribute, hp, atk, defense, spd, specAtk, specDef):
        super().__init__()
        # Stats
        self.name = name
        self.attribute = attribute
        self.level = level
        self.max_hp = hp
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.spd = spd
        self.specAtk = specAtk
        self.specDef = specDef
        self.xp = 0
    
    def show_all_stats(self):
        if self.hp <= 0:
            self.hp = 0

        print('-----------------------------------------------------')
        print(f'Name: {self.name}')
        print(f'Level: {self.level}')
        print(f'Attribute: {self.attribute}')
        print(f'HP: {self.hp}')
        print(f'ATK: {self.atk}')
        print(f'DEF: {self.defense}')
        print(f'SPD: {self.spd}')
        print(f'SP_ATK: {self.specAtk}')
        print(f'SP_DEF: {self.specDef}')
        print('-----------------------------------------------------')
    
    def show_battle_stats(self):
        if self.hp <= 0:
            self.hp = 0

        print('-----------------------------------------------------')
        print(f'Name: {self.name}')
        print(f'Level: {self.level}')
        print(f'Attribute: {self.attribute}')
        print(f'HP: {self.hp}')
        print('-----------------------------------------------------')
    
    def update_stats(self, xp):
        """
        Add xp to this pokemon, then re-evaluate its level and new stats (if leveled up).
        """
        self.xp += xp
        level = 1

        # Level caps:
        # 1: 100xp
        if self.xp < 100:
            level = 1
        # 2: 250xp
        elif self.xp < 350:
            level = 2
        # 3: 450xp
        elif self.xp < 850:
            level = 3
        # 4: 700xp
        elif self.xp < 1200:
            level = 4
        # 5: 1000xp
        elif self.xp < 2000:
            level = 5
        # 6: 1300xp
        elif self.xp < 3000:
            level = 6
        # 7: 1600xp
        elif self.xp < 4500:
            level = 7
        # 8: 1900xp
        elif self.xp < 7000:
            level = 8
        # 9: 2500xp
        elif self.xp < 10000:
            level = 9
        # 10: Max Level.
        else:
            level = 10
        
        # Check if the pokemon leveled up.
        if not self.level == level:
            # Update level.
            self.level = level

            # Get a list of 6 random integers (between 3 and 6).
            gained_stats = [random.randint(3, 7) for x in range(0, 6)]

            # Add the new gained stats to the pokemon.
            self.max_hp += gained_stats[0]
            self.atk += gained_stats[1]
            self.defense += gained_stats[2]
            self.spd += gained_stats[3]
            self.specAtk += gained_stats[4]
            self.specDef += gained_stats[5]
            
            time.sleep(1)
            print(f'{self.name} has leveled up! New level: {self.level}')
            time.sleep(2)
            self.hp = self.max_hp
            print('-----------------------------------------------------')
            print(f'HP: {self.hp}')
            print(f'ATK: {self.atk}')
            print(f'DEF: {self.defense}')
            print(f'SPD: {self.spd}')
            print(f'SP_ATK: {self.specAtk}')
            print(f'SP_DEF: {self.specDef}')
            print('-----------------------------------------------------')
            time.sleep(4)