import numpy as np
def max_sum_non_adjacent(arr):
    n = len(arr)
    S = [0] * n
    for i in range(n):
        max1 = 0
        for j in range(i):
            if S[j] > max1:
                max1 = S[j]
        if arr[i] >= 0:
            S[i] = arr[i] + max1
        else: 
            S[i] = max1

    return max(S)

n = 1000
arr = []
for i in range (n):
    arr.append(np.random.randint(-20,20))
# print(arr)
print(max_sum_non_adjacent(arr))