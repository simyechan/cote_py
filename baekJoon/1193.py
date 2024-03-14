# 1193

l = 1
x = int(input())

while x > l:
  x -= l
  l += 1

if l % 2 == 0:
  print(x, '/', l-x+1, sep='')
else:
  print(l-x+1, '/', x, sep='')