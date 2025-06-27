n = int(input())

score = {}

for i in range(n):
    namee, scoree = str(input()).split()
    score[namee] = scoree

sort = sorted(score)

for i in sort:
    print(i, end=' ')