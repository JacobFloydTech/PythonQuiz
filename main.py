import os
import sys
import platform
import time

score = 5 #Setting the starting score


def typing(string): #Fancy typing go brrrrrr
  for char in string:
    sys.stdout.write(char)
    sys.stdout.flush() 
    time.sleep(0.10)

def user_ready(): #I made this a function instead of just having it as an if statement so I could loop the third (else) condition back to the function
    ready = input("")
    if ready.lower() == 'y':
        main()
    elif ready.lower() == 'n':
        print("Exiting", end="", flush=True)
        typing("......\n")
        sys.exit()
    else:
        print("Please use y/n")
        time.sleep(0.5)
        user_ready()

def start(): #Function for stating/explaining the game 
    os.system('clear')
    print("Welcome to the True/False Python Quiz! There are 15 questions and you will start with 5 points, -1 points for each question wrong and +1 for each question right")
    print("So, are you ready? Y/N")
    user_ready()


def input_answer(question, answer): #This is the function where our user will give their answer, then we will check it the answers list
    global score
    user_input = input(f"{question}\n")
    if user_input.lower() in answer: #Error fixed: Was using .upper()ste instead of lower()
        print("Nice one! One point!")
        score += 1
        print(score, "points!")
        time.sleep(1.2)
        os.system('clear')
    elif user_input.lower() not in answer and user_input.lower() != "f" or "false":
        print("Please enter true, false, t, or f")
        time.sleep(0.5)
        user_input = input(f"{question}\n")
        print(score, 'points!')
        time.sleep(0.5)
        os.system('clear')
    elif user_input.lower() not in answer:
        print("Got it wrong :(")
        score -= 1 
        print(score, "points!")
        time.sleep(1.2)
        os.system('clear')

def main():
    os.system('clear')
    global score
    questions = [ #The questions of the quiz
        "\"==\" is the operator we use to check if something is the same as something else",
        "To output something to console, we would do p(\"Hello World!\")",
        "To add a comment, Python uses #",
        "Variable_x is a valid name in Python (as in it actually runs)",
        "flt() is used to convert a number or a string into an float",
        "To print out the type of object something is, we would use \"print(TypeOf(x))\"",
        "The extension of Python files is .py",
        "\"func myfunction():\" is used to create a function",
        "x = \"Hello\".char(0) is how you get the first character of a string",
        "trim() is used to remove whitespace at the beginning and the end of a string",
        ".lower() is used to convert a string into all lowercase letters",
        "* is to multiply numbers in Python",
        "== is the same as =",
        "A list [] and a tuple () are different",
        "You cannot start an if/else statement using elif",
    ]
    answers = [ #The answers to the questions
        ["true", "t"], #Decided to do lists within lists, so if people do t OR true, it will accept both as it's checking all the strings in each one
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
    for i in range(len(questions)): #range(len()) counts up how many questions they are
        print("Question {}:".format(i+1))
        input_answer(questions[i], answers[i]) #Then the loop runs my input_answer function for each number, from 0-15, running through each question 
    os.system('clear')
    print("You got {}! \nDo you want to play again? Y/N".format(score))  #Error fixed: Was using % instead of .format() for {}
    user_ready()
start() #Starting the game
