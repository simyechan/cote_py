# 1157

al = input().upper()
all = list(set(al))
ar = []


for i in all:
    ar.append(al.count(i))

if(ar.count(max(ar)) > 1):
    print('?')
else:
    print(all[ar.index(max(ar))])