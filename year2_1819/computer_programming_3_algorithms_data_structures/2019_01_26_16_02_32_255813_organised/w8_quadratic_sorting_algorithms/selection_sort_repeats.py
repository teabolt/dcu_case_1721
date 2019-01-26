
#
#   Return None to get your list of numbers.
#
#   Then return a tuple of two integers
# [10, 15, 6, 14, 4, 19]
# [4,15,6,14,10.19]
#[4,6,15,14,10,19]
#[4,6,10,14,15,19]
#
#
# def solution():
#     return 10, 2

# list:   [12, 18, 15, 7, 6, 9]
# pass 1: [6, 18, 15, 7, 12, 9] swap 12, 6
# pass 2: [6, 7, 15, 18, 12, 9] swap 18, 7
# pass 3: [6, 7, 9, 18, 12, 15] swap 15, 9
# pass 4: [6, 7, 9, 12, 18, 15] swap 18, 12
# pass 5: [6, 7, 9, 12, 15, 18] swap 18, 15
# top candidates: 18 - 3, 12 - 2, 15 - 2, ...
def solution():
    return 18, 3