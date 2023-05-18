N = input()
M = []
for i in N: M.append(int(i))
M.sort()
M.reverse()

for j in M: print(j, end='')