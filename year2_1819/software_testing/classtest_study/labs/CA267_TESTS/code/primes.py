def is_prime(number):
#funtion goes here
    for element in range(2,number):
         if number % element == 1:
              print(number)
              print("NOT PRIME")
              return False
    print(number)
    print("PRIME")
    return False

x=int(input("enter:"))
is_prime(x)


