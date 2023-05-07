import numpy as np
def knapsack_01(values, weights, capacity):
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(capacity, 0, -1):
            if weights[i] <= j:
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

    return dp[capacity]

n = 10
values = []
for i in range (n):
    values.append(np.random.randint(0,100))
weights = []
for i in range (n):
    weights.append(np.random.randint(0,20))
capacity = 100
print(values)
print(weights)
print(knapsack_01(values, weights, capacity))