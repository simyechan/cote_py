# 1158

ls = []
step = 0
r = []
N, K = map(int, input().split())

for i in range(1, N + 1):
  ls.append(i)

for i in range(N):
  step = (step + K - 1) % len(ls)
  r.append(str(ls.pop(step)))

str = ', '.join(r)

print('<' + str + '>')