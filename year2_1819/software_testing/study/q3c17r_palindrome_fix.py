# a palindrome is a word that spells the same in both directions
# e.g. eve, madam, civic
def DoSomething():
    reverse=""
    i = 0

    original = input('Enter a string to check if it is a name ')
    length = len(original)
    print('length is ', length, ', string is ', original)

    for i in range(length - 1, -1, -1):
        reverse = reverse + original[i] # fix

    if original == reverse: # fix 
        print('Entered string is a palindrome')
    else:
        print('Entered string is not a palindrome')


DoSomething()