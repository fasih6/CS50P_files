
import validators
x = input("What's your email address? ")

if validators.email(x):
    print("Valid")
else:
    print("Invalid")