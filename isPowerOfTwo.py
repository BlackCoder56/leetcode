import math
def isPower(n):
    # def getPower(x):
    #     return 2**x
    
    # for i in range(0,n):
    #     square_num = getPower(i)
    #     if n == square_num:
    #         return True
    # return False
    
    if n <= 0:
            return False
    log_n = math.log2(n)
    return log_n.is_integer()


print(isPower(131071))
print(isPower(16))
print(isPower(1))
print(isPower(6))
print(isPower(2))
print(isPower(4))
        