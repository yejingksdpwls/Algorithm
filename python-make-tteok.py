# 떡볶이 떡을 절단기에 넣어 자르려고 한다. 절단기에 높이 H를 지정하면 줄지어진 떡을 한 번에 절단한다.
# 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고 낮은 떡은 잘리지 않는다. 잘린 떡의 길이만큼 손님은 가져가게된다.
# 손님이 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하여라

H, M = map(int, input().split())
tteok = list(map(int, input().split()))

n = 0
length = 0

while True:
    n += 1

    if length >= M:
        print(k)
        break

    length = 0

    k = max(tteok)-n

    for i in tteok:
        if i > k:
            length += i-k