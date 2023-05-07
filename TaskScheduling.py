import matplotlib.pyplot as plt
import numpy as np
import timeit
import random

def Scheduling(activities):
    selected = [activities[0]]
    j = 0
    for i in range(1,n):
        if activities[i][0] >= activities[j][1]:
            selected.append(activities[i])
            j = i
    return selected

# n = 5
# activities = [[a := random.randint(1, 16), a + random.randint(1,5)] for i in range(n)]
# activities.sort(key=lambda x: x[1])
# print(activities)
# print(Scheduling(activities))

data = np.arange(1, 50)
time = []
for n in data:
  activities = [[a := random.randint(1, 16), a + random.randint(1,5)] for i in range(n)]
  t = timeit.timeit(lambda: Scheduling(activities), number = 100) / 100
  time.append(t)

# Vẽ biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào bằng cách sử dụng thư viện matplotlib
plt.plot(data, time)
plt.xlabel("Dữ liệu đầu vào(n)")
plt.ylabel("Thời gian")
plt.title("Biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào của bài xếp balo")
plt.show()