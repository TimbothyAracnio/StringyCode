# Strings

# We will be talking about Concatenation
#    2 or more strings put'n them together

firstName = "Doug"
lastName = "Dimmadome"

# stick'n them together
print(firstName + " " + lastName)

# this works!
name = firstName + " " + lastName
lastFirst = lastName + ", " + firstName

print(lastFirst)

# Repetition

print("Duck, " * 2 + "Goose!")

def rowYourBoat():
    print("Chug, " * 15 + "*INHALE* your boat")
    print("Harshly up the waterfall,")
    print("Strenuously. " * 8)
    print("life stinks.")

rowYourBoat()



# Indexing: you can pick it apart

name = "Charlie"
firstChar = name[0]
print(firstChar)

middleCharIndex = len(name) // 2
print(middleCharIndex)
print(name[middleCharIndex])
print(name[-1])

# cool thing repeats
for i in range(0, len(name)):
    print(name[i])

print("-----------------")

# Slicing and dicing

# gets numbers
print(name[0:6])

for i in range(0, len(name) + 1):
    print(name[0:i])


# Oh, and one more thing
# Searching, is a new game that we[Apple] are releasing

print("Charly" in name)
if "y" not in name:
    print("H is not in name")
else:
    print("H is in name")