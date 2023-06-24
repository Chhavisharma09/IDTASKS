import random
cnumber= random.randrange(1,100)
userInput =int(input("Emter a Number:----"))
if userInput>cnumber:
    print("computer Number",cnumber)          
    print("Your guess number is too high")
elif cnumber>userInput:
    print("computer Number",cnumber)
    print("Your guess number is too low")
else:
    print("computer Number",cnumber)
    print("Your guess number is equal")


