# 2941

cr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

s = input()

for i in cr:
    s = s.replace(i, 'a')
print(len(s))