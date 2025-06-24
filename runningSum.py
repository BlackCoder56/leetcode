nums = [1,1,1,1,1]
runningSumList = []
total = 0

for num in nums:
    total += num
    runningSumList.append(total)

print(runningSumList)