# 25206
# 전공평점 = ((학점 * 과목평점) + 전공과목별) / 학점의 총합
# p 과목 제외

# 등급에 따른 과목평점
# A+ = 4.5
# A0 = 4.0
# B+ = 3.5
# B0 = 3.0
# C+ = 2.5
# C0 = 2.0
# D+ = 1.5
# D0 = 1.0
# F = 0.0

r = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
sg = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
gr = 0
allgrade = 0
for i in range(20):
    sub, grade, rating = input().split()
    if(rating == 'P'):
        continue
    grade = float(grade)
    if (rating in r):
        gr += grade * float(sg[r.index(rating)])
    allgrade += grade

print(gr / allgrade)