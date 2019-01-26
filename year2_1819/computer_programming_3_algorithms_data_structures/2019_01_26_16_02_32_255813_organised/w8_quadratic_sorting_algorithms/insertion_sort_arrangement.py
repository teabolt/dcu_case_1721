
#
#   Return an empty list to get your list of numbers.
#
#   Then return a list of lists corresponding to the passes of an insertion sort on the numbers.
# [10, 15, 6, 14, 4, 19]
# def solution():
#     return [[10,15],
#         [6,10,15],
#         [6,10,14,15],
#         [4,6,10,14,15],
#         [4,6,10,14,15,19]]

# [12, 18, 15, 7, 6, 9]
def solution():
    return [
        [12, 18],
        [12, 15, 18],
        [7, 12, 15, 18],
        [6, 7, 12, 15, 18],
        [6, 7, 9, 12, 15, 18],
        ]