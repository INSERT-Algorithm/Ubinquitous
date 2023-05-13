S = input()
K = S
cnt = 0

while 1:
    if K == '1':
        cnt = 60
        break
    if len(K) == 1:
        K = '0' + K
    N = str(int(K[0]) + int(K[1]))
    K = K[-1] + N[-1]
    cnt += 1
    
    if K == S: break
print(cnt)