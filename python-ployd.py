# 플로이드 워셜 알고리즘

INF = int(1e9)

n, m = map(int, input().split())
distance = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    distance[a][b] = c

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            distance[j][k] = min(distance[j][k], distance[j][i]+distance[i][k])

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == INF:
            print("무한", end=" ")
        else:
            print(distance[i][j], end=" ")
    print()