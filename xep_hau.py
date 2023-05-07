def xep_hau(count):
    for i in range(n):
        if kiem_tra(i,count):
            ban_co[i][count] = 1
            count = count + 1
            if count == 8: 
                for h in range(n):
                    for k in range(n):
                        if ban_co[h][k] == 1:
                            print(h," ",k)
                print()
                return
            else: xep_hau(count)
            count = count - 1
            ban_co[i][count] = 0


def kiem_tra(row,col):
    #kiem tra hang ngang
    for i in range(n):
        if ban_co[row][i] == 1: return False 
    #kiem tra duong cheo trai
    t = (row - col)
    for i in range(n):
        if i + t <= 7 and i + t >= 0:
            if ban_co[i+t][i] == 1: return False
    #kiem tra duong cheo phai
    t = (row + col)
    for i in range(n):
        if t - i <= 7 and t - i >= 0:
            if ban_co[t - i][i] == 1: return False
    return True

n = 8
count = 0
ban_co = [[0 for i in range(n)] for j in range(8)] 
xep_hau(count)
