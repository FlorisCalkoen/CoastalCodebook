# TODO: in future use https://github.com/jupyter/nbgrader instead
# Function for cheking the first exercise:
def Check1(ans1, ans2, ans3, ans4, ans5):
    c = 0
    # Checking answer 1:
    if ans1 == "A":
        c = c + 1
        print(
            "Answer 1: \t Correct! The channel velocity is too small to keep the inlet open. Sedimentation leads to closure of the inlet."
        )
    if ans1 == "B":
        print("Answer 1: \t Are you sure that point B is a stable point?")
    if (ans1 == "C") & (ans1 == "D"):
        print(
            "Answer 1: \t Is it possible for a tidal inlet to naturally pass point B from location 1?"
        )
    if ans1 == "E":
        print(
            "Answer1: \t Wow! Talking about over compensation... I suggest you rethink your answer"
        )

    # Checking answer 2:
    if ans2 == "D":
        c = c + 1
        print(
            "Answer 2: \t Correct! Although we are close to point B, an unstable equilibrium, the channel velocity is large enough to increase the channel cross-section. It grows towards point C, passes it, and eventually reach point D, a stable equilibrium."
        )
    if ans2 == "C":
        print(
            "Answer 2: \t Almost! The cross-section grows towards point C, but does it stop there?"
        )
    if (ans2 != "D") & (ans2 != "C"):
        print(
            'Answer 2: \t Location 2 lies between an unstable equilibrium (point B) and stable equilbrium (point D). The unstable equilibrium "pushes" away and the stable equilibrium "attracts". It can\'t really go anywhere else but...?'
        )

    # Checking answer 3:
    if ans3 == "D":
        c = c + 1
        print(
            "Answer 3: \t Correct! The channel velocity is still too large. Through erosion the channel moves to point D."
        )
    if ans3 == "C":
        print(
            "Answer 3: \t Almost! The channel velocity is larger than the equilibrium velocity. The channel is eroding, thus moving towards?"
        )
    if (ans3 != "D") & (ans3 != "C"):
        print(
            'Answer 3: \t Location 3 lies between an unstable equilibrium (point B) and stable equilbrium (point D). The unstable equilibrium "pushes" away and the stable equilibrium "attracts". It can\'t really go anywhere else but...?'
        )

    # Checking answer 4:
    if ans4 == "D":
        c = c + 1
        print(
            "Answer 4: \t Correct! The channel velocity is too small and the cross-section too large. Sedimentation occurs and we move towards point D"
        )
    if (ans4 == "C") | (ans4 == "B"):
        print("Answer 4: \t Hmmm, are you sure we can move past point D?")
    if ans4 == "A":
        print("Answer 4: \t Oh no! Where are you going, come back!")
    if ans4 == "E":
        print(
            "Answer 4: \t A channel cross-section that is actually too large will grow even more. Are you sure about that?"
        )

    # Checking answer 5:
    if ans5 == "D":
        c = c + 1
        print(
            "Answer 5: \t Correct! The cross-section will grow until an equilibrium is found."
        )
    if ans5 == "E":
        print(
            "Answer 5: \t A channel cross-section that is actually too large will grow even more. Are you sure about that?"
        )
    if (ans5 != "D") & (ans5 != "E"):
        print("Answer 5: \t Hmmm, are you sure we can move past point D?")
    if ans5 == "A":
        print("Answer 4: \t Oh no! Where are you going, come back!")

    if c == 5:
        print(
            "Well done! You are a master of understanding the Escoffier curve. But what about other scenarios? Go to Part 2 and find out."
        )
    if c == 0:
        print(
            "Mmm... I think you should read the section about this topic again. If you can't figure it out, discuss with your peers or ask us for help."
        )
    if (c > 0) & (c < 5):
        print(
            "Some of your answers are incorrect. Retrhink your answers or dicuss with your peers what the correct answers should be."
        )


# Function for cheking the second exercise:
def Check2(ansII_1, ansII_2, ansII_3, ansIII_1, ansIII_2, ansIII_3):
    c = 0
    # Checking scenario II answer 1:
    if ansII_1 == "A":
        c = c + 1
        print("Answer II_1: \t Correct!")
    if ansII_1 == "C":
        print(
            "Answer II_1: \t Point C does coincide with the equilibrium velocity, but is this a stable situtaion?"
        )
    if ansII_1 == "E":
        print(
            "Answer II_1: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )

    # Checking scenario II answer 2:
    if ansII_2 == "A":
        c = c + 1
        print("Answer II_2: \t Correct!")
    if ansII_1 == "C":
        print(
            'Answer II_2: \t Definitely possible, as long as the deviation is "to the right". As soon as a deviation is "to the left", what happens?'
        )
    if ansII_1 == "E":
        print(
            "Answer II_2: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )

    # Checking scenario II answer 3:
    if ansII_3 == "A":
        c = c + 1
        print("Answer II_3: \t Correct!")
    if ansII_1 == "C":
        print(
            "Answer II_3: \t The situation will approach point C, but how likely is it that no overshoot occurs?"
        )
    if ansII_1 == "E":
        print(
            "Answer II_3: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )

    # Checking scenario III answer 1:
    if ansIII_1 == "A":
        c = c + 1
        print("Answer III_1: \t Correct!")
    if ansIII_1 == "C":
        print(
            "Answer III_1: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )
    if ansIII_1 == "E":
        print(
            "Answer III_1: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )

    # Checking scenario III answer 2:
    if ansIII_2 == "A":
        c = c + 1
        print("Answer III_2: \t Correct!")
    if ansIII_2 == "C":
        print(
            "Answer III_2: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )
    if ansIII_2 == "E":
        print(
            "Answer III_2: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )

    # Checking scenario III answer 3:
    if ansIII_3 == "A":
        c = c + 1
        print("Answer III_3: \t Correct!")
    if ansIII_3 == "C":
        print(
            "Answer III_3: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )
    if ansIII_3 == "E":
        print(
            "Answer III_3: \t Are you sure? Look back at the previous exercise and reconsider what happens."
        )

    if c == 6:
        print(
            "Well done! Your understanding of the possible scenarios is very good. Now we are going to test you some more, go to the next exercise."
        )
    if c == 0:
        print(
            "Mmm... I think you should go through the theory and this notebook again."
        )
    if (c > 0) & (c < 6):
        print(
            "Some of your answers are incorrect. Retrhink your answers or dicuss with your peers what the correct answers should be."
        )


# Function for cheking the third exercise:
def Check3():
    print(
        "Question 1: \t If the cross-section gets really large, there is a point where the estuary/basin starts to act more as a normal coastline."
    )
    print(
        "Question 2: \t A cross-sectional (area) going to inifity does not really have a physical meaning."
    )
    print(
        "Question 3: \t Modifying the Escoffier curve means modifying the tidal prism, see the equation in this notebook. You can change the tidal prism in many ways. A possbility is damming the estuary, as is done with the Zuiderzee (now IJsselmeer) in The Netherlands. Another option is to dredge and/or reclaim land, altering the storage capacity of the estuary. "
    )
    print(
        "Question 4: \t Ofcourse! Estuaries constantly change due to changes in sediment import/export and fluvial discharges. As long as the estuary is not in a steady equilibrium, the tidal prism can vary in time, and thus the closure curve."
    )
