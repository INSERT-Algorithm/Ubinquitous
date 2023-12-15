import math

temp = [10, 5, 1]

N, M = map(int, input().split(' '))

finished = abs(N-M)
cnt = 0

# 19일땐 20으로 17일땐 15로

if finished%5 != 0:
        K, L = (finished, finished)
        A, B = (0, 0)
        
        while True:
            if K%5 == 0: break
            else: K-=1
            A += 1
        while True:
            if L%5 == 0: break
            else: L+=1
            B += 1
        if min(A, B) == A:
            finished -= A
            cnt += A
        else:
            finished += B
            cnt += B
while True:
    if finished == 0: break
    cnt += 1
    if finished - 10 >= 0:
        finished -= 10
    else:
        finished -= 5
print(cnt)