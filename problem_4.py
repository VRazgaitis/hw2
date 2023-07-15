# MAX function by Vaidas Razgaitis

def max_of_three(a, b, c):
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    return max_value

# take user inputs
a = input('input a value: ')
b = input('input b value: ')
c = input('input c value: ')

# get max
largest_value = max_of_three(a,b,c)
print(largest_value)