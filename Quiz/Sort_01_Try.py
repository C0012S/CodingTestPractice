"""
<문제> 두 배열의 원소 교체 : 문제 설명
- 동빈이는 두 개의 배열 A와 B를 가지고 있습니다. 두 배열은 N 개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수입니다.
- 동빈이는 최대 K 번의 바꿔치기 연산을 수행할 수 있는데, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 바꾸는 것을 말합니다.
- 동빈이의 최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것이며, 여러분은 동빈이를 도와야 합니다.
- N, K, 그리고 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램을 작성하세요.


<문제> 두 배열의 원소 교체 : 문제 조건
난이도 ●○○ | 풀이 시간 15 분 | 시간 제한 2 초 | 메모리 제한 128MB

- 입력 조건
  - 첫 번째 줄에 N, K가 공백을 기준으로 구분되어 입력됩니다. (1 <= N <= 100,000, 0 <= K <= N)
  - 두 번째 줄에 배열 A의 원소들이 공백을 기준으로 구분되어 입력됩니다. 모든 원소는 10,000,000보다 작은 자연수입니다.
  - 세 번째 줄에 배열 B의 원소들이 공백을 기준으로 구분되어 입력됩니다. 모든 원소는 10,000,000보다 작은 자연수입니다.

- 출력 조건
  - 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력합니다.
"""

N, K = map(int, input().split(' '))
listA = list(input().split(' '))
listB = list(input().split(' '))

# listA 오름차순 정렬
sorted_listA = sorted(listA)

# listB 내림차순 정렬
sorted_listB = sorted(listB, reverse = True)

# K 번 바꿔치기
for i in range(0, K):
  if (sorted_listA[i] < sorted_listB[i]):
    sorted_listA[i], sorted_listB[i] = sorted_listB[i], sorted_listA[i]
  else:
    break

# 배열 A의 모든 원소의 합
sum = 0
for j in range(0, len(sorted_listA)):
  sum += int(sorted_listA[j])

print("배열 A의 모든 원소의 합의 최댓값 : " + str(sum))