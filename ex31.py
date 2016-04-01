print("only input shoul;d be integers. keep in mind or you get errors")
print("You enter a dark room with two doors. Do you go with door #1 or door #2")

door = int(input("> "))

if door == 1:
    print("There is gaint bear eating a cheege cake. What do you do ?")
    print("1. take the cake")
    print("2. Scream at bear")

    bear = int(input("> "))
    if bear == 1:
        print("well bear eat your face off. Good job!")
    elif bear == 2:
        print("bear eats your leg off. Good job!")
    else:
        print("well doing %s is probably better. Run away" % bear)

elif door == 2:
    print("You stare into the endless abss at cthutlu's retina")
    print("1. Blueberries")
    print("2. Yellow jacket clothespin")
    print("3. Understanding revolver standing memories")
    insanity = input("> ")
    if insanity == 1 or insanity == 2:
        print("Your body survided powerd by mind of jello. Good job")
    else:
        print("The insanity rot your eyes into pool of muck. Good job")

else:
    print("You stunmble around and fall on a knife and die")

