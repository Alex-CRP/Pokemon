# PokemonGame

import random
import time

Pokemon = {
    "pihachu_characteristic": {
        "Attack1": 25, "Energy1": 25, "Info1": "Quick Attack", "PosOfStun1": 50,
        "Attack2": 20, "Energy2": 30, "Info2": "Iron Tail", "PosOfStun2": 75,
        "Attack3": 50, "Energy3": 55, "Info3": "ThunderBolt", "PosOfStun3": 55,
        "Info": {"Name": "Pikachu", "Type": "Electric", "Weakness": "Fire", "Description": "When it is angered, it immediately discharges the energy stored in the pouches in its cheeks. "}
    },
    "charmander_characteristic": {
        "Attack1": 25, "Energy1": 15, "Info1": "Flamethrower", "PosOfStun1": 5,
        "Attack2": 35, "Energy2": 20, "Info2": "Claws", "PosOfStun2": 5,
        "Attack3": 50, "Energy3": 60, "Info3": "Fiery rain", "PosOfStun3": 10,
        "Info": {"Name": "Charmander","Type": "Fire", "Weakness": "Water", "Description": "It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail."}
    },
    "squirtle_characteristic": {
        "Attack1": 25, "Energy1": 20, "Info1": "Water Ball", "PosOfStun1": 20,
        "Attack2": 35, "Energy2": 35, "Info2": "Bite", "PosOfStun2": 10,
        "Attack3": 30, "Energy3": 40, "Info3": "3 little water balls", "PosOfStun3": 45,
        "Info": {"Name": "Squirtle","Type": "Water", "Weakness": "Electric", "Description": "When it retracts its long neck into its shell, it squirts out water with vigorous force."}
    }
}
# Справочники с характеристиками покемонов

PokemonChoice = True
Health, EnemyHealth, YourEnergy, EnemyEnergy = 100, 115, 100, 100

EnemyPokemon = random.randint(1,3)

if EnemyPokemon == 1:
    EnemyPokemon = Pokemon["pihachu_characteristic"].copy()
elif EnemyPokemon == 2:
    EnemyPokemon = Pokemon["charmander_characteristic"].copy()
else:
    EnemyPokemon = Pokemon["squirtle_characteristic"].copy() # Выбор покемона противником

def Energy(Attack, EnergyConsumption, PosOfStun, info): # Проверяет достаточно ли энергии для атаки у игрока
    global YourEnergy, EnemyHealth, Enemy_active
    if YourEnergy < EnergyConsumption:
        print("Oops, your pokemon are exhausted. You need to let it have a rest a bit")
        print("\n...\n")
        time.sleep(1.5)
    else:
        EnemyHealth -= Attack
        YourEnergy -= EnergyConsumption
        if random.randint(1, 100) <= PosOfStun:
            Enemy_active = False
        print("\n", name.capitalize(), ": ", YourPokemonName.capitalize(), " use \"", info, "\"!\n\n...\n", sep="")
        time.sleep(3)
        print("Success! You made the attack!\t Enemy's HP:", EnemyHealth)

def EnergyEnemy(Attack, EnergyConsumption, PosOfStun, info): # Проверяет достаточно ли энергии для атаки у противника
    global EnemyEnergy, Health, You_active
    if EnemyEnergy < EnergyConsumption:
        print("The enemy decided to let his pokemon have a rest this time")
    else:
        Health -= Attack
        EnemyEnergy -= EnergyConsumption
        if random.randint(1, 100) <= PosOfStun:
            You_active = False
        print("\nBe ready! The enemy is attaking!")
        time.sleep(3)
        print("Your opponent: ", EnemyPokemon["Info"]["Name"].capitalize(), " use \"", info, "\"!\n\n...", sep="")
        time.sleep(3)

def DoYouAgree(): # Подтверждение выбора покемона
    loop1 = True
    while loop1:
        Yes_No = input("\nDo you want to choose this one?\nEnter \"Yes\" or \"No\": ")
        if Yes_No.lower() == "no":
            loop1 = False
        elif Yes_No.lower() == "yes":
            loop1 = False
            global PokemonChoice
            PokemonChoice = False
            global YourPokemonName, YourPokemon
            if YourPokemonName == "pikachu":
                YourPokemon = Pokemon["pihachu_characteristic"].copy()
            elif YourPokemonName == "charmander":
                YourPokemon = Pokemon["charmander_characteristic"].copy()
            else:
                YourPokemon = Pokemon["squirtle_characteristic"].copy()
        else:
            print("Incorrect command")


name = input("Hi, a seeker of adventures! What's your name?\n")
print("\nToday you will be a participent of the Pokemon competition!\nYou need to opt for a pokemon from the list below:\nPikachu, Charmander, Squirtle")

