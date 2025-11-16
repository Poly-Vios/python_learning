answer = input("Would you like me to print a minor scale? (yes/no)").lower()
if answer =="yes":
        notes = ["A","B","C","D","E","F","G"]

        for note in notes:
            print(f"🎵{note}")
      
        print("scale complete!")

else: 
        print("Alright - no scale for you.")