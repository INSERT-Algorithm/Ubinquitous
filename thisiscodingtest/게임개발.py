N, M = map(int, input().split(' '))
Y, X, direction = map(int, input().split(' '))

S = []
for i in range(M):
    F = list(map(int, input().split(' ')))
    S.append(F)
    
def turn_left(direction):
    if direction == 0:
        return 3
    return direction - 1
    
def move_left(X, Y, direction):
    # 북쪽
    if direction == 0:
        return (X - 1, Y)
    # 동쪽
    if direction == 1:
        return (X, Y - 1)
    # 남쪽
    if direction == 2:
        return (X + 1, Y)
    # 서쪽
    if direction == 3:
        return (X, Y + 1)
        
def move_back(X, Y, direction):
    # 북쪽
    if direction == 0:
        return (X, Y - 1)
    # 동쪽
    if direction == 1:
        return (X + 1, Y)
    # 남쪽
    if direction == 2:
        return (X, Y + 1)
    # 서쪽
    if direction == 3:
        return (X - 1, Y)
    
def is_full(X, Y):
    fuller_counter = 0
    fuller = [ S[X][Y+1], S[X+1][Y], S[X][Y-1], S[X-1][Y] ]
    for full in fuller:
        if full == 1 or full == 9:
            fuller_counter += 1
    if fuller_counter == 4: return True
    return False

while True:
    S[X][Y] = 9
    
    if is_full(X, Y):
        sX, sY = move_back(X, Y, direction)
        
        if S[sX][sY] == 9:
            X, Y = sX, sY
        break
    
    dX, dY = move_left(X, Y, direction)
    direction = turn_left(direction)
    
    if S[dX][dY] == 0:
        X, Y = dX, dY
        
cnt = 0
for i in S:
    for j in i:
        if j == 9: cnt += 1
print(cnt)