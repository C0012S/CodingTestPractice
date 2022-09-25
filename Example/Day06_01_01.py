"""
다이나믹 프로그래밍
  - 다이나믹 프로그래밍은 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법입니다.
  - 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산하지 않도록 합니다.
  - 다이나믹 프로그래밍의 구현은 일반적으로 두 가지 방식(탑다운과 보텀업)으로 구성됩니다.

  - 다이나믹 프로그래밍은 동적 계획법이라고 부릅니다.
  - 일반적인 프로그래밍 분야에서의 동적(Dynamic)이란 어떤 의미를 가질까요?
    - 자료 구조에서 동적 할당(Dynamic Allocation)은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미합니다.
    - 반면에 다이나믹 프로그래밍에서 '다이나믹'은 별다른 의미 없이 사용된 단어입니다.


다이나믹 프로그래밍의 조건
  - 다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있습니다.
    1. 최적 부분 구조(Optimal Substructure)
      - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있습니다.
    2. 중복되는 문제(Overlapping Subproblem)
      - 동일한 작은 문제를 반복적으로 해결해야 합니다.

    
피보나치 수열
  - 피보나치 수열 다음과 같은 형태의 수열이며, 다이나믹 프로그래밍으로 효과적으로 계산할 수 있습니다.
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
  - 점화식이란 인접한 항들 사이의 관계식을 의미합니다.
  - 피보나치 수열을 점화식으로 표현하면 다음과 같습니다.
    a_(n) = a_(n - 1) + a_(n - 2), a_(1) = 1, a_(2) = 1

  - 피보나치 수열이 계산되는 과정은 다음과 같이 표현할 수 있습니다.
    - 프로그래밍에서는 이러한 수열을 배열이나 리스트를 이용해 표현합니다.

  - 피보나치 수열이 계산되는 과정은 다음과 같이 표현할 수 있습니다.
    - n 번째 피보나치 수를 f(n)라고 할 때 4 번째 피보나치 수 f(4)를 구하는 과정은 다음과 같습니다.
"""


# 피보나치 수열 : 단순 재귀 소스 코드 (Python)

# 피보나치 함수(Fibonacci Function)을 재귀함수로 구현
def fibo(x):
  if x == 1 or x == 2:
    return 1
  return fibo(x - 1) + fibo(x - 2)

print(fibo(4))


"""
피보나치 수열의 시간 복잡도 분석
  - 단순 재귀 함수로 피보나치 수열을 해결하면 지수 시간 복잡도를 가지게 됩니다.
  - 다음과 같이 f(2)가 여러 번 호출되는 것을 확인할 수 있습니다. (중복되는 부분 문제)

  - 피보나치 수열의 시간 복잡도는 다음과 같습니다.
    - 세타 표기법 θ(1.618...^N)
    - 빅오 표기법 O(2^N)
  - 빅오 표기법을 기준으로 f(30)을 계산하기 위해 약 10억가량의 연산을 수행해야 합니다.
  - 그렇다면 f(100)을 계산하기 위해 얼마나 많은 연산을 수행해야 할까요?


피보나치 수열의 효율적인 해법 : 다이나믹 프로그래밍
  - 다이나믹 프로그래밍의 사용 조건을 만족하는지 확인합니다.
    1. 최적 부분 구조 : 큰 문제를 작은 문제로 나눌 수 있습니다.
    2. 중복되는 부분 문제 : 동일한 작은 문제를 반복적으로 해결합니다.
  - 피보나치 수열은 다이나믹 프로그래밍의 사용 조건을 만족합니다.
"""
