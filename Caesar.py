def letterToIndex(letter, key):
    from string import ascii_lowercase
    alphabet = ascii_lowercase + ' '

    for i in range(0, len(letter) + 1):
        idx = alphabet.find(letter) + key


        if idx > 26:
            idx = idx - 26



    let = ascii_lowercase[idx]


    return let



print(letterToIndex("y", 4))
