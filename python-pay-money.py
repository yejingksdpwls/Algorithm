# N가지 종류의 화폐들의 개수를 최소한으로 이용해 가치의 합이 M원이 되도록 하려고 한다.
# 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.

N, M = map(int, input().split())

money = []

for i in range(N):
    money.append(int(input()))

d = [10001]*(M+1)

d[0]=0
for i in range(N):
    for j in range(money[i], M+1):
        if d[j-money[i]] != 10001:
            d[j] = min(d[j],d[j-money[i]]+1)

if d[M] == 10001:
    print(-1)
else:
    print(d[M])