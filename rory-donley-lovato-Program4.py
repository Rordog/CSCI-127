import string

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Program 4: Pokedex                    |
# ROry Donley-Lovato                    |
# Last Modified: October 27, 2020       |
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

# Prints menu with all possible functions
def print_menu():
    print("1. Print Pokedex")
    print("2. Print Pokemon by Name")
    print("3. Print Pokemon by Number")
    print("4. Count Pokemon by Type")
    print("5. Print Average Pokemon Combat Points")
    print("6. Quit\n")

# Creates Pokemon object
class Pokemon:

# Defines all attributes of Pokemon
    def __init__(self, name, number, combat_points, types):
        self.name = name
        self.number = number
        self.combat_points = combat_points
        self.types = types
        self.fintypes = ""

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_combat_points(self):
        return self.combat_points
# Transforms list of types into a string
    def get_types(self):
        self.fintypes = ""
        for i in self.types:
            self.fintypes += str(i) + " and "
        return self.fintypes[:-4]

# Transforms all attributes into a usable string    
    def __str__(self):
        result = ""
        result += "Number: " + str(self.number) + ", Name: " + self.name.capitalize() + ", CP: " + str(self.combat_points) + ", Type: " + self.get_types()
        return result

# Prints all Pokemon in Pokedex
def print_pokedex(pokedex):
    print("\nThe Pokedex")
    print("-----------")
    for pokemon in pokedex:
        print(pokemon)
            
# Finds Pokemon by name input
def lookup_by_name(pokedex, name):
    for pokemon in pokedex:
        if pokemon.get_name() == name:
            print(pokemon)

# Finds Pokemon by number input
def lookup_by_number(pokedex, number):
    for pokemon in pokedex:
        if pokemon.get_number() == number:
            print(pokemon)

# Counts all Pokemon that share the same type
def total_by_type(pokedex, pokemon_type):
    t = 0
    for pokemon in pokedex:
        if pokemon_type in pokemon.get_types():
            t += 1
    print("Number of Pokemon that contain type", pokemon_type, "=", t)

# Calculates the average combat points of all Pokemon in Pokedex
def average_hit_points(pokedex):
    x = 0
    for pokemon in pokedex:
        x += pokemon.get_combat_points()
    y = x/len(pokedex)
    print("Average Pokemon combat points =", round(y, 2))
    


# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def create_pokedex(filename):
    pokedex = []
    file = open(filename, "r")
    
    for pokemon in file:
        pokelist = pokemon.strip().split(",")
        number = int(pokelist[0])               # number
        name = pokelist[1]                      # name
        combat_points = int(pokelist[2])        # hit points
        types = []
        for position in range(3, len(pokelist)):
            types += [pokelist[position]]       # type
        pokedex += [Pokemon(name, number, combat_points, types)]

    file.close()
    return pokedex

# ---------------------------------------

def get_choice(low, high, message):
    legal_choice = False
    while not legal_choice:
        legal_choice = True
        answer = input(message)
        for character in answer:
            if character not in string.digits:
                legal_choice = False
                print("That is not a number, try again.")
                break 
        if legal_choice:
            answer = int(answer)
            if (answer < low) or (answer > high):
                legal_choice = False
                print("That is not a valid choice, try again.")
    return answer

# ---------------------------------------

def main():
    pokedex = create_pokedex("pokedex.txt")
    choice = 0
    while choice != 6:
        print_menu()
        choice = get_choice(1, 6, "Enter a menu option: ")
        if choice == 1:    
            print_pokedex(pokedex)
        elif choice == 2:
            name = input("Enter a Pokemon name: ").lower()
            lookup_by_name(pokedex, name)
        elif choice == 3:
            number = get_choice(1, 1000, "Enter a Pokemon number: ")
            lookup_by_number(pokedex, number)
        elif choice == 4:
            pokemon_type = input("Enter a Pokemon type: ").lower()
            total_by_type(pokedex, pokemon_type)
        elif choice == 5:
            average_hit_points(pokedex)
        elif choice == 6:
            print("Thank you.  Goodbye!")
        print()

# ---------------------------------------

main()
