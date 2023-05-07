import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

def knapSack(W, wt, val, n):
  
    if n == 0 or W == 0 :
        return 0
  
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
  
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))

  
# val = [80, 100, 120]
# wt = [10, 20, 30]
# W = 50
# n = len(val)
# print(knapSack(W, wt, val, n))


data = np.arange(1, 20)
time = []
for W in data:
  val = [random.randint(1,100) for i in range(W)]
  wt = [random.randint(1,100) for i in range(W)]
  W = random.randint(1,100) * W
  n = len(val)
  t = timeit.timeit(lambda: knapSack(W, wt, val, n), number = 10) / 10
  time.append(t)

# Vẽ biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào bằng cách sử dụng thư viện matplotlib
plt.plot(data, time)
plt.xlabel("Dữ liệu đầu vào(n)")
plt.ylabel("Thời gian")
plt.title("Biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào của bài xếp balo")
plt.show()