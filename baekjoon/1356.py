N = input()

key = False
for i in range(1, len(N)):
    S = ''
    V = ''
    
    SS = 1
    VV = 1
    for j in range(i): S += N[j]
    for k in range(i, len(N)): V += N[k]
    for l in S: SS *= int(l)
    for m in V: VV *= int(m)
    
    if SS == VV:
        key = True
        print("YES")
        break
if key == False:
    print("NO")