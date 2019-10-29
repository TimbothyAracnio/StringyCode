# Transpostion Cipher


# encryption function
def scram2Enc(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = evenChars + ch
        charCount = charCount + 1
    cipherTex = oddChars + evenChars
    return cipherTex

def scram2dec(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:] #halflength to the end
    oddChars = cipherText[:halfLength] # 0 to halflength - 1
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + evenChars[i]

