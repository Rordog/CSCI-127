# ---------------------------------------------
# CSCI 127, Lab 3                              |
# September 8, 2020                            |
# Rory Donley-Lovato                           |
# --------------------------------------------- 
# Calculate how many bilabial consonents       |
# (letters that make your lips touch: b, m, p) |
# are in a sentence using two techniques.      |
# ---------------------------------------------



def count_built_in(sentence):
    sub = "p"
    sentence.count(sub)
    sub_p = sentence.count(sub)
    sub = "b"
    sentence.count(sub)
    sub_b = sentence.count(sub)
    sub = "m"
    sentence.count(sub)
    sub_m = sentence.count(sub)
    status = sub_p + sub_b + sub_m
    return status
    
    pass

def count_iterative(sentence):
    count = 0
    for char in sentence:
        if char == "b":
            count = count+1
        elif char == "p":
            count = count+1
        elif char == "m":
            count = count+1
    status = count

    return status    
    #TODO: Count the number of bilabial consonents
    # without using the Python built-in method
    pass

# --------------------------------------

def main():
    answer = "yes"
    while (answer == "yes") or (answer == "y"):
        sentence = input("Please enter a sentence: ")
        sentence = sentence.lower()
        print()
        print("Counting bilabial consonents  using ...")
        print("---------------------------------------")
        print("Built-in function =", count_built_in(sentence))
        print("Iteration =", count_iterative(sentence))
        print()
        answer = input("Would you like to continue: ").lower()
        print()

# --------------------------------------

main()
