# 개선된 다익스트라 알고리즘

import heapq #우선순위 큐 라이브러리 로드
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
node = [[] for i in range(n+1)]
distance = [INF for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    node[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # 시작 노드로 가기 위한 최단 경로 0으로 설정 후 큐에 삽입
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q) #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        # 현재 노드가 이미 처리된 적 있는 노드면 스킵
        if distance[now] < dist:
            continue
        for i in node[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 우선 순위 큐에 삽입에 다음에 방문할 후보로 선정

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("무한")
    else:
        print(distance[i])