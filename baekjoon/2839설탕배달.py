N = int(input())

P = [3, 5]
current = 0
cnt = 0

if (N-3)%5 == 0:
    N -= 3
    cnt += 1
    cnt += N//5
    print(cnt)
elif N%5 == 0:
    cnt += N//5
    print(cnt)
else:
    while True:
        if N <= 0 or current == 2: break
        
        if N - P[current] < 0:
            current = 2
            break
        N -= P[current]
        cnt += 1
        
        if N%5 == 0:
            current = 1
    if current == 2: print(-1)
    else: print(cnt)