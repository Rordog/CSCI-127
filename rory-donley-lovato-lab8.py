# -----------------------------------------------------
# CSCI 127, Lab 8
# October 13, 2020
# Rory Donley-Lovato
# -----------------------------------------------------

class MSUContact:

    def __init__(self, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.title = ""
        self.line_number = phone[-4:]
        
    def get_first_name(self):
        return self.first_name

    def set_first_name(self, name):
        self.first_name = name

    def set_title(self, title):
        self.title = title
        
    def get_last_name(self):
        return self.last_name

    def get_phone(self):
        return self.phone

    def get_line_number(self):
        return self.line_number
    
    def print_entry(self):
        if (self.title != ""):
            full_name = self.title + " " + self.first_name + " " + self.last_name
        else:
            full_name = self.first_name + " " + self.last_name
        print('{:28}{}'.format(full_name, self.phone))
    
# -----------------------------------------------------
# Do not change anything below this line
# -----------------------------------------------------

def print_directory(contacts):
    print("MSU Contacts:")
    print("----------------------------------------")
    for person in contacts:
        person.print_entry()
    print("----------------------------------------\n")

# -----------------------------------------------------

def main():
    
    prof_892 = MSUContact("Daniel", "DeFrance", "406-994-1624")
    mascot = MSUContact("MSU", "Bobcat", "406-994-0000")
    director_CS = MSUContact("John", "Paxton", "406-994-5979")
    president = MSUContact("Waded", "Cruzado", "406-994-CATS")
    
    contacts = [prof_892, mascot, director_CS, president]

    mascot.set_first_name("Champ")
    
    prof_892.set_title("Instuctor")
    director_CS.set_title("Director")
    president.set_title("President")

    print_directory(contacts)
    
    contact = prof_892
    print(contact.get_first_name() + "'s MSU phone line is", \
          contact.get_line_number())

# -----------------------------------------------------

main()
