import os
import sys
import platform
import time

score = 5 #Setting the starting score

def clear(): #Function for clearing the terminal
    if platform.system == "Windows":
        os.system('cls')
    else:
        os.system('clear')
def input_answer(question, answer): #This is the function where our user will give their answer, then we will check it the answers list
    global score
    user_input = input(f"{question}\n")
    if user_input.lower() in answer:
        print("Nice one! One point!")
        score += 1
        print(score)
        time.sleep(1)
        clear()
    elif user_input.lower() not in answer:
        print("Got it wrong :(")
        score -= 1 
        print(score)
        time.sleep(1)
        clear()

def start(): #Function for stating/explaining the gamein
    clear()
    print("Welcome to the True/False Python Quiz! There are 15 questions and you will start with 5 points, -1 points for each question wrong and +1 for each question right")
    print("So, are you ready? Y/N")
    ready = input("")
    if ready.lower() == "y":
        os.system('clear')
        main()
    elif ready.lower() == "n":
        print("Exiting.....")
        sys.exit()
    else:
        print("Please use Y/N")
        ready = input("")

def main():
    global score
    questions = [ #The questions of the quiz
        "\"==\" is the operator we use to check if something is the same as something else",
        "To output something to console, we would do p(\"Hello World!\")",
        "To add a comment, Python uses #",
        "Variable_x is a valid name in Python (as in it actually runs)",
        "flt() is used to convert a number or a string into an float",
        "To print out the type of object something is, we would use \" print(TypeOf(x))",
        "The extension of Python files is .py",
        "\"func myfunction():\" is used to create a function",
        "x = \"Hello\".char(0) is how you get the first character of a string",
        "trim() is used to remove whitespace at the beginning and the end of a string",
        ".lower() is used to convert a string into all lowercase letters",
        "* is to multiply numbers in Python"
        "== is the same as =",
        "A list [] and a tuple () are different",
        "You cannot start an if/else statement using elif",
    ]
    answers = [ #The answers to the questions
        ["true", "t"],
        ["false", "f"],
        ["true", "t"],
        ["true", "t"],
        ["false", "f"],
        ['false', "f"],
        ['true', "t"],
        ['false', "f"],
        ['false', "f"],
        ["false", "f"],
        ["true", "t"],
        ["true", "t"] ,
        ['false', "f"],
        ['true', "t"],
        ['true', "t"],
    ]
    for i in range(len(questions)):
        input_answer(questions[i], answers[i])
    clear()
    print("You got {}!".format(score))
start()
