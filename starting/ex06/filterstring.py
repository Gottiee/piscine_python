from sys import argv
from ft_filter import ft_filter
    # creer un liste qui separe la string en mot -> utiliser une expression
    # filter les string qui font moin de nbr char-> utiliser un lambda

def main():
    if len(argv) != 3:
        print("AssertionError: the arguments are bad")
        exit(1)
    try:
        nbr = int(argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")

    word_list = argv[1].split()
    print(list(ft_filter(lambda x: len(x) > nbr, word_list)))


if __name__ == "__main__":
    main()