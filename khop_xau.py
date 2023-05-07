def khop_xau(T, P):
    n = len(T)
    m = len(P)
    for s in range(n - m + 1):
        if P == T[s:s + m]:
            print(s)

def main():
    T = "xin chao cac ban. Xin chao cac ban"
    P = "ao"
    khop_xau(T,P)

main()
