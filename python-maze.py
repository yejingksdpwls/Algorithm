# N * M 크기의 직사각형 형태의 미로에 갇혀있다. 미로에는 여러 마리의 괴물이 있어
# 이를 피해 탈출해야 한다. 나의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며
# 한 번에 한 칸씩 이동할 수 있다. 이 때 괴물이 있는 부분은 0으로, 괴물이 없는 부분은 1로 표시되어
# 있다. 미로는 반드시 탈출할 수 있는 형태로 제시된다. 이 때 내가 탈출하기 위해 움직여야 하는 최소
# 칸의 개수를 구하시오. 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산한다.



# 칸 수 입력받기
N, M = map(int, input().split())

# 미로 입력받기
maze = []
for i in range(N):
    maze.append(list(map(int, input())))

# 이동 칸 개수 계산하기
result = 0
def move(n, m):
    global result
    if maze[n][m] != 1:
        return 0
    else:
        if n == N-1 and m == M-1:
            result += 1
            return 1
        if m < M-1:
            move(n, m+1)
            if result:
                result += 1
        if n < N-1:
            if move(n+1, m):
                result += 1
    return result
    
# 결과 확인
print(move(0,0))