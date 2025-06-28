# 두 배열의 원소 교체
# 두 개의 배열 A와 B를 가지고 있다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는
# 모두 자연수이다. 최대 K번의 바꿔치기 연상을 수행할 수 있는데, 최종 목표는 배열 A의 모든
# 원소의 합이 최대가 되도록 하는 것이다.
# 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를
# 서로 바꾸는 것을 말한다.


N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(K):
    min_A = min(A)
    max_B = max(B)

    if min_A < max_B:
        min_A_index = A.index(min_A)
        max_B_index = B.index(max_B)

        A[min_A_index], B[max_B_index] = max_B, min_A

print(sum(A))