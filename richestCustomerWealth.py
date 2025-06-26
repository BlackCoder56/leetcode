accounts = [[2,8,7],[7,1,3],[1,9,5]]
maxWealth = 0
for account in accounts:
    currentWealth = 0
    for j in account:
        currentWealth += j

    maxWealth = max(maxWealth, currentWealth)

print(maxWealth)