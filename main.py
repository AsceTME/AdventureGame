def introScene():
    directions = ["Forward", "Left", "Right"]
    print("you are in a dimly lit tunnel, you can choose the direction to go in. Where would you like to go ? ")
    print("choose your direction")
    userInput = input()
    if userInput == "Left":
        showShadowFigure()
    elif userInput == "right":
        showSlime()
    elif userInput:

    else:
        print("Try again.")
nput == "forward":
        trapRoom()
    elif userInput == "backward":
        print("You find the closed entrance duh -side eye-")"forward":
        trapRoom()
if __name__ == "__main__":

  while True:
        print("Welcome to your next adventure")
        print("As a pennyless wanderer, you decide to search a newly found dungeon")
        print("You walk into the dungeon and suddenly you hear..... ")
        print("CRASH!!!! The entrance shuts closed")
        print("BUT BEFORE ALL THAT WHAT IS YOUR NAME!:")
        name = input()
        print("Good luck, " + name + ".")
        introScene()

def introScene

        def showShadowFigure():
            directions = ["right", "backward"]
            print("You see a dark figure in the distance. You feel watched. Where would you like to go? ")
            userInput = ""
            while userInput not in directions:
                print("Options : right/left/backward")
                userInput = input()
                if userInput == "right":
                    cameraScene()
                elif userInput == "left":
                    print("you walk into a wall.")
                elif userInput == "backward":
                    introScene()
                else:
                    print("how about we try a different  route")

        def cameraScene():
            directions = ["forward", "backward"]
            print("You see a giant camera on the ceiling. Strange because you dont know what a camera is. Where do "
                  "you want to go?")
            userInput = ""
            while userInput not in directions:
                print("Options: forward/backward")
                userInput = input()
                if userInput == input("forward"):
                    print("You made it out alive!!")
                    quit()
                elif userInput == "backward":
                    showShadowFigure()
                else:
                    print("How about you try again")
        def trapRoom():
            directions = ["right" , "left" , "backward"]
            print("You walk right into the trap room. The skeletons have awoken. Where would you like to go?")
            userInput = ""
            while userInput not in directions:
                print("Options: right/left/backward")
                userInput = ""
                if userInput == "right":
                    print("Multiple skeletons attack you. You are gravely wounded and die.")
                    quit()
                elif userInput == "left":
                    print("You survived! You have found a exit ,be free with your skeleton attached.")
                    quit()
                elif userInput == "backward":
                    introScene()
                else:
                    print("How about you try again")

        def showSlime():
            directions = ["backward", "forward"]
            global weapon
            print("You come face to face with a giant slime wall ass you walk. Where do you go ? ")
            userInput = input()
            if userInput == "left":
                print("You find a chest inside of the wall. You open the chest to find a water gun ")
                weapon = True
            elif userInput == "backward":
                introScene()
            elif userInput == "forward":
                strangeCreature()
            else:
                print("How about you try again?")

        def strangeCreature():
            actions = ["fight", "flee"]
            global weapon
            print("A giant egg shaped monster appears. You can either run or be a warrior and fight. What do you do?")
            userInput = ""
            if userInput == "fight":
                if weapon:
                    print("You kill the monster with the water gun you found earlier. After moving forward you find "
                          "the exit. Congrats! ")
                else:
                    print("the egg-like creature has killed you.")
                quit()
            elif userInput == "flee":
             showSlime()
            else:
                print("how about you try again")
