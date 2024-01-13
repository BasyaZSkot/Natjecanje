A = int(input())
B = int(input())
C = int(input())
D = int(input())

def func(A, B, C, D):
    l = [A, B, C, D]
    if l[0]*l[1]==l[2]+l[3]:
        return f'{l[0]}*{l[1]}={l[2]}+{l[3]}'
    elif l[0]*l[2]==l[1]+l[3]:
        return f'{l[0]}*{l[2]}={l[1]}+{l[3]}'
    elif l[0]*l[3]==l[2]+l[1]:
        return f'{l[0]}*{l[3]}={l[2]}+{l[1]}'
    elif l[1]*l[2]==l[0]+l[3]:
        return f'{l[1]}*{l[2]}={l[0]}+{l[3]}'
    elif l[1]*l[3]==l[0]+l[2]:
        return f'{l[1]}*{l[3]}={l[0]}+{l[2]}'
    elif l[2]*l[3]==l[0]+l[1]:
        return f'{l[2]}*{l[3]}={l[0]}+{l[1]}'
    
    max_numb = max(A, B, C, D)
    l.remove(max_numb)
    if l[0]*l[1]+l[2]==max_numb:
        return f'{l[0]}*{l[1]}+{l[2]}={max_numb}'
    elif l[0]*l[2]+l[1]==max_numb:
        return f'{l[0]}*{l[2]}+{l[1]}={max_numb}'
    elif l[1]*l[2]+l[0]==max_numb:
        return f'{l[1]}*{l[2]}+{l[0]}={max_numb}'


    
    

a = func(A, B, C, D)
print(a)