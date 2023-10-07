import sys
from sys import argv
import string

def getstr() -> str:
    if len(argv) == 2:
        return argv[1]
    print("What is the text to count?")
    str = ""
    while True:
        char = sys.stdin.read(1)
        if char == "":
            print("")
            break
        elif char == '\n':
            str += char 
            break 
        str += char
    return str    

def print_info(str:str):
    print("The text contains ", len(str), "characters:")
    print(sum(1 for char in str if char.isupper()), "upper letters")
    print(sum(1 for char in str if char.islower()), "lower letters")
    print(sum(1 for char in str if char in string.punctuation), "punctuation marks")
    print(sum(1 for char in str if char == ' ' or char == '\n'), "spaces")
    print(sum(1 for char in str if char.isdigit()), "digits")

def main():
    if len(argv) > 2:
        print("AssertionError: to much argument provided")
        return 

    str = getstr()
    print_info(str)    
    return 

if __name__ == "__main__":
    main()