
def count(m, n):
    if n == 0:
        return 0
    if m == 0:
        return 1
    if m < n:
        return count(m,m)
    if m >= n:
        return count(m, n - 1) + count(m - n, n)

print(count(20,5)) 
