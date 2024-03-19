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



# 부분집합 구하기

# n = int(input())
# graph = [0] * (n+1)

# def dfs(x):
#   if x == n+1:
#     for i in range(1, n+1):
#       if graph[i] == 1:
#         print(i, end=' ')
#     print()
#     return
#   else:
#     graph[x] = 1
#     dfs(x+1)
#     graph[x] = 0
#     dfs(x+1)

# dfs(1)



# 합이 같은 부분집합

# n = int(input())
# ls = []
# cnt = 0
# graph = [0] * (n)
# for _ in range(n):
#   ls.append(int(input()))

# def dfs(x):
#   s_o = s_z = 0
#   global cnt
#   if x == n:
#     for i in range(n):
#       if graph[i] == 1:
#         s_o += ls[i]
#       else:
#         s_z += ls[i]
#     if s_o == s_z:
#       cnt += 1
#     return
#   else:
#     graph[x] = 1
#     dfs(x+1)
#     graph[x] = 0
#     dfs(x+1)
# dfs(0)

# if cnt > 0:
#   print('YES')
# else:
#   print('NO')


# 바둑이 승차
# c, n = map(int, input().split())
# W = []
# graph = [0] * (n)
# m_w = []
# for _ in range(n):
#   W.append(int(input()))

# def dfs(x):
#   sum = 0
#   if x == n:
#     for i in range(n):
#       if graph[i] == 1:
#         sum += W[i]
#     if sum <= c:
#       m_w.append(sum)
#     return
#   else:
#     graph[x] = 1
#     dfs(x+1)
#     graph[x] = 0
#     dfs(x+1)
# dfs(0)

# print(max(m_w))



# 중복순열
m, n = map(int, input().split())
graph = [0] * n
cnt = 0

def dfs(x):
  global cnt
  if x == n:
    for i in range(n):
      print(graph[i], end=' ')
    print()
    cnt += 1
  else:
    for i in range(1, m+1):
      graph[x] = i
      dfs(x+1)
dfs(0)
print(cnt)
