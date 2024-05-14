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
# m, n = map(int, input().split())
# graph = [0] * n
# cnt = 0

# def dfs(x):
#   global cnt
#   if x == n:
#     for i in range(n):
#       print(graph[i], end=' ')
#     print()
#     cnt += 1
#   else:
#     for i in range(1, m+1):
#       graph[x] = i
#       dfs(x+1)
# dfs(0)
# print(cnt)


#동전교환
# n = int(input())
# dong_ty = sorted(map(int, input().split()), reverse=True)
# m = int(input())
# r = 0

# for i in dong_ty:
#   r += m // int(i)
#   m = m % int(i)

# print(r)


# 순열 구하기
# N, M = map(int, input().split())

# graph = [0] * N
# v = [False] * (N + 1)
# cnt = 0

# def dfs(x):
#   global cnt
#   if x == M:
#     for i in range(M):
#       print(graph[i], end=' ')
#     print()
#     cnt += 1
#   else:
#     for i in range(1, N + 1):
#       if not v[i]:
#         v[i] = True
#         graph[x] = i
#         dfs(x+1)
#         v[i] = False
# dfs(0)
# print(cnt)


# 수열 추측하기
# ls = []
# N, F = map(int, input().split())
# for i in range(1, N + 1):
#   ls.append(i)

# print(ls)


# 조합 구하기
# N, M = map(int, input().split())
# graph = [0] * N
# v = [0] * (N + 1)
# a = 0
# cnt = 0
# def dfs(x):
#   global cnt, a
#   if x == M:
#     for i in range(M):
#       print(graph[i], end=' ')
#     print()
#     cnt += 1
#   else:
#     for i in range(1, N + 1):
#       if not v[i]:
#         v[i] = True
#         graph[x] = i
#         dfs(x+1)
#         if a < i:
#           a += 1
#           v[i] = False
# dfs(0)
# print(cnt)



#최대점수 구하기(DFS)
# p_l = []
# t_l = []
# m_p = []
# n, m = map(int, input().split())
# graph = [0] * n

# for _ in range(n):
#   p, t = map(int, input().split())
#   p_l.append(p)
#   t_l.append(t)

# def dfs(x):
#   sum_t = 0
#   sum_p = 0
#   if x == n:
#     for i in range(n):
#       if graph[i] == 1 and (sum_t + t_l[i]) <= m:
#         sum_t += t_l[i]
#         sum_p += p_l[i]
#     m_p.append(sum_p)
#     return
#   else:
#     graph[x] = 1
#     dfs(x+1)
#     graph[x] = 0
#     dfs(x+1)
# dfs(0)
# print(max(m_p))


## 휴가
# t_l = []
# p_l = []
# al_s = []
# n = int(input())
# graph = [0] * n
# for _ in range(n):
#   t, p = map(int, input().split())
#   t_l.append(t)
#   p_l.append(p)

# def dfs(x, s):
#   global max_s
#   if x >= n:
#     al_s.append(s)
#     return
#   if x + t_l[x] <= n:
#     dfs(x + t_l[x], s + p_l[x])

#   dfs(x + 1, s)
# dfs(0, 0)
# print(max(al_s))

# 7
# 4 20
# 2 10
# 3 15
# 3 20
# 2 30
# 2 20
# 1 10

# 송아지 찾기(BFS)
# 왜 스카이 콩콩을 타고 송아지를 찾지???
# s, e = map(int, input().split())

# def bfs(a):
#   v = [0] * 10001
#   q = []
#   q.append((a, 0))
#   v[a] = 1
#   while q:
#     b, l = q.pop(0)
#     if b == e:
#       print(l)
#       break
#     for i in (b + 1, b - 1, b + 5):
#       if i < 10001:
#         if v[i] == 0:
#           v[i] = 1
#           q.append((i, l + 1))

# bfs(s)

# 사과나무(BFS)
# arr = []
# n = int(input())
# for _ in range(n):
#   arr.append(list(map(int, input().split())))

