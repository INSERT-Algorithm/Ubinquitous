S = range(int(input()))
for i in S:
    N, M = input().split()
    print(bin(int(N, 2) + int(M, 2))[2:])