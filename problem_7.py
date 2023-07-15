# draw a pyramid of height n by Vaidas Razgaitis

def pyramid(height):
    # range starts at the 0 index, correct for this with +1
    for row in range(height + 1):
        print(row * '*')

n = input('input the traingle height: ')
pyramid(int(n))