# def bfs(arr, x, y):
#   vx = [0] * (len(arr) + 1)
#   vy = [0] * (len(arr) + 1)
#   q = []
#   q.append((x, y, 0))
#   vx[x] = 1
#   vy[y] = 1
#   while q:
#     rx, ry, l = q.pop(0)
#     if l == (n//2 - 1):
#       print(l)
#       break
#     for i in (rx - 1, ry - 1, rx + 1, ry + 1):
#       if vx[i] == 0 and vy[i] == 0:
#         vx[i] = 1
#         vy[i] = 1
#         q.append(i, i, l + 1)
#       if vx[i] == 0:
#         vx[i] = 1
#         q.append(i, ry, l + 1)
#       if vy[i] == 0:
#         vy[i] = 1
#         q.append(rx, i, l + 1)
        
# bfs(arr, (n//2 - 1), (n//2 - 1))


# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19


# 미로의 최단거리 통로(BFS)

# def bfs(g, a):
#   v = [0] * (len(g) + 1)
#   q = []
#   q.append(a)
#   v[a] = 1
#   while q:
#     b = q.pop(0)
#     print(a, end=' ')
#     for i in g[b]:
#       if not v[i]:
#         q.append[i]
#         v = 1


# 이분검색
# l = '9014 20755 19244 15936 15256 4038 32457'
# numbers = list(map(int, l.split()))
# def add_commas(number):
#     return "{:,}".format(number)
# format = [add_commas(number) for number in numbers]
# m = list(map(int, [number.replace(',', '') for number in format]))
# print(m)
# n = 10000
# t = 941

# n, t  = map(int, input().split())
# m = list(map(int, input().split()))
# m.sort()
# m_i = len(m)

# def a(arr, t, s, e):
#   if s > e:
#         return 0
#   ind = (s + e) // 2
  
#   if arr[ind] == t:
#     return ind
#   elif arr[ind] > t:
#     return a(arr, t, s, ind - 1)
#   else:
#     return a(arr, t, ind + 1, e)


# re = a(m, t, 0, n - 1)
# print(re + 1)

# 8 32
# 23 87 65 12 57 32 99 81


# 랜선자르기(결정알고리즘)
# l = []
# k, n = map(int, input().split())
# for _ in range(k):
#   l.append(int(input()))

# def a(arr, s, e):
#   sum = 0
#   if s > e:
#         return e
#   ind = (s + e) // 2
#   for i in arr:
#      sum += i // ind
#   if sum >= n:
#     return a(arr, ind + 1, e)
#   else:
#     return a(arr, s, ind - 1)
  
# print(a(sorted(l), 1, max(l)))


# 뮤직비디오
# n, m = map(int, input().split())
# l = list(map(int, input().split()))
# res = 0

# def bs(arr, s, e, res):
#   a = 0
#   cnt = 1
#   if s > e:
#     return res
#   mid = (s + e) // 2
#   for i in arr:
#     if a + i > mid:
#       cnt += 1
#       a = i
#     else:
#       a += i
#   if cnt <= m and mid >= max(l):
#     return bs(arr, s, mid - 1, mid)
#   else:
#     return bs(arr, mid + 1, e, res)

# print(bs(sorted(l), max(l), sum(l), 0))

# 9 3
# 1 2 3 4 5 6 7 8 9


# 회의실 배정
# n = int(input())
# l = []
# for _ in range(n):
#   l.append(list(map(int, input().split())))

# l.sort(key=lambda x:(x[1], x[0]))

# arr = [l[0][1]]

# for i in range(n):
#   if arr[-1] <= l[i][0]:
#     arr.append(l[i][1])

# print(int(len(arr)))


# 씨름 선수
# n = int(input())
# l = []
# for _ in range(n):
#   l.append(list(map(int, input().split())))
# l.sort(reverse=True)
# arr = [l[0][1]]
# for i in range(n):
#   if arr[-1] < l[i][1]:
#     arr.append(l[i][1])
# print(int(len(arr)))


# 창고 정리
# l = int(input())
# arr = list(map(int, input().split()))
# m = int(input())
# arr.sort()

# for i in range(m):
#   n1 = arr.pop()
#   n2 = arr.pop(0)
#   n1 -= 1
#   n2 += 1
#   arr.append(n1)
#   arr.append(n2)
#   arr.sort()

# print(max(arr) - min(arr))


# 역수열
# n = int(input())
# l = list(map(int, input().split()))
# arr = [0] * n

# for i in range(n):
#   for j in range(n):
#     if l[i] == 0 and arr[j] == 0:
#       arr[j] = i + 1
#       break
#     elif arr[j] == 0:
#       l[i] -= 1
# print(arr)
