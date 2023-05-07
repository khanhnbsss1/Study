import matplotlib.pyplot as plt
import numpy as np
import timeit
# kiểm tra nguyên tố
def primes(n):
    if ( n < 2) :
        return False
    if (n == 2):
        return True
    else:
        for i in range(2,n):
            if (n % i == 0 ):
                return False
    return True

# phan tich thanh thua so
def phan_tich(term):
    if (term < 2):
        return [term]
    if ( primes(term) ):
        return [term]
    else:
        for i in range(2, term //2 + 1):
            if (term % i == 0):
                return [i] + list(phan_tich(term // i))

# for a in range(0,20):
#     print(phan_tich(a))
# print(phan_tich(54145))

data = np.arange(1, 1001)
time = []
for n in data:
  # Lặp lại 10 lần và lấy trung bình để giảm sai số
  t = timeit.timeit(lambda: phan_tich(n), number = 10) / 10
  time.append(t)

# Vẽ biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào bằng cách sử dụng thư viện matplotlib
plt.plot(data, time)
plt.xlabel("Dữ liệu đầu vào(n)")
plt.ylabel("Thời gian")
plt.title("Biểu đồ sự phụ thuộc của thời gian vào dữ liệu đầu vào của bài in ra thừa số nguyên tố")
plt.show()