def level(years):
    if years < 2:
        return "a beginner"
    elif years < 10:
        return "an intermediate musician"
    else: 
        return "an advanced musician"

name = input("What is your name? ")
instrument = input("What instrument do you play? ")
years = int(input(f"How many years have you played the {instrument}?"))

musician_level = level(years)
print(f"You are {musician_level}.")

print(f"{name}, you have played the {instrument} for {years} years. You are {musician_level}.")
print(f"The {instrument} sings through your hands, {name}. Never stop creating. 🎼")

scale_yes_no = input("Would you like me to print a minor scale? (yes/no) ").lower()
if scale_yes_no == "yes":
    notes = ["A", "B", "C", "D", "E", "F", "G"]
    for note in notes:
        print(f"🎵 {note}")
    
    print("Scale complete!")
    
elif scale_yes_no == "no":
        print("No scale for you!")



   