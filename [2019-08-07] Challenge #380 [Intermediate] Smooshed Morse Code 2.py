morseCode = ".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
morseLetters = morseCode.split()
latinLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
morseDict = {}
for i in range(0,26):
    print 'morse(\''+str(latinLetters[i])+'\',\''+str(morseLetters[i])+'\').'

def smalpha(smorse):
    if smorse == "":
        return ''
    if smorse[0:2] in morseDict:
        return morseDict[smorse[0:2]]+smalpha(smorse[2:])
    if smorse[0:2] in morseDict:
        return morseDict[smorse[0:2]]+smalpha(smorse[2:])

