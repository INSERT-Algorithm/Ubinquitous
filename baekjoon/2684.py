N = int(input())

case = [
    "TTT",
    "TTH",
    "THT",
    "THH",
    "HTT",
    "HTH",
    "HHT",
    "HHH",
]

F = []

for i in range(N):
    S = input()
    
    M = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(2, len(S)):
        cnt = 0
        for j in case:
            if S[i-2] + S[i-1] + S[i] == j: M[cnt] += 1
            cnt+=1
    F.append(M)

for i in F:
    for j in i: print(j, end=' ')
    print()