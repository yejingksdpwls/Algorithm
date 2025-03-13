# 첫째 줄에 맵의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다. (3 <= N, M <= 50)
# 둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A, B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여 주어진다.
# 방향 d의 값으로는 다음과 같이 4가지가 존재한다.
# --------------------------------------------------
# - 0 : 북쪽
# - 1 : 동쪽
# - 2 : 남쪽
# - 3 : 서쪽

# 셋째 줄부터 맵이 육지인지 바다인지에 대한 정보가 주어진다. N개의 줄에 맵의 상태가 북쪽부터 남쪽
# 순서대로, 각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어 있다.
# ---------------------------------------------------
# - 0 : 육지
# - 1 : 바다

# 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
# 첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력하시오.




# N, M 입력
N, M = map(int, input().split())

# A, B, d 입력
A, B, d = map(int, input().split())

# map 입력
map_ = []
for i in range(N):
    map_.append(list(map(int, input().split())))

# 가본 칸 기록 변수 정의
record = []
for i in range(N):
    add = []
    for i in range(M):
        add.append(0)
    record.append(list(add))

# 방향 회전 함수 정의
def turn_left(d):
    if d == 0:
        d = 3
    else:
        d -= 1
    return d

# 이동한 칸의 수 계산
num = 1
turn = 0

while True:
    d = turn_left(d)
    record[A][B] = 1
    
    if d == 0:
        turn += 1
        x = A-1
        y = B
        if map_[x][y] != 1 and record[x][y] == 0:
            num += 1
            turn = 0
            A = x
            B = y
    
    elif d == 1:
        turn += 1
        x = A
        y = B+1
        if map_[x][y] != 1 and record[x][y] == 0:
            num += 1
            turn = 0
            A = x
            B = y
    
    elif d == 2:
        turn += 1
        x = A+1
        y = B
        if map_[x][y] != 1 and record[x][y] == 0:
            num += 1
            turn = 0
            A = x
            B = y
    
    elif d == 3:
        turn += 1
        x = A
        y = B-1
        if map_[x][y] != 1 and record[x][y] == 0:
            num += 1
            turn = 0
            A = x
            B = y

    if turn == 4:
        print(num)
        break