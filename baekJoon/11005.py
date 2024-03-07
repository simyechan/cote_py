# 11005

Al = {}
r = ''
for i, j in zip(range(10, 37), range(ord('A'), ord('Z') + 1)):
    Al[i] = chr(j)

N, B = map(int, input().split())

while N != 0:
    b = N % B
    if(b > 9):
        b = Al[b]
    r += str(b)
    N = int(N / B)

print(r[::-1])