n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)

for i in range(n+1):
    if sum(coins[:i]) > sum(coins[i:]):
        print(i)
        break
