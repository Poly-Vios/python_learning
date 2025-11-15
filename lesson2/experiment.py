name = input("What is your name, musician? ")
age = int(input("How old are you? "))

instrument = input("What is your favorite instrument to play? ")
years_playing = int(input(f"How many years have you played the {instrument}? "))

print()
print(f"🎵 Welcome, {name}! 🎵")
print(f"You love playing the {instrument}.")

if years_playing < 2:
    print("You are just beginning your musical journey — enjoy every moment!")
elif years_playing < 10:
    print("You are growing into your sound beautifully.")
else:
    print("Your mastery and dedication shine through every note.")

print()

if age < 18:
    print("You carry youthful fire — let it inspire your music!")
elif age < 40:
    print("You are in a powerful stage of artistic expression.")
else:
    print("Your life experience enriches your music with depth and wisdom.")

print("\nKeep creating, keep playing, keep resonating. 🎶")