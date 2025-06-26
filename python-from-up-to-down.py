n = int(input())

array = []
for i in range(n):
    array.append(int(input()))

sort = sorted(array, reverse=True)

for i in sort:
    print(i,end=' ')

# end='\n' (기본값): 출력 후 줄바꿈
# end=' ' : 출력 후 공백으로 이어서 출력
# end='' : 출력 후 아무 것도 붙이지 않음 (완전히 이어서 출력됨)