# 미래 도시에는 1번부터 N번까지의 회사가 있는데 특정 회사끼리는 서로 도로를 통해
# 연결되어 있다. 특정 회사에 도착하기 위한 방법은 회사끼리 연결되어 있는 도로를 이용하는 방법이 유일하고,
# 또한 연결된 2개의 회사는 양방향으로 이동할 수 있다. 각 도로를 이동하는 시간은 정확히 1만큼의
# 시간으로 이동할 수 있다. A는 현재 1번 회사에 위치해 있으며, K번 회사를 방문한 뒤 X번 회사로 가는 것이
# 목표다. 이 때 A가 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오.

INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    graph[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1, K+1):
    for i in range(1, K+1):
        for j in range(1, K+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print(-1)
else:
    print(distance)