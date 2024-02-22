def isSimilar():
    x = [1,2,3]
    y = [1,2,3]
    
    while len(x) == len(y):
        for i in x:
            while i not in y:
                return False
        return True
    return False


# Print result on terminal
print("\n",isSimilar(),"\n")
        