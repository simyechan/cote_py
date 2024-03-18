# 요세푸스

# ls = []
# step = 0
# r = []
# N, K = map(int, input().split())

# for i in range(1, N + 1):
#   ls.append(i)

# for i in range(N):
#   step = (step + K - 1) % len(ls)
#   r.append(ls.pop(step))

# print(r)


# 괄호

T = int(input())

for _ in range(T):
  ls = list((input()))
  a = []
  for i in ls:
    if (i == '('):
      a.append(i)
    elif (len(a) > 0 and a[-1] == '('):
      a.pop()
    else:
      a.append(i)
  if (len(a) == 0):
    print('YES')
  else:
    print('NO')