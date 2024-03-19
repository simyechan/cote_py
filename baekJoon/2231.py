# 2231

n = int(input())
ls = []

for i in range(n):
  s = i + sum(map(int, str(i)))
  if s == n:
    print(i)
    ls.append(i)
    break
if len(ls) < 1:
  print(0)