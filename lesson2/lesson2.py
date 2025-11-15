name = input("What is your name? ")
age = int(input("How old are you? "))

print(f"Welcome, {name}!")

if age < 18:
    print("You are young and full of potential!")
elif age < 40:
    print("You are in a powerful stage of life.")
else:
    print("Your wisdom is your strength.")

