# 2745

Al = {}
r = 0
for i, j in zip(range(ord('A'), ord('Z') + 1), range(10, 37)):
    Al[chr(i)] = j

N, B = input().split()
B = int(B)

if ('A' <= N <= 'Z'):
    for i in range(len(N) - 1, -1, -1):
        r += int(Al[N[len(N)-1 - i]]) * (B ** i)

else:
    for i in range(len(N) - 1, -1, -1):
        r += int(N[len(N)-1 - i]) * (B ** i)
print(r)