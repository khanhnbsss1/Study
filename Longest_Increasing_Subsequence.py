import numpy as np
def lis(arr):
    n = len(arr)
    dp = [0] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],dp[j]+1)

    result = [float('inf')] * (max(dp)+1)
    maximum = max(dp)
    for i in range(n-1,-1,-1):
        if dp[i] == maximum:
            result[maximum] = arr[i]
            maximum = maximum - 1
    return result

arr = []
n = 10
for i in range (n):
    arr.append(np.random.randint(-20,20))
print(arr)
print(lis(arr))