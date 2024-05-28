import sys
al = { 'A' : 3, 'B' : 2, 'C' : 1, 'D' : 2, 'E' : 3, 'F' : 3, 'G' : 2, 'H' : 3, 'I' : 3, 'J' : 2, 'K' : 2, 'L' : 1, 'M' : 2, 'N' : 2, 'O' : 1, 'P' : 2, 'Q' : 2, 'R' : 2, 'S' : 1, 'T' : 2, 'U' : 1, 'V' : 1, 'W' : 1, 'X' : 2, 'Y' : 2, 'Z' : 1}
a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()
sum = []
for i in range(len(a)):
    sum.append(al[a[i]])
    sum.append(al[b[i]])
while len(sum) > 2:
  sum_temp = []
  for i in range(len(sum) - 1):
    sum_temp.append((sum[i] + sum[i + 1]) % 10)
  sum = sum_temp
print(str(sum[0]) + str(sum[1]))
