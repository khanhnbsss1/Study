import matplotlib.pyplot as plt
import numpy as np
import timeit
import random
from copy import deepcopy

def MergeFile1(arr): #cach xep thong thuong
    temp = []
    temp.append(arr[0])
    for i in range(1,n):
       temp.append(arr[i]+temp[i-1])
    result = sum(temp) - arr[0]
    return result

def MergeFlie2(arr): #xep theo tung cap
    result = 0
    while len(arr)>1:
        n = len(arr)
        for i in range(n//2):
            arr[i] = arr[i] + arr[i+1]
            result = result + arr[i]
            arr.remove(arr[i+1])
    return result
            
def MergeFile3(arr): #sap xep roi cong file
    arr.sort()
    return MergeFile1(arr)

# n = 6
# data = [15,10,100,60,20,30]
# print(data)
# data1 = deepcopy(data)
# print(MergeFile1(data1))
# data1 = deepcopy(data)
# print(MergeFlie2(data1))
# data1 = deepcopy(data)
# data1.sort()
# print(MergeFile3(data1))

data = np.arange(1, 10000)
time1 = []
time2 = []
time3 = []
for n in data:
  File = [np.random.randint(0,100) for i in range(n)]
  file1 = deepcopy(File)
  time1.append(MergeFile1(file1))
  file1 = deepcopy(File)
  time2.append(MergeFlie2(file1))
  file1 = deepcopy(File)
  time3.append(MergeFile3(file1))

# Vẽ biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào bằng cách sử dụng thư viện matplotlib
plt.plot(data, time1,label = "Cach 1")
plt.plot(data, time2,label = "Cach 2")
plt.plot(data, time3,label = "Cach 3")

plt.xlabel("Dữ liệu đầu vào(n)")
plt.ylabel("Số bước ")
plt.title("Biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào của bài Merge File theo 3 cách")
plt.legend()
plt.show()