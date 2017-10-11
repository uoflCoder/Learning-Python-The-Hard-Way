#Exercise 36

def main():
    print("You enter the pharaoh's tomb...")
    print("There is a relic in the middle of the room what do you do?")
    print("Grab it")
    print("Explore")
    print("Pick up a rock")

    decision = input(">")

    if(decision.upper() == "GRAB IT"):
        booby_trap(1)

    elif(decision.upper() == "EXPLORE"):
        booby_trap(2)

    elif(decision.upper() == "PICK UP A ROCK"):
        pharohs_exit()


    else:
        booby_trap(3)


def booby_trap(case):

    if(case == 1):
        print("You fall into a pit of snakes!")

    elif(case == 2):
        print("A poison dart shoots you in the kneck")

    else:
        print("A huge boulder crushes you")

    exit(0)
def pharaohs_exit():
    print("A room full of gold and silver appears! Congratulations you're richer than Bill Gates!")
    exit(0)

main()
