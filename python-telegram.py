# N개의 도시는 보내고자 하는 메시지가 있는 경우, 다른 도시로 전보를 보내 다른 도시로 메시지를 전송할 수 있다.
# 하지만 X에서 Y로 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다.
# Y에서 X로 통하는 통로가 있더라도, X에서 Y로의 통로가 없다면 X에서 Y로 전보를 보낼 수 없다.
# 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
# 어느 날 C라는 도시에서 위급 상황이 발생해 최대한 많은 도시로 메시지를 보내고자 한다. 
# 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게되는 도시의 개수는
# 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

N, M, C = map(int, input().split())

graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

num = 0
time = 0

for i in range(1, N+1):
    if graph[C][i] != INF and graph[C][i] != 0:
        num += 1
        if graph[C][i] > time:
            time = graph[C][i]

print(num, time)
 
