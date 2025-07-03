# 가로 길이 N, 세로 길이 2인 직사각형 형태의 바닥에 1X2, 2X1, 2X2의 덮개를 이용해 채우고자 한다.
# 이 때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.

N = int(input())
array = [0]*1000

array[0]=1
array[1]=3
for i in range(2,N):
    array[i]=(array[i-1]+2*array[i-2]) % 796796

print(array[N-1])