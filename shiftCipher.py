#!/usr/bin/python3

# import urlparse
# url = "https://megxos.home.blog"
# parsed_query = urlparse.urlparse(url).query
# print ("urlparse.parse_qs(parsed_query")

# num = input("Enter value here >>> ")
# while num != "q":
#     ans = int(num) % 26
#     print("The solution of ", num , "% 26 = ", ans )
#     num = input("Enter value here >>> ")

def welcome():
    print("     ^", "          ^")
    print("    / \ ", "       / \ ")
    print("   /   \ ", "     /   \ ")
    print("  /     \ ", "   /     \ ")
    print(" /       \ ", " /       \ ")
    print("___________", "___________")
    print("WELCOME TO MIKAH'S SHIFT CIPHER")
    print("")
    print("")

welcome()
def encrypt():
    Y = corrNum
    y = (int(K) +int(Y)) % 26
    print(y)
    ciphertext.append(alphabets[y])

def decrypt():
    Y = corrNum
    y = (int(Y) - 26) +int(K)
    print(y)
    ciphertext.append(alphabets[y])

alphabets = ["A","B",'C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#index = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
word = input("Enter plaintext here >>>  ")
K = input("Enter key here >>> ")
word  = word.upper()
ciphertext = []

for x in word:
    corrNum = alphabets.index(x)
    encrypt()
print("The ciphertext is >>" ,  ciphertext)

