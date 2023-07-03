# --------------------------------------
# CSCI 127, Lab 7                      |
# October 6, 2020                      |
# Rory Donley-Lovato                   |
# --------------------------------------

def create_dictionary(file_name): 
    codes = open("ascii-codes.csv", "r")
    cipher = {}
    for line in codes:
        bin_code = line.split(",")
        bin_code[-1] = bin_code[-1].strip()
        if (bin_code[-1] == 'comma'):
            bin_code[-1] = ','
        if (bin_code[-1] == 'quote'):
            bin_code[-1] = '"'
        if (bin_code[-1] == 'space'):
            bin_code[-1] = ' '
        cipher[bin_code[-1]] = bin_code[0]
    codes.close()
    print(cipher)
    return cipher 
        
def translate(sentence, dictionary, file_name):
    end = open(file_name, "w")
    for char in sentence:
       if char in dictionary:
           printer = dictionary[char] + "    " + char
           end.write(printer + '\n')  
       else:
           end.write("Undefined" + "\n")
    end.close()
  
    
# --------------------------------------
def main():
    dictionary = create_dictionary("ascii-codes.csv")
    sentence = "A long time ago in a galaxy far, far away..."
    translate(sentence, dictionary, "output-1.txt")
    sentence = "Montana State University (406) 994-0211"
    translate(sentence, dictionary, "output-2.txt")
    sentence = "“True friends stab you in the front.” —Wilde"
    translate(sentence, dictionary, "output-3.txt")

# --------------------------------------

main()
