# Palindrome checker by Vaidas Razgaitis

# parse input to remove spaces
test_string = input('Enter a word or phrase: ').replace(' ','')
reversed_string = test_string[::-1]

print('This is a palindrome.') if test_string == reversed_string else print('This is NOT a palindrome.')

