# N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
# 이 때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.



# 틀 입력받기
N, M = map(int, input().split())

# 얼음틀 형태 입력받기
map_ = []
for i in range(N):
    map_.append(list(map(int, input().split())))

# 얼음 개수 확인 함수
def check(n, m):
    if n <= -1 or n >= N or m <= -1 or m >= M:
        return False
    if map_[n][m] == 0:
        map_[n][m] = 1
        check(n-1, m)
        check(n, m-1)
        check(n+1, m)
        check(n, m+1)
        return True
    return False

result = 0
for i in range(N):
    for j in range(M):
        if check(i,j) == True:
            result += 1

print(result)