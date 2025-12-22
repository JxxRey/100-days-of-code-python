print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("How old are you?"))
    if age <= 12:
        print("$5 for child")
        bill = 5
    elif age <= 18:
        print("$7 for youth")
        bill = 7
    else:
        print("$12 for adult")
        bill = 12
    include_photo = (input("Do you also want photos? Y for yes N for no "))
    if include_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry you have to grow taller before you can ride.")
