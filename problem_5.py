# divisible by 11 by Vaidas Razgaitis

def divisibility(n):
    running_sum = 0
    i_value = 0
    for digit in n:
        running_sum = (running_sum + int(digit)) if i_value % 2 == 0 else (running_sum - int(digit))
        i_value += 1
    print('This is divisible by 11.') if running_sum % 11 == 0 else print('This is NOT divisible by 11.')

input_number = input('Enter a number: ')
divisibility(input_number)
