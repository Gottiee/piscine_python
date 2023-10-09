from sys import argv

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ': '/'}

def error():
    print("AssertionError: the arguments are bad")
    exit(1)

def main():
    if len(argv) != 2:
        error()
    str = argv[1].upper()
    for char in str:
        if char not in MORSE_CODE_DICT:
            error()
    for index, char in enumerate(str):
        print(MORSE_CODE_DICT[char], end="")
        if index != len(str) -1:
            print(end=" ")
        else:
            print(end="\n")

if __name__ == "__main__":
    main()