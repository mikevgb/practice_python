# Write a password generator in Python. Be creative with how you generate 
# passwords - strong passwords have a mix of lowercase letters, uppercase 
# letters, numbers, and symbols. The passwords should be random, generating 
# a new password every time the user asks for a new password. Include your 
# run-time code in a main method.

# Extra:

# Ask the user how strong they want their password to be. For weak passwords,
# pick a word or two from a list.

import string
import random

up = string.ascii_uppercase
low = string.ascii_lowercase
num = string.digits
sym = string.punctuation

r_num = random.choice(num)
r_up = random.choice(up)
r_low = random.choice(low)
r_sym = random.choice(sym)

combined = r_up + r_low + r_num + r_sym

print(combined)
