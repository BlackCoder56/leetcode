def isHappyNumber(n):
  
    def sum_of_digits(number):
        return sum(int(i)**2 for i in str(number))
    
    seen_number = set()
    while n != 1 and n not in seen_number:
        seen_number.add(n)
        n = sum_of_digits(n)
    return n == 1


print(isHappyNumber(2))     # Output: False
print(isHappyNumber(19))    # Output: True
print(isHappyNumber(7))     # Output: True
    