# Temperature converter program by Vaidas Razgaitis.

temperature_input = input('Enter a temperature in Fahrenheit: ')

if temperature_input[0] == '-':
    # the number is negative, or at least a string that begins with -
    print('Please enter a positive, whole number numeric temperature.')
elif temperature_input.isdigit():
    # user input is a positive whole number as required 
    temp_f = int(temperature_input)
    temp_c = round((temp_f - 32) / 1.8, 2)
    print(f'The temperature is {temp_c} in Celsius.')
else:
    # user input is a string with values that aren't digits 
    print('Please enter a positive, whole number numeric temperature.')