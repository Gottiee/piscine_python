from sys import argv

def getstr() -> str:
    if len(argv) == 2:
        return argv[1]
    return input("What is the text to count?\n")
        


def main():
    if len(argv) > 2:
        print("AssertionError: to much argument provided")
        return 

    str = getstr()
    print(str)
    

if __name__ == "__main__":
    main()