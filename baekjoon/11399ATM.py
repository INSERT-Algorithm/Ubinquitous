S = int(input())
N = list(map(int, input().split(' ')))

N.sort()

summ = 0

for i in range(S):
    for j in range(i+1):
        summ += N[j]
print(summ)