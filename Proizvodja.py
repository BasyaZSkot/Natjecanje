_A = int(input())
_B = int(input())
_C = int(input())
X = int(input())
Y = int(input())
Z = int(input())

def func(_A, _B, _C, X, Y, Z):
    _summ = []
    summ = 0
    A = _A
    B = _B
    C = _C
    
    b = min(A//212, B//97, C//15)
    summ += b*X
    A -= b*212
    B -= b*97
    C -= b*15
    
    b = min(A//307, B//76, C//40)
    summ += b*Y
    A -= b*307
    B -= b*76
    C -= b*40

    b = min(A//100, B//60, C//55)
    summ += b*Z
    A -= b*100
    B -= b*60
    C -= b*55

    _summ.append(summ)
    summ = 0
    A = _A
    B = _B
    C = _C

    b = min(A//212, B//97, C//15)
    summ += b*X
    A -= b*212
    B -= b*97
    C -= b*15

    b = min(A//100, B//60, C//55)
    summ += b*Z
    A -= b*100
    B -= b*60
    C -= b*55
    
    b = min(A//307, B//76, C//40)
    summ += b*Y
    A -= b*307
    B -= b*76
    C -= b*40

    _summ.append(summ)

    summ = 0
    A = _A
    B = _B
    C = _C

    
    b = min(A//307, B//76, C//40)
    summ += b*Y
    A -= b*307
    B -= b*76
    C -= b*40

    b = min(A//212, B//97, C//15)
    summ += b*X
    A -= b*212
    B -= b*97
    C -= b*15

    b = min(A//100, B//60, C//55)
    summ += b*Z
    A -= b*100
    B -= b*60
    C -= b*55

    _summ.append(summ)

    summ = 0
    A = _A
    B = _B
    C = _C

    b = min(A//100, B//60, C//55)
    summ += b*Z
    A -= b*100
    B -= b*60
    C -= b*55

    b = min(A//307, B//76, C//40)
    summ += b*Y
    A -= b*307
    B -= b*76
    C -= b*40

    b = min(A//212, B//97, C//15)
    summ += b*X
    A -= b*212
    B -= b*97
    C -= b*15

    _summ.append(summ)

    summ = 0
    A = _A
    B = _B
    C = _C

    b = min(A//100, B//60, C//55)
    summ += b*Z
    A -= b*100
    B -= b*60
    C -= b*55

    b = min(A//212, B//97, C//15)
    summ += b*X
    A -= b*212
    B -= b*97
    C -= b*15

    b = min(A//307, B//76, C//40)
    summ += b*Y
    A -= b*307
    B -= b*76
    C -= b*40

    _summ.append(summ)

    return max(_summ)
    


    # a = max(X, Y, Z)
    # if a == X:
    #     b = min(A//212, B//97, C//15)
    #     print(b)
    #     summ += b*X
    #     A -= b*212
    #     B -= b*97
    #     C -= b*15
    #     if Y>Z:
    #         b = min(A//212, B//97, C//15)
    #         print(b)
    #         summ += b*Y
    #         A -= b*212
    #         B -= b*97
    #         C -= b*15

    #         b = min(A//100, B//60, C//55)
    #         print(b)
    #         summ += b*Z
    #         A -= b*100
    #         B -= b*60
    #         C -= b*55

    #     else:
    #         b = min(A//100, B//60, C//55)
    #         print(b)
    #         summ += b*Z
    #         A -= b*100
    #         B -= b*60
    #         C -= b*55

    #         b = min(A//212, B//97, C//15)
    #         print(b)
    #         summ += b*Y
    #         A -= b*212
    #         B -= b*97
    #         C -= b*15
            
    # elif a == Y:
    #     b = min(A//307, B//76, C//40)
    #     print(b)
    #     summ += b*Y
    #     A -= b*307
    #     B -= b*76
    #     C -= b*40

    #     if X>Z:
    #         b = min(A//212, B//97, C//15)
    #         print(b)
    #         summ += b*X
    #         A -= b*212
    #         B -= b*97
    #         C -= b*15
    #         b = min(A//100, B//60, C//55)
    #         print(b)
    #         summ += b*Z
    #         A -= b*100
    #         B -= b*60
    #         C -= b*55
    #     else:
    #         b = min(A//100, B//60, C//55)
    #         print(b)
    #         summ += b*Z
    #         A -= b*100
    #         B -= b*60
    #         C -= b*55
    #         b = min(A//212, B//97, C//15)
    #         print(b)
    #         summ += b*X
    #         A -= b*212
    #         B -= b*97
    #         C -= b*15
    # else:
    #     b = min(A//100, B//60, C//55)
    #     print(b)
    #     summ += b*Z
    #     A -= b*100
    #     B -= b*60
    #     C -= b*55
    #     if X>Y:
    #         b = min(A//212, B//97, C//15)
    #         print(b)
    #         summ += b*X
    #         A -= b*212
    #         B -= b*97
    #         C -= b*15
    #         b = min(A//307, B//76, C//40)
    #         print(b)
    #         summ += b*Y
    #         A -= b*307
    #         B -= b*76
    #         C -= b*40
    #     else:
    #         b = min(A//307, B//76, C//40)
    #         print(b)
    #         summ += b*Y
    #         A -= b*307
    #         B -= b*76
    #         C -= b*40
    #         b = min(A//212, B//97, C//15)
    #         print(b)
    #         summ += b*X
    #         A -= b*212
    #         B -= b*97
    #         C -= b*15

    # print(A, B, C)
    return summ
    

print(func(_A, _B, _C, X, Y, Z))