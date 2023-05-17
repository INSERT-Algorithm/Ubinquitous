N = list(map(lambda x: x, range(1, int(input())+1)))

M = []
while len(N) != 1:
    M.append(N[0])
    N.remove(N[0])
    S = N[0]
    N.remove(N[0])
    N.append(S)

for i in M: print(i, end=' ')
print(N[0])