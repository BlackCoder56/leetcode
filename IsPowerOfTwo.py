class CheckingPower:
    def isPowerOfTwo(n):
        def getPower(x):
            return 2**x
        y = n
        
        if n == 1:
            p = 2**0
            if p == n:
                return True
        else:            
            while y % 2 == 0:
                m = y/2
                y = m
                for i in range(int(m)+1):
                    square_num = getPower(i)
                    
                    if n == square_num:
                        return True
            return False
        
        
print(CheckingPower.isPowerOfTwo(3))
print(CheckingPower.isPowerOfTwo(131071))
print(CheckingPower.isPowerOfTwo(16))
print(CheckingPower.isPowerOfTwo(1))
print(CheckingPower.isPowerOfTwo(4))
print(CheckingPower.isPowerOfTwo(6))