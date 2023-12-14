N, M = map(int, input().split(' '))

S = []

for i in range(N):
    J = list(map(int, input().split(' ')))
    S.append(J)
    
maxx = -1
for i in S:
    if min(i) > maxx: maxx = min(i)
print(maxx)