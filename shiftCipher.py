#!/usr/bin/python3
print("     ^", "          ^")
print("    / \ ", "       / \ ")
print("   /   \ ", "     /   \ ")
print("  /     \ ", "   /     \ ")
print(" /       \ ", " /       \ ")
print("___________", "___________")
print("WELCOME TO MIKAH'S SHIFT CIPHER")
print("")
print("")

print("1. Encrypt Text")
print("2. Decrypt Text")

choice = int(input("Select choice: "))

alphabets = ["A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

text = input("Enter text here >>>  ")
text  = text.upper()

K = input("Enter key here >>> ")
result = []

# encrypt  text
def encrypt():
    Y = index
    i = (int(K) + int(Y)) % 26
    result.append(alphabets[i])

# decrypt text
def decrypt():
    Y = index
    i = (int(Y) - int(K)) % 26
    result.append(alphabets[i])

for x in text:
    index = alphabets.index(x)
    if(choice == 1): encrypt()
    else: decrypt()
# convert list to string and print
if(choice == 1): print("The ciphertext is >>" ,  ''.join(result))

# convert list to string and plaintext to lowercase
else: print("The plaintext is >>" ,  ''.join(result).lower())

