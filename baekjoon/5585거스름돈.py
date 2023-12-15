N = 1000 - int(input())

money = [500, 100, 50, 10, 5, 1]

current = 0
cnt = 0

while True:
    if N == 0: break

    if N - money[current] >= 0:
        cnt += 1
        N -= money[current]
    else:
        current += 1

print(cnt)