S = [3, 7, 17, 41]

for i in range(3, 100001):
    S.append(((S[-1]+S[-2])+S[-1])%9901)

N = int(input())
print(S[N-1]%9901)