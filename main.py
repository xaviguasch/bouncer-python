age = input("How old are you? ")

if age:
    age = int(age)
    if age >= 18 and age < 21:
        print("You can enter, but need a wristband")
    elif age >= 21:
        print("You are good to enter and can drink!")
    else:
        print("too young to enter, sorry")
else:
    print("Enter an age!!!!")


