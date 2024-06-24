# #마구간 정하기(결정알고리즘)
# def cnt(arr, m):
#   n = 0
#   count = 0
#   while n < max(arr):
#     for i in arr:
#       if n <= i < n + m:
#         count += 1
#         break
#     n += m
#   return count
  
# n, c = map(int, input().split())
# l = []
# m1 = 0
# for i in range(n):
#   l.append(int(input()))
# l.sort()

# def a(arr, s, e):
#   global m1
#   mid = (s + e) // 2
#   if s >= e:
#     return m1
#   if cnt(arr, mid) >= c:
#     m1 = mid
#     return a(arr, mid + 1, e)
#   else:
#     m1 = mid
#     return a(arr, s, mid - 1)
  
# print(a(l, l[0], l[-1]))


#침몰하는 타이타닉(그리디)
# n, m = map(int, input().split())
# l = list(map(int, input().split()))
# cnt = 0
# l.sort(reverse=True)
# while len(l) > 1:
#   if l[0] + l[-1] > m:
#     l.pop(0)
#     cnt += 1
#   else:
#     l.pop(0)
#     l.pop(-1)
#     cnt += 1
# if len(l) > 0:
#   cnt += 1
# print(cnt)


#증가수열 만들기(그리디)
# cnt = 0
# s = []
# n = int(input())
# l = list(map(int, input().split()))
# if l[0] < l[-1]:
#     p = l[0]
#     l.pop(0)
#     s.append('L')
# else:
#     p = l.pop(-1)
#     s.append('R')
# while 1:
#   cnt += 1
#   if p < l[0] and p < l[-1]:
#     if l[0] < l[-1]:
#       p = l.pop(0)
#       s.append('L')
#     else:
#       p = l.pop(-1)
#       s.append('R')
#   elif p < l[0]:
#     p = l.pop(0)
#     s.append('L')
#   elif p < l[-1]:
#     p = l.pop(-1)
#     s.append('R')
#   else:
#      break
# print(cnt)
# print(s)