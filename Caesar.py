def letterToIndex():
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '

    strg = input("What is your text: ")
    key = input("What is your shift: ")

    for i in range(0, len(strg) + 1):
        singstrg = strg[i]
        idx = alphabet.find() + key

        if idx > 26:
            idx = idx - 26
        let = ascii_lowercase[idx]


    return let



print(letterToIndex())
