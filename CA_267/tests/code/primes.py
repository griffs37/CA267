def is_prime(number):
#funtion goes here
    for element in range(2,number):
         if number % element == 0:
              print(number)
              print("NOT PRIME")
              return False
    print(number)
    print("PRIME")
    return True


