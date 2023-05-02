N = int(input())

M = []
for i in range(N):
  math, info = map(int, input().split())
  M.append((i+1, math, info))

M.sort(key = lambda i: (-i[1], -i[2], i[0]))

for i in M:
  print(i[0], i[1], i[2])