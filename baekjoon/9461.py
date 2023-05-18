'''
2 = 1 1
3 = 1 2
4 = 1 3
5 = 1 4
7 = 2 5
9 = 2 7
12= 3 9

M[-2] + M[-3] = M[new]
'''
M = [1, 1, 1, 2]

for i in range(1, 100):
    M.append(M[-2]+M[-3])

N = range(int(input()))

for i in N:
    S = int(input())
    print(M[S-1])