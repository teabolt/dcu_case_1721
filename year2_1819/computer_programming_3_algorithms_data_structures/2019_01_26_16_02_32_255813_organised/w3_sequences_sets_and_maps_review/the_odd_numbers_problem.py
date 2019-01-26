
def get_odd_list():
    odds = []
    num = int(input())
    while num != -1:
        if num % 2 != 0:
            odds.append(num)
        num = int(input())
    return odds