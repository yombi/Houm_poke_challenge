import poke_constants
import requests
import argparse

# How many pokemon have "at" and 2 "a" in their names?
def first_question():
    # Get a json file that contains pokemon names along with other information
    all_pokemon=requests.get(poke_constants.all_pokemon_url).json()
    counter=0
    for dict in all_pokemon["results"]:
        counter=counter+1 if "at" in dict["name"] and dict["name"].count('a')==2 else counter
    return counter

# How many pokemon can Raichu mate with <3 ?
def second_question():
    # List thats gonna be used to store Raichhu's mate partners
    raichus_partner=[]
    for i in range(1,poke_constants.egg_groups):
        # Set to True when the egg group contains "raichu"
        raichu=False
        # All pokemon from all egg_groups are gonna be put in here
        temp_list=[]
        # Get a json file that contains egg group information
        egg_group=requests.get(poke_constants.egg_group_url+str(i)).json()
        for dict in egg_group["pokemon_species"]:
            raichu= True if dict["name"] == "raichu" else raichu
            temp_list.append(dict["name"])
        # If the egg group contained raichu, then all of those pokemon are mate partners,i.e, we append them to the list
        if raichu:
            for pokemon in temp_list:
                raichus_partner.append(pokemon)
    # Set items are unordered, unchangeable, and do not allow duplicate values, i.e, we remove duplicates
    return len(set(raichus_partner))

# Max and min weight from first generation fighting pokemon
def third_question():
    max=0
    min=100000
    for i in range(1,152):
        #Get a json file that contains pokemon specific information
        pokemon=requests.get(poke_constants.pokemon_url+str(i)).json()
        for dict in pokemon["types"]:
            #If the pokemon is a fighting type, we are gonna compare its weight
            if dict["type"]["name"] == "fighting":
                max= pokemon["weight"] if pokemon["weight"] > max else max
                min= pokemon["weight"] if pokemon["weight"] < min else min
                continue
    #Returning max and min weight as a list
    return [max,min]

if __name__ == "__main__":
    # Parsing arguments from the command line
    parser = argparse.ArgumentParser()
    parser.add_argument('-f',action='store_true',help="How many pokemon have \"at\" and 2 \"a\" in their names?",dest='first')
    parser.add_argument('-s',action='store_true',help="How many pokemon can Raichu mate with <3 ?",dest='second')
    parser.add_argument('-t',action='store_true',help="Max and min weight from first generation fighting pokemon",dest='third')
    args=parser.parse_args()
    if args.first:
        print("\n¿Cuantos pokemones poseen en sus nombres \"at\" y tienen 2 \"a\" en su nombre, incluyendo la primera del \"at\"?")
        print(first_question())
    if args.second:
        print("\n¿Con cuántas especies de pokémon puede procrear raichu?")
        print(second_question())
    if args.third:
        print("\nMáximo y mínimo peso de los pokémon de tipo fighting de primera generación")
        print("\n--------Esta es la opción más tardada debido a la cantidad de peticiones que hay que hacer--------")
        print("\t\t\t\t------NO DESESPERES-----")
        print(third_question())
