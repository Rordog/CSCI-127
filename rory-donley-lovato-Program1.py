# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 1: GPA Calculator 
# Rory Donley-Lovato
# Last Modified: Sept ??, 2020 
# ---------------------------------------
# This program takes the number of classes taken, the grades per class, and credits per class to calculate GPA.
# ---------------------------------------

def num_grade(letter_grade):
    if (letter_grade == "a"):
        status = 4.0
    elif (letter_grade == "a-"):
        status = 3.7
    elif (letter_grade == "b+"):
        status = 3.3
    elif (letter_grade == "b"):
        status = 3.0
    elif (letter_grade == "b-"):
        status = 2.7
    elif (letter_grade == "c+"):
        status = 2.3
    elif (letter_grade == "c"):
        status = 2.0
    elif (letter_grade == "c-"):
        status = 1.7
    elif (letter_grade == "d+"):
        status = 1.3
    elif (letter_grade == "d"):
        status = 1.0
    elif (letter_grade == "f"):
        status = 0.0
    else:
        status = print("That is an unrecognized grade."), main()
    return status

    
        
def main():
    num_class = int(input("\nEnter the number of courses you are taking: "))
    total_credits = 0
    total_gpa = 0
    if (1<=num_class<=7):
        for num_classes in range (1, num_class + 1):
            letter_prompt = "\nEnter grade for course " + str(num_classes) + ":"
            letter = input(letter_prompt)
            letter_grade = letter.lower()
            grade = num_grade(letter_grade)
            credit_prompt = "Enter credits for course " + str(num_classes) + ":"
            credit = int(input(credit_prompt))
            total_credits = total_credits + credit
            class_gpa = grade*credit
            total_gpa = total_gpa + class_gpa          
        true_GPA = total_gpa/total_credits
        GPA = round(true_GPA, 2)
        final_GPA = "Your GPA is " + str(GPA) + "."
        print(final_GPA)
    else:
        print("Please enter a reasonable amount of classes.")
    
main()
