#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 0:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) > 0:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv)):
        if i > 0:
            print("{}: {}".format(i, sys.argv[i]))
