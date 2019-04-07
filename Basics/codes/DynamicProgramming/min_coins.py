def coinChange(coins, amount):
    coins.sort()
    print(coins)
    dp = {0:0}
    for i in range(1,amount+1):
        dp[i] = amount+1
        for j in coins:
            if j <= i:
                dp[i] = min(dp[i-j]+1, dp[i])
                print(dp)
    if dp[amount] == amount+1:
        return -1
    else:
        return dp[amount]


def main():
    coins = [1,3,5]
    amount = 12
    print(coinChange(coins, amount))

if __name__ == '__main__':
    main()