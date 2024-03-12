# 다각형

# N, M = input().split()
# n = int(N)
# m = int(M)
# a = [0] * (n+m)
# max = 0

# for i in range (1, n+1):
#     for j in range (1, m+1):
#         a[i+j] = a[i+j]+1

# for i in range(n+m+1):
#     if a[i] > max:
#         max = a[i]

# for i in range(n+m+1):






# n  = int(input())
# a = []
# for i in range(1, n+1):
#     a.append(i)

# for j in range(1, n+1, i):
#     print(i)





# 가장 큰 수

# ls = []
# n, m = map(int, input().split())
# n_s = str(n)

# for i in n_s:
#   if len(ls) == 0:
#     ls.append(i)
#     continue
#   elif m > 0:
#     while len(ls) > 0 and i > ls[-1] and m > 0:
#       ls.pop()
#       m -= 1
#   ls.append(i)

# if m > 0:
#   ls = ls[:-m]

# print(ls)
# print(m)



# 공주 구하기

# from collections import deque

# q = deque()
# n, k = map(int, input().split())
# K = k
# for i in range(1, n + 1):
#   q.append(i)

# # for _ in range(k-1):
# while len(q) > 1:
#   if K > 1:
#     a = q.popleft()
#     q.append(a)
#     K -= 1
#   elif K == 1:
#     q.popleft()
#     K = k

# print(q)


# 쇠막대기
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())

# ls = list(input())
# p = []
# cnt = 0
# for i in range(len(ls)):
#   if len(p) == 0 or ls[i] == '(':
#     p.append(ls[i])
#   else:
#     p.pop()
#     if ls[i-1] == '(':
#       cnt += len(p)
#     else:
#       cnt += 1

# print(cnt)