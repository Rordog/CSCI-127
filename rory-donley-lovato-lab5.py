# --------------------------------------
# CSCI 127, Lab 5                       |
# September 22, 2020                    |
# Rory Donley-Lovato                    |
# --------------------------------------

def average_magnitude(quake):
    quake = open("earthquakes.csv", "r")
    av = []
    ma2 = 0
    for line in quake:
        av_m = line.split(",")
        av.append(av_m[-8])
    del av[0]
    ma2 = [float(i) for i in av]
    ma = sum(ma2)
    mag = ma / len(ma2)
    fin_mag = round(mag, 2)
    quake.close()
    return fin_mag

def earthquake_locations(quake):
    quake = open("earthquakes.csv", "r")
    locations = []
    unique = []
    for line in quake:
        places = line.split(",")
        locations.append(places[-5])
    for i in locations:
        if i not in unique:
            unique.append(i)
    unique.sort()
    unique.pop()
    print("Alphabetical Order of Earthquake Locations")
    print("------------------------------------------")
    for i in unique:
        print(unique.index(i) +1, end='. ')
        print(i)
    quake.close()

def count_earthquakes(quake, lower_bound, upper_bound):
    quake = open("earthquakes.csv", "r")
    quaks = []
    qu2 = 0
    big_quak = []
    for line in quake:
        qua = line.split(",")
        quaks.append(qua[-8])
    del quaks[0]
    qu2 = [float(i) for i in quaks]
    for i in qu2:
        if (lower_bound <= i <= upper_bound):
            big_quak.append(i)
    fin_quak = len(big_quak)
    return fin_quak
    quake.close()

# --------------------------------------

def main(quake):
    quake = open("earthquakes.csv", "r")
    magnitude = average_magnitude(quake)
    print("The average earthquake magnitude is", magnitude, "\n")
    
    earthquake_locations(quake)
    
    
    
    lower_bound = float(input("\nEnter a lower bound for the magnitude: "))
    upper_bound = float(input("Enter an upper bound for the magnitude: "))
    how_many = count_earthquakes(quake, lower_bound, upper_bound)
    print("Number of recorded earthquakes between", lower_bound, "and", upper_bound, "=", how_many)
    
# --------------------------------------

main("earthquakes.csv")
