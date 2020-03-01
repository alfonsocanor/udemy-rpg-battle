import random
from pip._vendor.colorama import init
init()

class Bcolor:
    HEADER = '\033[95n'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92n'
    WARNING = '\033[93n'
    FAIL = '\033[91n'
    ENDC = '\033[0n'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4n'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.action = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp
    
    def get_max_hp(self):
        return self.maxHp
    
    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(Bcolor.OKBLUE + Bcolor.BOLD + "Actions" + Bcolor.ENDC)
        for item in self.action:
            print(str(i) + ":", item)
            i += 1
    
    def choose_magic(self):
        i = 1
        print(Bcolor.OKBLUE + Bcolor.BOLD + "Magic" + Bcolor.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["mp"]) + ")")
            i += 1