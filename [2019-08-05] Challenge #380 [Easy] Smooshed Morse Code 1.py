morseCode = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morseLetters = morseCode.split()
latinLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
morseDict = {}
for i in range(0,26):
    morseDict[latinLetters[i]]=morseLetters[i]

def smorse(word):
    return ''.join([morseDict[letter] for letter in word])
