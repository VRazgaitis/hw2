# Score calculation program by Vaidas Razgaitis.

test_score = input('Enter a score: ')

if test_score.isdigit():
    score = int(test_score)
    if score < 0 or score > 100:
        print('This in not a valid input.')
    # return the proper grade if the score is in the correct range
    elif score >= 90:
        print('You received an A!')
    elif score >= 80:
        print('You received a B')
    elif score >= 70:
        print('You received a C')
    elif score >= 60:
        print('You received a D')
    else:
        print('You received an F')
else:
    # user input is a string with values that aren't digits 
    print('This is not a valid input.')
