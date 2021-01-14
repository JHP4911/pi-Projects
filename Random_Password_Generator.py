'''
Create a program that takes the length of the password and generates a random password of the same length.
'''
import random
passlen = int(input("Enter the length of password"))
s = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRST!@#$%^&*(){}?[]'
p = "".join(random.sample(s,passlen))
print(p)