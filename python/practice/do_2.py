N = int(input())
coins = {}
for number in range(N):
    coin = int(input())
    if coin in coins:
        coins[coin] += 1
    else:
        coins[coin] = 1
for number, frequency in sorted(coins.items()):
    print(f"{number} {frequency}")
