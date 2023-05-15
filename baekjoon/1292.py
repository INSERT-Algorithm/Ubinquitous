S = []
N, M = map(int, input().split())
for i in range(1, 80):
    for j in range(0, i): S.append(i)
summ = 0
for k in range(N-1, M): summ += S[k]
print(summ)