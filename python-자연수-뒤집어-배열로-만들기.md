### [ 문제 ]
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

--> **[ 제한 조건 ]**
n은 10,000,000,000이하인 자연수입니다.

&nbsp;
&nbsp;
**[ 코드 및 설명]**
```python
def solution(n):
    answer = []
    str_n = str(n) # int로 받은 n을 문자열로 변환
    if n <= 10000000000: # 제한조건
        for i in range(0,len(str_n)): # n의 자릿수만큼 반복
            answer.append(int(str_n[len(str_n)-i-1])) # 뒤집어 배열해야 하므로 n의 자릿수에서 순서-1을 뺀 값으로 인덱싱
            # 리스트에 삽입할 때는 정수 값이어야 하므로 다시 int로 변환
    return answer
```
&nbsp;
&nbsp;
**[ 경험적 오류 및 반성 ]**
1 )
```python
for i in range(len(str_n),0):
	answer.append(int(str_n[i]))
```
: i 값 감소하면서 진행하려면 range(len(str_n), 0, -1) 으로 -1씩 줄어든다는 것을 명시해야함
	&nbsp;

2 )
```python
for i in range(0, len(str_n)):
	answer.append(n[len(str)-i-1]))
```
: 정수 값은 자릿수 별 인덱싱이 불가능함
--> str로 변환 후 int로 변환함
&nbsp;
&nbsp;
*더 효율적인 코드* )

```python
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
```
: reversed 함수를 사용해 문자열인 n을 뒤집고, map 함수를 통해 다시 int로 변환함