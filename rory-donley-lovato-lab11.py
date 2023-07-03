import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# CSCI 127, Lab 11                                |
# Nov 10, 2020                                    |
# Rory Donley-Lovato                              |
# -------------------------------------------------

def read_file(file_name):
    enrollment = open(file_name, "r")
    numbers = []
    names = []
    people = []  
    for line in enrollment:
        items = line.split(",")
        numbers = np.append(numbers, items[0])
        names = np.append(names, items[1])
    numbers = np.delete(numbers, 0)
    for i in numbers:
        people.append(int(i))
    names = np.delete(names, 0)
    c = (names, people)
    return c

# -------------------------------------------------

def main(file_name):
    college_names, college_enrollments = read_file(file_name)
    plt.figure("MSU Enrollments")
    plt.bar(college_names, college_enrollments, color=["gold", "dodgerblue"])
    plt.xlabel("College")
    plt.ylabel("Enrollment")
    plt.title("Fall 2020")
    plt.ylim([0, 5000])
    plt.show()
    
# -------------------------------------------------

main("fall-2020.csv")
