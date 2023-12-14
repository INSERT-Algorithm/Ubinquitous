N, M, K = map(int, input().split(' '))
L = input().split(' ')
S = list(map(int, L))

keep = 0
summ = 0
cnt = 0
for _ in range(M):
  cnt += 1

  if cnt == K:
    keep = max(S)
    S.remove(max(S))
    summ += max(S)
    S.append(keep)
    cnt = 0
    continue
  summ += max(S)
print(summ)
