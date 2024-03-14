# 2292

cnt = 1
add = 0
weight = 0
n = int(input())

while n - 1 > weight:
  add += 6
  weight += add
  cnt += 1

print(cnt)

