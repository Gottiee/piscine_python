import sys

if len(sys.argv) > 2:
    print ("AssertionError: more than one argument is provided")
    exit(1)
if len(sys.argv) == 1:
    print("AssertionError: no argument is provided")
    exit(1)

try:
    int_argv = int(sys.argv[1])
    if int_argv % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")
