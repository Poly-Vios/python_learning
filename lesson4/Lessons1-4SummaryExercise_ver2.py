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
def print_scale():
    notes = ["A", "B", "C", "D", "E", "F", "G"]
    for note in notes:
        print(f"🎵 {note}")
    print("Scale complete!")

def no_scale():
    print("Alright, no scale will be printed.")

if scale_yes_no == "yes":
    print_scale()
   
else:
    no_scale()



   