# from Util.A_stringPython import *
from random import randint

# - - - - - LOGIC- - - - -


def main():
    # - - - - VARIABLE - - - -
    # nbOfQuestion by batch
    nbQuestionBatch: int = 5
    # nb of correct question to get to the next level
    half = round(nbQuestionBatch / 2)
    # nb correct questiom
    correctAnswer: int = 0
    # nb total correct questiom
    totalCorrectAnswer: int = 0

    # start the loop of guess
    for difficulty in range(3):
        print(difficulty)
        # for each , ask a batch of question
        correctAnswer += SetOfQuestions(nbQuestionBatch, difficulty)

        # add correctAnswer to total correct answer
        totalCorrectAnswer += correctAnswer

        # check if you have reach the end
        if difficulty == 2:
            print(
                f"you have finish the game! , your total score is {totalCorrectAnswer}/{nbQuestionBatch*difficulty}"
            )
            break

        # you have score more than half of good answer , and can keep going
        if correctAnswer > half:
            print(
                f"you score is {correctAnswer} out of {nbQuestionBatch},Keep going!",
            )
        else:
            # you have score less tha
            print(f"you lost , your final score is {correctAnswer}")
            break

        # reset correctAnswer
        correctAnswer = 0

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


def SetOfQuestions(nbQuestion: int, difficulty: int) -> int:
    """create a set of question , return the number of correct question"""
    nbAnswer: int = 0

    for el in range(nbQuestion):
        correctAnswer = GenerateQuestion(difficulty)
        answer = int(input())
        # check if answer is correct
        if correctAnswer == answer:
            nbAnswer += 1
            print("great, correct answer!")
        else:
            print("wrong!")

    return nbAnswer


main()
