A = int(input())
N = []
cnt = 0

for i in range(A):
    M = list(input())
    if i == 0: N = M
    else:
        for j in M:
            if N[cnt] != j: N[cnt] = '?'
            cnt+=1
        cnt = 0
        
print(''.join(N))