### [ 문제 ]
함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

--> [ 제한 조건 ]
* x는 -10000000 이상, 10000000 이하인 정수입니다.
* n은 1000 이하인 자연수입니다.

&nbsp;
&nbsp;
&nbsp;
**[ 코드 및 설명 ]**
```python
def solution(x, n): # x, n을 인수로 받는 solution 함수 정의
    answer = [] # 결과로 출력할 리스트 정의
    if -10000000 <= x <= 10000000 and n <= 1000: # 제한 조건에 해당하는 경우에만 함수 실행
        num = 0 # 리스트에 삽입할 값, 후에 x를 더해야 하므로 0으로 초기화
        for i in range(0,n): # x씩 추가되는 과정을 n번 반복
            num = num+x # num 변수에 x씩 증가
            answer.append(num) # 증가한 num 값을 리스트에 추가
    return answer # 리스트 결과값 출력
```

&nbsp;
&nbsp;
**[ 경험적 오류 ]**

1 ) 
```python
answer.append(num)
num = num+x
```
: num은 현재 0으로 초기화했으므로 이대로 실행하면 0부터 리스트에 삽입됨
--> 처음부터 num 값을 x로 초기화했으면 가능한 문장 (개선점)
				&nbsp;

2 )
```python
x += x
answer.append(x)
```
: x 만큼 증가해야 하는데 x 값 자체가 증가하고 있으니 제곱되는 결과가 출력됨
--> 증가하는 값을 다른 변수에 저장해 x 값에는 변화가 없도록 해야함