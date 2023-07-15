""" 
Passwored strength checker by Vaidas Razgaitis

REQUIREMENTS:
    1. 12 character min
    2. Contains both numbers and letters
    3. Contains at least one special character: !,@,#,$,%
    4. Contains at least one capital and one lowercase letter
"""

password = input('enter a password: ')

# CONDITION 1
valid_length = True if len(password) >= 12 else False

# CONDITION 2
contains_letters_and_numbers = True if not (password.isalpha() or password.isdigit()) else False

# CONDITION 3
contains_special_character = True if '!' in password or '@' in password or '#' in password or '$' in password or '%' in password else False

# scan password for uppercase and lowercase letters
contains_lower = False
contains_upper = False
contains_capital_and_lower = False
for character in password:
    if character.islower():
        contains_lower = True
    if character.isupper():
        contains_upper = True
    if contains_upper and contains_lower:
        # CONDITION 4
        contains_capital_and_lower = True
        break

# DEBUGGING CHECKS
# print(f'valid length: {valid_length}')
# print(f'valid numbers and letters: {contains_letters_and_numbers}')
# print(f'special chars: {contains_special_character}')
# print(f'capital and lower case letters: {contains_capital_and_lower}')

if (valid_length and 
    contains_letters_and_numbers and 
    contains_special_character and 
    contains_capital_and_lower):
    print('This is a strong password :)')
else:
    print('This is not a strong password :(')


    

