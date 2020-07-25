import string
from random import shuffle

part_lower = list(string.ascii_lowercase)
part_upper = list(string.ascii_uppercase)
part_digit = list(string.digits)
part_punctuation = list(string.punctuation)
try:
    password_length = int(input("Enter the required password length: "))
except Exception:
    print("Enter valid input")

password = []
password.extend(part_lower)
password.extend(part_upper)
password.extend(part_digit)
password.extend(part_punctuation)
shuffle(password)
print("Your password is:",end=" ")
print("".join(password[0:password_length]))
