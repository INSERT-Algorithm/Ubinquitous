x, y = (1, 1)
maxx = int(input())

order_list = list(input().split(' '))

for order in order_list:
    if order == 'U' and y > 1:
        y -= 1
    if order == 'R' and x < maxx:
        x += 1
    if order == 'D' and y < maxx:
        y += 1
    if order == 'L' and x > 1:
        x -= 1
print(y, x)