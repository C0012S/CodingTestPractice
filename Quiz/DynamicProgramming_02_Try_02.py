"""
<문제> 1로 만들기 : 문제 설명
  - 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4 가지입니다.
    1. X가 5로 나누어 떨어지면, 5로 나눕니다.
    2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
    3. X가 2로 나누어 떨어지면, 2로 나눕니다.
    4. X에서 1을 뺍니다.
  - 정수 X가 주어졌을 때, 연산 4 개를 적절히 사용해서 값을 1로 만들고자 합니다. 연산을 사용하는 횟수의 최솟값을 출력하세요. 예를 들어 정수가 26이면 다음과 같이 계산해서 3 번의 연산이 최솟값입니다.
    - 26 → 25 → 5 → 1


<문제> 1로 만들기 : 문제 조건
  난이도 ●◐○ | 풀이 시간 20 분 | 시간 제한 1 초 | 메모리 제한 128MB
  
  - 입력 조건
    - 첫째 줄에 정수 X가 주어집니다. (1 <= X <= 30,000)
  
  - 출력 조건
    - 첫째 줄에 연산을 하는 횟수의 최솟값을 출력합니다.
"""


# 점화식 : min_operation[n] = min(min_operation[n // 5], min_operation[n // 3], min_operation[n // 2], min_operation[n - 1]) + 1

X = int(input())

min_operation = [0] * 30001

for i in range(2, X + 1):
  min_operation[i] = min_operation[i - 1] + 1

  if i % 5 == 0:
    min_operation[i] = min(min_operation[i], min_operation[i // 5] + 1)

  if i % 3 == 0:
    min_operation[i] = min(min_operation[i], min_operation[i // 3] + 1)

  if i % 2 == 0:
    min_operation[i] = min(min_operation[i], min_operation[i // 2] + 1)

print(min_operation[X])
