N, K = map(int, input().split())

A = list(map(int, input().split(',')))

S = []
for i in range(K):
    for i in range(len(A)):
        if i != len(A) - 1: S.append(A[i+1] - A[i])
    A = S
    S = []

for i in range(len(A)):
    if i != len(A) - 1: print(A[i], end=',')
    else: print(A[i])
