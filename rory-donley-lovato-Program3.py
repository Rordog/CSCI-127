# -----------------------------------------+
# CSCI 127, Joy and Beauty of Data         |
# Program 3: Classics CSV Library          |
# Rory Donley-Lovato                       |
# Last Modified: October 13, 2020          |
# -----------------------------------------+
# Analyzes classic.csv for longest book,   |
# most difficult book, and finds books by  |
# last name of author.                     |
# -----------------------------------------+

# Creates list of input options
def menu():
    print()
    print("1. Identify the longest book by word count.")
    print("2. List a range of books by difficulty rating.")
    print("3. Identify all books by certain author.")
    print("4. Identify all books not written in english.")
    print("5. Quit.")
    print()

# Finds and returns longest book
def longest(input_file):
    b = open(input_file, "r")
    maxb = 0
    word_count = []
    title = []
    # Checks length of every book
    for line in b:
        try:
            p = float(line.split(",")[-1])
            t = line.split(",")[3]
            maxb = max(maxb,p)
            word_count.append(p)
            title.append(t)
        except:
            pass
    index = word_count.index(maxb)
    book = title[index]
    print("The longest book is", book)
    b.close()
    
# Returns all books found in the Flesch-Kincaid grade formula bounded by user inputs
def fk_difficulty_range(input_file, least, most):
    c = open(input_file, "r")
    fk_all = []
    fk_line = []
    # Makes list of lists that contain FK grade and title
    for line in c:
        try:
            s = float(line.split(",")[23])
            t = line.split(",")[3]
            fk_line = [s, t]
            fk_all.append(fk_line)     
        except:
            pass
    fk_all.sort()
    # Checks list for results within input bounds
    for i in fk_all:
        if (least <= fk_all.index(i) <= most):
            print(fk_all.index(i), "-", i[1], "- Grade Level:", i[0])
        else:
            pass
    c.close()
    
    
# Finds books by author's last name
def all_books_by_author(input_file, author):
    d = open(input_file, "r")
    author_first = []
    author_last = []
    for line in d:
        a = line.split(",")[11]
        f = a.split(";")
        f.reverse()
        t = line.split(",")[3]
        # Places first and last names in lists to be checked against input
        if (len(f) > 1):
            author_first.append(f[0])
        else:
            author_first.append("")
        author_last.append(f[-1])
        if (author in author_last[-1]):
            print(t, "by", author_first[-1], author_last[-1])
        else:
           pass
    d.close()

# Identifies books not written in English
def foreign_lang(input_file):
    e = open(input_file, "r")
    author_first = []
    author_last = []
    for line in e:
        t = line.split(",")[3]
        a = line.split(",")[11]
        f = a.split(";")
        f.reverse()
        l = line.split(",")[1]
        if (len(f) > 1):
            author_first.append(f[0])
        else:
            author_first.append("")
        author_last.append(f[-1])
        # Puts language and title in list for access
        lang_all = [l, t]
        if (lang_all[0] == "bibliography.languages"):
            pass
        # Checks if language is English
        elif (lang_all[0] != "en"):
            print(t, "by", author_first[-1], author_last[-1])
        else:
            pass
    e.close()
    
def main():
    input_file = "classics.csv"
    choice = 0
    while (choice != 5):
        menu()
        choice = int(input("Enter your choice: "))
        print()
        if (choice == 1):
            longest(input_file)
        elif (choice == 2):
            least = int(input("Enter least difficult out of 1000 (e.g. 250): "))
            most = int(input("Enter most difficult out of 1000 (e.g. 300): "))
            print("Using the Flesch–Kincaid grade level formula.\n")
            fk_difficulty_range(input_file, least, most)
        elif (choice == 3):
            author = input("Enter last name of author (e.g. Dickens): ")
            all_books_by_author(input_file, author)
        elif (choice == 4):
            foreign_lang(input_file)
        elif (choice != 5):
            print("That is not a valid option.  Please try again.")
    print("Goodbye!")

# -----------------------------------------+

main()
