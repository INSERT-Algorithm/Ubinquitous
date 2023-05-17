M = []

for i in range(1, 21):
    F = 1
    for j in range(2, i): F*=j
    M.append(F)

N = int(input())

if N == 0: print('NO')

for k in range(19, -1, -1):
    if N >= M[k]: N -= M[k]
print('YES') if N == 0 else print('NO')