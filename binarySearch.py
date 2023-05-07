import matplotlib.pyplot as plt
import numpy as np
import timeit

def binary(n):
  if n == 0:
    return "0"
  elif n == 1:
    return "1"
  else:
    return binary(n // 2) + str(n % 2)

#binarynumber = str[::-1]
data = np.arange(1, 1001)
time = []
for n in data:
  # Lặp lại 10 lần và lấy trung bình để giảm sai số
  t = timeit.timeit(lambda: binary(n), number = 10) / 10
  time.append(t)

# Vẽ biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào bằng cách sử dụng thư viện matplotlib
plt.plot(data, time)
plt.xlabel("Dữ liệu đầu vào(n)")
plt.ylabel("Thời gian")
plt.title("Biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào của bài in ra số nhị phân")
plt.show()
