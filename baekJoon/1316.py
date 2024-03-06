# 1316

a = int(input())
cnt = a
for _ in range(a):
    s = input()
    for i in range(len(s) - 1):
        if (s[i] == s[i+1]):
            continue
        elif (s[i] in s[i+1:]):
            cnt -= 1
            break
print(cnt)
