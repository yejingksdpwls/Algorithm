# 다익스트라 알고리즘 기본 구현법

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

distance = [INF for i in range(n+1)] # 최소 거리 리스트 초기화
check = [False for i in range(n+1)] # 방문 기록 리스트 초기화
node = [[] for i in range(n+1)] # 노드 간선 연결 정보 리스트 초기화

for _ in range(m): # 반복을 위한 것으로 _ 기호 사용
    a, b, c = map(int, input().split()) # a: 출발지, b: 도착지, c: 간선 길이
    node[a].append((a,b)) # append는 하나의 값만 넣을 수 있어서 튜플로 묶어서 넣어줌

def find_short():
    min = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min and not check[i]:
            min = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0 # 시작 노드에 대해 초기화
    check[start] = True

    for j in node[start]:
        distance[j[0]] = j[1]

    for j in range(n-1):
        now = find_short()
        check[now] = True

        for i in node[now]:
            cost = distance[now] + i[1]
        
            if cost < distance[i[0]]:
                distance[i[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print('무한')
    else:
        print(distance[i])