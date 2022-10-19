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


# 다시 풀어 봐야 한다.


# 점화식 : min_operation = min(min_operation(division), min_operation(subtraction))

X = int(input())

def dividing(X):
  quotient = X
  
  if (X % 5 == 0):
    quotient = X / 5
  elif (X % 3 == 0):
    quotient = X / 5
  elif (X % 2 == 0):
    quotient = X / 2

  return quotient

min_operation = X

while (min_operation != 1 and min_operation > 0):
  min_operation = min(dividing(min_operation), min_operation - 1)
  # print(min_operation)

print(min_operation)
