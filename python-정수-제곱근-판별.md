### [ 문제 설명 ]
임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
&nbsp;
&nbsp;
### [ 코드 및 설명 ]
```python
import math 								# 제곱근 함수를 위한 패키지 불러오기
def solution(n):
    answer = 0
    if math.sqrt(n) == int(math.sqrt(n)):	# int로 변환한 값이 실제 제곱근 값과 동일한 경우
        answer = (math.sqrt(n)+1)**2
    else: 									# 아닌 경우
        answer = -1
    return answer
```