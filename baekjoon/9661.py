# 1 : SK
# 2 : CY
# 3 : SK

# 4 : SK | CY

# 5 : CY
# 6 : SK
# 7 : CY

# 8 : CY
# 9 : SK
# 10 : CY
# 11 : SK

# 12 : CY
# 13 : SK
# 14 : SK
# 15 : CY
# 16 : SK | CY

# 17 : CY
# 18 : SK
# 19 : CY
# 20 : CY

# 5마다 분기가 바뀜

N = int(input())

S = ['SK', 'CY']

if N%5==0 or N%5==2: print(S[1])
else: print(S[0])