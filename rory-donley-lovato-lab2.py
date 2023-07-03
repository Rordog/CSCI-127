# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Lab 2: Season Checker
# Rory Donley-Lovato
# Last Modified: September 1, 2020 
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------


# TODO: write a function called season_checker that returns
#  a string: Spring, Summer, Winter, Fall, or Invalid

def season_checker(month, user_day):
    if (month == "march" and 20 <= user_day < 32) or (month=="april" and 1<=user_day<31) or (month=="may" and 1<=user_day<32) or (month=="june" and 1<=user_day<21):
        status = "That's a Spring day."
    elif (month=="june" and 21<=user_day<31) or (month=="july" and 1<=user_day<32) or (month=="august" and 1<=user_day<31) or (month=="september" and 1<=user_day<22):
        status = "That's a Summer day."
    elif (month=="september" and 22<=user_day<31) or (month=="october" and 1<=user_day<32) or (month=="november" and 1<=user_day<31) or (month=="december" and 1<=user_day<21):
        status = "That's a Fall day."
    elif (month=="december" and 21<=user_day<32) or (month=="january" and 1<=user_day<32) or (month=="february" and 1<=user_day<30) or (month=="march" and 1<=user_day<20):
        status = "That's a Winter day."
    else:
        print("That's an unrecognized date.")
    return status

def main():
    user_month = input("Enter month: ")
    month = user_month.lower()
    user_day = int(input("Enter day: "))
    season = season_checker(month, user_day)
    print(season)

    # TODO: output the season for the user in a print statement,
    # or tell them if they input an invalid date


main()
