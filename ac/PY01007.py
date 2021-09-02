t = int(input())
for tt in range(t):
    n, x, m = list(map(float, input().split()))
    current_money = n
    year = 0
    while current_money < m:
        current_money += current_money*x/100
        year += 1
    print(year)
