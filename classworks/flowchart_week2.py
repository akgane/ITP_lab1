def gameStart():
    print("Welcome to the Treasure Island."
          "\nYour mission is to find the treasure island")
    print("You've come to a fork in the road. Which way will you go: right or left?")
    choice = input()
    if choice != "left":
        print("Oh, you fell into a hole. Game over :(")
        return
    else:
        river()


def river():
    print("There's a river in front of you. However, you don't have to swim across it, you can also just wait. Which "
          "will you choose: wait or swim?")
    choice = input()
    if choice != "wait":
        print("You was attacked by trout. Game over")
        return
    else:
        doors()


def doors():
    print("You notice three doors: red, yellow, blue. Which one will you choose?")
    choice = input()
    if choice == "red":
        print("You were burned by fire. Game over")
        return
    elif choice == "blue":
        print("You were eaten by beasts. Game over")
        return
    elif choice == "yellow":
        print("You found treasures! You win!")
        return
    else:
        print("Game over")

gameStart()