while PokemonChoice:
    YourPokemonName = input("\nWhich pokemon do you want to opt for?\nI want ").lower()
    if YourPokemonName == "pikachu":
        print("Type:", Pokemon["pihachu_characteristic"]["Info"]["Type"],  "\nWeakness:", Pokemon["pihachu_characteristic"]["Info"]["Weakness"] ,"\nDescription:", Pokemon["pihachu_characteristic"]["Info"]["Description"])
        DoYouAgree()
    elif YourPokemonName == "charmander":
        print("Type:", Pokemon["charmander_characteristic"]["Info"]["Type"],  "\nWeakness:", Pokemon["charmander_characteristic"]["Info"]["Weakness"] ,"\nDescription:", Pokemon["charmander_characteristic"]["Info"]["Description"])
        DoYouAgree()
    elif YourPokemonName == "squirtle":
        print("Type:", Pokemon["squirtle_characteristic"]["Info"]["Type"],  "\nWeakness:", Pokemon["squirtle_characteristic"]["Info"]["Weakness"] ,"\nDescription:", Pokemon["squirtle_characteristic"]["Info"]["Description"])
        DoYouAgree()
    else:
        print("There is no such a pokemon")

        # Описание всех покемонов

print("\n" + name.capitalize() + ": " + YourPokemonName.capitalize() + ", I choose you!\n") # Выбор покемона
time.sleep(3) # Данная команад вызывает паузу в 3 секунды
print("Your enemy has chosen a", EnemyPokemon["Info"]["Name"])
time.sleep(1.5)
You_active = True
Enemy_active = True

while Health > 0 and EnemyHealth > 0: # Цикл не заканчивается пока кто-то не проиграет

    if You_active == True:


        print("\nYour HP:", Health, ";\tYour energy: ", YourEnergy, ";\tEnemy's HP: ", EnemyHealth, ";", sep="")
        print("Your turn! Chose an attack:\n\n1)\"" + YourPokemon["Info1"] + "\": Attack - " + str(YourPokemon["Attack1"]) + ", Energy consumption - " + str(YourPokemon["Energy1"]) + ", Possibility of stun - " + str(YourPokemon["PosOfStun1"]) + "%" )
        print("2)\"" + YourPokemon["Info2"] + "\": Attack - " + str(YourPokemon["Attack2"]) + ", Energy consumption - " + str(YourPokemon["Energy2"]) + ", Possibility of stun - " + str(YourPokemon["PosOfStun2"]) + "%" )
        print("3)\"" + YourPokemon["Info3"] + "\": Attack - " + str(YourPokemon["Attack3"]) + ", Energy consumption - " + str(YourPokemon["Energy3"]) + ", Possibility of stun - " + str(YourPokemon["PosOfStun3"]) + "%" )
        print("4) Wait\n")

        # Список атак

        ChoiceAttack = int(input())
        if ChoiceAttack == 1:
            Energy(YourPokemon["Attack1"], YourPokemon["Energy1"], YourPokemon["PosOfStun1"], YourPokemon["Info1"])
        elif ChoiceAttack == 2:
            Energy(YourPokemon["Attack2"], YourPokemon["Energy2"], YourPokemon["PosOfStun2"], YourPokemon["Info2"])
        elif ChoiceAttack == 3:
            Energy(YourPokemon["Attack3"], YourPokemon["Energy3"], YourPokemon["PosOfStun3"], YourPokemon["Info3"])
        else:
            print("You decided to save your strength")

        # Выбор атаки, есть возможность застанить врага

    You_active = True
    if Enemy_active == False:
        time.sleep(3)
        print("\nYou stunned the enemy!")
    if EnemyHealth <= 0:
        break

    if Enemy_active == True:
        time.sleep(3)
        EnemyChoiceAttack = random.randint(1,3)
        if EnemyChoiceAttack == 1:
            EnergyEnemy(EnemyPokemon["Attack1"], EnemyPokemon["Energy1"], EnemyPokemon["PosOfStun1"], EnemyPokemon["Info1"])
        elif EnemyChoiceAttack == 2:
            EnergyEnemy(EnemyPokemon["Attack2"], EnemyPokemon["Energy2"], EnemyPokemon["PosOfStun2"], EnemyPokemon["Info2"])
        elif EnemyChoiceAttack == 3:
            EnergyEnemy(EnemyPokemon["Attack3"], EnemyPokemon["Energy3"], EnemyPokemon["PosOfStun3"], EnemyPokemon["Info3"])
        EnemyEnergy += 10
    Enemy_active = True
    # Атака противника, тут все аналогично
    if You_active == False:
        print("Oh no, you were just stunned!\tYour HP:", Health)
        time.sleep(3)
    else:
        YourEnergy += 10
    # Энергия в конце хода прибавляется только в том случае, если покемон не в стане

time.sleep(1.5)
if Health <= 0:
    print("\n ", name.capitalize(), ": Oh, no, I have been defeated", sep="")
    time.sleep(1.5)
    print("Judge: ", YourPokemonName, " can't go on fighting! The winner is ", EnemyPokemon["Info"]["Name"], sep="")
else:
    print("\n", name.capitalize(), ": Yeah! We did it!")
    time.sleep(2)
    print("Judge: ", EnemyPokemon["Info"]["Name"], " can't go on fighting! The winner is ", YourPokemonName, sep="")

# Вывод результатов боя