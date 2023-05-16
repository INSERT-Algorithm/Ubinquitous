N, M = map(int, input().split())

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
weeks = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI','SAT']

for i in range(N-1):M += month[i]

for i in range(1, 8):
    if M%7==i:
        print