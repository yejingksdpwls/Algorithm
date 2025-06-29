# 부품이 N개 있고, 각 부품의 정수 형태의 고유한 번호가 있다. 
# 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성하시오.

def find_part(find, list, start, end):
    if start > end:
        return print('no', end=' ') 

    mid = (start+end) // 2

    if list[mid] == find:
        return print('yes', end=' ')
    
    elif list[mid] > find:
        return find_part(find, list, start, mid-1)

    elif list[mid] < find:
        return find_part(find, list, mid+1, end)


N = int(input())
store = sorted(list(map(int, input().split())))

n = int(input())
find = list(map(int, input().split()))

for i in find:
    find_part(i, store, 0, N-1)