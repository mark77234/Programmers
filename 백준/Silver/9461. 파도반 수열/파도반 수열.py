r = int(input())
for i in range(r):
    a = int(input())
    dp = [0] * (a + 1)

    if a < 4:
        print(1)
    elif a == 5:
        print(2)
    else:

        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        for i in range(5, a + 1):
            dp[i] = dp[i - 1] + dp[i - 5]
        print(dp[a])
