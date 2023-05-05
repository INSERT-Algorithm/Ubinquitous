while(1):
    N = input()
    if N == '0':
        break
    if N[::-1] == N:
        print('yes')
    else:
        print('no')