# 2720

alC = [25, 10, 5, 1]
T = int(input())

for _ in range(T):
  C = int(input())
  r = []
  for i in alC:
    c = 0
    c += C // i
    r.append(str(c))
    C %= i
  rstr = ' '.join(r)
  print(rstr)

