import math

pasta = []
juice = []

for i in range(3):
    pasta.append(int(input()))
for i in range(2):
    juice.append(int(input()))
print( round((min(pasta) + min(juice)) * 1.1, 2) )
