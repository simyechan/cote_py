# 1978

r = 0
num = int(input())
ls =list(map(int, input().split()))
for i in ls:
  cnt = 0
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        cnt += 1
    if cnt == 0:
      r += 1
print(r)