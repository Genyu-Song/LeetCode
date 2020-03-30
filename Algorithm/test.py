def helper(n):
    if n == 1: return 1
    money = 1
    cnt = 0
    day = 1
    while day < n:
        cnt += 1
        for i in range(cnt):
            money += 1
            day += 1
            if day == n:
                return money
        money -= 1
        day += 1
    return money

day = int(input())
print(helper(day))