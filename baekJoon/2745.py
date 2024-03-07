# 2745

Al = {}
r = 0
for i, j in zip(range(ord('A'), ord('Z') + 1), range(10, 37)):
    Al[chr(i)] = j

N, B = input().split()
B = int(B)

for i in range(len(N)):
    if ('A' <= N[i] <= 'Z'):
        r += int(Al[N[i]]) * (B ** (len(N) - 1 - i))
    else:
        r += int(N[i]) * (B ** (len(N) - 1 - i))
print(r)