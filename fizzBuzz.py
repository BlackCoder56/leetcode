answer = []
for i in range(1, 6):
    divisibleBy3 = i % 3 == 0
    divisibleBy5 = i % 5 == 0

    currentString = ""

    if(divisibleBy3):
        currentString += "Fizz"
    
    if(divisibleBy5):
        currentString += "Buzz"
    
    if(len(currentString) == 0):
        currentString = f"{i}"
    
    answer.append(currentString)

print(answer)