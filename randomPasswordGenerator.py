import random
import string 

string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

numChar = int(input("How many characters would you like in your password? "))

#def password():
for num in str(numChar):
    for _ in range(numChar):
        value =  random.randint(0,2)
        if value == 1:
            print (random.randint(0,9))
        else:
            print (random.choice(string.ascii_letters))