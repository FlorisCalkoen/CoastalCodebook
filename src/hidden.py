# This is a test cell that should not be displayed because it has the tag "remove-cell".
#
# @DANIEL: Put your code for the questions here


# you could also consider to put it in if/else with a WrongAnswer exception or something like that?
# or just try to use the nbgrader :-)
# class WrongAnswer(Exception):
#     print("The answer is incorrect. ")

# score = 0
# if ans1 == "A":
#     score += 1
#     print("Answer 1: \t Well done!")
# else:
#     raise WrongAnswer


# TODO: in future use https://github.com/jupyter/nbgrader instead
# Function for cheking the first exercise:
def Check1(ans1, ans2, ans3, ans4, ans5):
    c = 0
    # Checking answer 1:
    if ans1 == "A":
        c = c + 1
        print("Answer 1: \t Well done!")
    if ans1 != "A":
        print("Answer 1: \t Ops! The answer is incorrect.")

    # Checking answer 2:
    if ans2 == "C":
        c = c + 1
        print("Answer 2: \t Well done!")
    if ans2 != "C":
        print("Answer 2: \t Ops! The answer is incorrect.")

    # Checking answer 3:
    if ans3 == "D":
        c = c + 1
        print("Answer 3: \t Well done!")
    if ans3 != "D":
        print("Answer 3: \t Ops! The answer is incorrect.")

    # Checking answer 4:
    if ans4 == "D":
        c = c + 1
        print("Answer 4: \t Well done!")
    if ans4 != "D":
        print("Answer 4: \t Ops! The answer is incorrect.")

    # Checking answer 5:
    if ans5 == "D":
        c = c + 1
        print("Answer 5: \t Well done!")
    if ans5 != "D":
        print("Answer 5: \t Ops! The answer is incorrect.")

    if c == 5:
        print("Nice! You have understood this topic")
    if c == 0:
        print("Mmm... I think you should check the section about this topic again.")


# Function for cheking the second exercise:
def Check2(ans1, ans2, ans3, ans4):
    c = 0
    # Checking answer 1:
    if ans1 == "A":
        c = c + 1
        print("Answer 1: \t Well done!")
    if ans1 != "A":
        print("Answer 1: \t Ops! The answer is incorrect.")

    # Checking answer 2:
    if ans2 == "C":
        c = c + 1
        print("Answer 2: \t Well done!")
    if ans2 != "C":
        print("Answer 2: \t Ops! The answer is incorrect.")

    # Checking answer 3:
    if ans3 == "D":
        c = c + 1
        print("Answer 3: \t Well done!")
    if ans3 != "D":
        print("Answer 3: \t Ops! The answer is incorrect.")

    # Checking answer 4:
    if ans4 == "D":
        c = c + 1
        print("Answer 4: \t Well done!")
    if ans4 != "D":
        print("Answer 4: \t Ops! The answer is incorrect.")

    if c == 4:
        print("Nice! You have understood this topic")
    if c == 0:
        print("Mmm... I think you should check the section about this topic again.")


# Function for cheking the third exercise:
def Check3(ans1, ans2, ans3, ans4):
    c = 0
    # Checking answer 1:
    if ans1 == "A":
        c = c + 1
        print("Answer 1: \t Well done!")
    if ans1 != "A":
        print("Answer 1: \t Ops! The answer is incorrect.")

    # Checking answer 2:
    if ans2 == "C":
        c = c + 1
        print("Answer 2: \t Well done!")
    if ans2 != "C":
        print("Answer 2: \t Ops! The answer is incorrect.")

    # Checking answer 3:
    if ans3 == "D":
        c = c + 1
        print("Answer 3: \t Well done!")
    if ans3 != "D":
        print("Answer 3: \t Ops! The answer is incorrect.")

    # Checking answer 4:
    if ans4 == "D":
        c = c + 1
        print("Answer 4: \t Well done!")
    if ans4 != "D":
        print("Answer 4: \t Ops! The answer is incorrect.")

    if c == 4:
        print("Nice! You have understood this topic")
    if c == 0:
        print("Mmm... I think you should check the section about this topic again.")
