from classes.game import Person, Bcolor
from pip._vendor.colorama import  init, Fore, Back, Style
init(convert=True)

magic = [{"name":"Fire", "cost": 10, "dmg": 100},
         {"name":"Thunder", "cost": 10, "dmg": 120},
         {"name":"Blizzard", "cost": 10, "dmg": 140}]

player = Person(460,65,60,34,magic)  
enemy = Person(1200, 65, 45 ,25, magic)

running = True
i = 0

print(Bcolor.FAIL + Bcolor.BOLD + "AND ENEMY ATTACKS" + Bcolor.ENDC)

while running:
    print("==========================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage. Enemy HP:", enemy.get_hp())
    if index == 1:
        print("==========================")
        player.choose_magic()
        magic_choice = int(input("Choose magic: "))-1
        spell = player.get_spell_name(magic_choice)
        cost = player.get_spell_mp_cost(magic_choice)

        current_mp = player.get_mp()

        if current_mp < cost:
            print(Bcolor.Fail + "\nNot enough MP\n" + Bcolor.ENDC)
            continue

        player.reduce_mp(cost)
        magic_dmg = player.generate_spell(magic_choice)
        enemy.take_damage(magic_dmg)
        print(Bcolor.OKBLUE + "\n" + spell + " deals", str(magic_dmg), "points of damage" + Bcolor.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "Player HP:", player.get_hp())

    print("--------------------------")

    if enemy.get_hp() == 0:
        print(Bcolor.OKGREEN + "You win!" + Bcolor.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolor.FAIL + "Your enemy has defeated you!" + Bcolor.ENDC)
        running = False
   
    print("Enemy HP:", Bcolor.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolor.ENDC)
    print("Your HP:", Bcolor.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolor.ENDC)
    print("Your MP:", Bcolor.OKBLUE + str(player.get_hp()) + "/" + str(player.get_max_mp())+ Bcolor.ENDC)