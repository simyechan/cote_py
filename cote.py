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

# T = int(input())

# for _ in range(T):
#   ls = list((input()))
#   a = []
#   for i in ls:
#     if (i == '('):
#       a.append(i)
#     elif (len(a) > 0 and a[-1] == '('):
#       a.pop()
#     else:
#       a.append(i)
#   if (len(a) == 0):
#     print('YES')
#   else:
#     print('NO')



# 카드
# n = int(input())
# ls = []

# for i in range(1, n+1):
#   ls.append(i)

# while len(ls) > 1:
#   ls.pop(0)
#   ls.append(ls.pop(0))

# print(ls)



# 후위 표기식2
# c = []
# num = []
# n = []
# n1 = n2 = 0
# n = int(input())

# ar = input()
# for i in ar:
#   c.append(i)

# for _ in range(n):
#   num.append(int(input()))

# for i in c:
#   if i == '*':
#     n2 = num.pop()
#     n1 = num.pop()
#     num.append(n1 * n2)
#   elif i == '/':
#     n2 = num.pop()
#     n1 = num.pop()
#     num.append(n1 / n2)
#   elif i == '+':
#     n2 = num.pop()
#     n1 = num.pop()
#     num.append(n1 + n2)
#   elif i == '-':
#     n2 = num.pop()
#     n1 = num.pop()
#     num.append(n1 - n2)
#   else:
#     print(num[c.index(i)])

# print(num)

# 5
# ABC*+DE/-
# 1
# 2
# 3
# 4
# 5

# 6.20