import random

numbers = "1234567890"
upper = "qazwsxedcrfvtgbyhnujmikolp"
lower = "ZAQXSWEDCRFVTGBYHNUJMIKOLP"
symbols = "!@#$^&*()/"

length = int(input("Input password length: "))

string = numbers + upper + lower + symbols

print("Your password is: ", end="")
for i in range (length):
    print(random.choice(string),end="")
input()