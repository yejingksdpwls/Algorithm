### [ 문제 설명 ]
함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.

&nbsp;

### [ 코드 및 설명 ]
```python
def solution(n):
    list = []
    for i in str(n): 							# 입력받은 수를 문자열로 만들어 하나씩 추출
        list.append(i)
        list.sort(reverse=True) 				# 하나씩 추출한 수를 내림차순으로 정렬
    list = "".join(list)						# 정렬된 문자열 하나로 병합
    return int(list) 							# 병합한 문자열 숫자로 반환
```
&nbsp;

#### [ 개선할 점 ]
```python
ls = list(str(n))
ls.sort(reverse = True)
```
---> 굳이 하나씩 추출하지 않아도 문자열 변환 후 리스트로 만든 뒤 바로 정렬 가능함