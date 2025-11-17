

def solfeggio (syllable):

    message = (f"The note is {syllable}")
    return(message)

note = input ("Enter note:").lower()

if note == "c":
        syllable = "doh"
        message = solfeggio(syllable)
        print (message)
if note == "d":
        syllable = "re"
        message = solfeggio(syllable)
        print (message)
if note == "e":
        syllable = "mi"
        message = solfeggio(syllable)
        print (message)
if note == "f":
        syllable = "fa"
        message = solfeggio(syllable)
        print (message)
if note == "g":
        syllable = "sol"
        message = solfeggio(syllable)
        print (message)
if note == "a":
        syllable = "la"
        message = solfeggio(syllable)
        print (message)
if note == "b":
        syllable = "si"
        message = solfeggio(syllable)
        print (message)
        
print ("Cheers Pierre!")