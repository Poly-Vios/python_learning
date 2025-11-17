def describe_instrument(instrument, years):
    print (f"You play the {instrument}.")

    if years < 2:
        return "You're just beginning your musical journey!"
    elif years < 10: 
        return "Your sound is developing beautifully."
    else:
        return "Your Mastery shows inceredible dedication."

name = input("What is your name? ")
instrument = input("What is your favorite instrument? ")
years = int(input(f"How many years have you played the {instrument}?"))

print()
print(f"🎶Hello {name}!🎶")
message = describe_instrument(instrument, years)
print(message)
print("Keep creating and expressing your unique voice!🎶")
