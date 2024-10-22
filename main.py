# from Util.A_stringPython import *
from random import randint

# - - - - - LOGIC- - - - -


def main():
    GenerateQuestion(0)
    return


# - - - - - FUNCTIONS- - - - -


def GenerateQuestion(difficulty: int, maxDiff: int = 2) -> int:
    """generate a addition, difficulty can be 0,1,2 , return the answer"""
    start: int
    end: int

    # check int difficulty is in correct range
    if difficulty < 0 or difficulty > maxDiff:
        print("ERROR, difficulty is not in correct range")
        exit(1)

    # create start and end based on difficulty
    match difficulty:
        case 0:
            start = 1
            end = 10
        case 1:
            start = 10
            end = 20
        case 2:
            start = 35
            end = 70

    # min and max value based on difficulty

    first = randint(start, end)
    sec = randint(start, end)

    # print the question
    print(f"{str(first)} + {str(sec)}")

    # return the answer
    return first + sec


main()
