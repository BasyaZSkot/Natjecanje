N = int(input())
l = []
for i in range(N):
    a = int(input())
    l.append(a)
M = int(input())

def func(N, l, M):
    summ = 0
    for i in l:
        summ+=i
    a = M-summ

    if summ==N:
        c = 0
    elif abs(a)%2 == 0:
        c = N
    elif summ-N < N*2:
        c = summ-N
    else:
        c = N-abs(a)
        




    return abs(a), c

a, b = func(N, l, M)
print(a, b)


