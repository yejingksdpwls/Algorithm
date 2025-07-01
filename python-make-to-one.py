# 1. X가 5로 나누어 떨어지면 5로 나눈다.
# 2. X가 3으로 나누어 떨어지면 3으로 나눈다.
# 3. X가 2로 나누어 떨어지면, 2로 나눈다.
# 4. X에서 1을 뺀다.
# 정수 X가 주어졌을 때, 연산 4개를 적절히 사용해 1을 만들려고 한다. 
# 연산을 사용하는 횟수의 최솟값을 출력하시오.

array = [0] * 30001

X = int(input())
n = 0

for i in range(2, X+1):
    array[i] = array[i-1]+1
    
    if i % 2 == 0:
        array[i] = min(array[i-1], array[i//2])+1
    
    if i % 3 == 0:
        array[i] = min(array[i-1], array[i//3])+1
    
    if i % 5 == 0:
        array[i] = min(array[i-1], array[i//5])+1

print(array[X])