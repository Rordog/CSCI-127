# -----------------------------------------------------
# CSCI 127, Lab 9                                     |
# October 20, 2020                                    |
# Rory Donley-Lovato                                  |
# -----------------------------------------------------

# Your solution goes here.  Do not change anything below.
class Stack:

    def __init__(self):
        self.items = []

    def push(self, number):
        self.items.append(number)
        
    def pop(self):
        popped = self.items.pop(-1)
        return popped
        

    def is_empty(self):
        if (len(self.items) == 0):
            return True

    def __iadd__(self, other):
        self.items.append(other)
        return self.__str__()

    def __str__(self):
        printr = ""
        for i in self.items:
            printr += str(i) + " "
        return printr
    

    

# -----------------------------------------------------

def main():
    numbers = Stack()

    print("Push 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.push(number)
        print("Contents:", numbers)

    print("\nPop one item")
    print("----------------")
    numbers.pop()
    print("Contents:", numbers)

    print("\nPop all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item popped:", numbers.pop())
        print("Contents:", numbers)

    # Push 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.push(number)

    # Push 15
    numbers += 15 # See: https://www.python-course.eu/python3_magic_methods.php
    print("\nPushed: 10, 11, 12, 13, 14, 15")
    print("-------------------------------")
    print("Contents:", numbers)

# -----------------------------------------------------

main()
