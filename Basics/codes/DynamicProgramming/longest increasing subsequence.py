def LIS(seq):
    dp = {0:0}
    for i in range(1, len(seq)):
        print(seq[i])
        dp[i]=0
        for j in range(0,i):
            if seq[j] <= seq[i]:
                dp[i] = max(dp[j]+1, 1)
                print(dp)
    return dp[len(seq)-1]


def main():
    seq = [5,3,8,16,7,9,11]
    dp = LIS(seq)
    print(dp)


if __name__ == '__main__':
    main()