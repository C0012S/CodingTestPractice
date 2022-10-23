"""
<문제> 병사 배치하기 : 문제 설명
  - N 명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있습니다.
  - 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다. 다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 합니다.
  - 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다. 그러면서도 남아 있는 병사의 수가 최대가 되도록 하고 싶습니다.

  - 예를 들어, N = 7일 때 나열된 병사들의 전투력이 다음과 같다고 가정하겠습니다.
    병사 번호    1    2    3    4    5    6    7
    전투력      15   11    4    8    5    2    4
  - 이때 3 번 병사와 6 번 병사를 열외시키면, 다음과 같이 남아 있는 병사의 수가 내림차순의 형태가 되며 5 명이 됩니다. 이는 남아 있는 병사의 수가 최대가 되도록 하는 방법입니다.
    병사 번호    1    2    4    5    7
    전투력      15   11    8    5    4
      * 이 경우에서는 구하고자 하는 정답 즉, 최적의 해가 5이다.
  - 병사에 대한 정보가 주어졌을 때, 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력하는 프로그램을 작성하세요.


<문제> 병사 배치하기 : 문제 조건
  난이도 ●◐○ | 풀이 시간 40 분 | 시간 제한 1 초 | 메모리 제한 256MB | 기출 핵심 유형

  - 입력 조건
    - 첫째 줄에 N이 주어집니다. (1 <= N <= 2,000) 둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례대로 주어집니다. 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수입니다.
      * N이 최대 2000까지 들어올 수 있기 때문에 시간 제한이 1 초인 상황에서 가능하면 O(N^2) 이하의 시간 복잡도를 가지는 알고리즘을 설계할 필요가 있다.
  
  - 출력 조건
    - 첫째 줄에 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력합니다.
"""


# 실행 결과는 맞지만 Dynamic Programming 알고리즘 적용해서 다시 풀어 보기

"""
# 아래와 같은 로직의 코드
N = int(input())
power = list(map(int, input().split(' ')))

max_power = [0] * N
minus = 0

for n in range(0, N - 1):
  if (power[n] < power[n + 1]):
    if (n == 0):
      minus += 1
      
    elif (n > 0 and power[n - 1] > power[n]):
      max_power[0] = power[0]
      minus += 1

print(minus)
"""


# 남아 있는 병사 리스트 출력하는 코드
N = int(input())
power = list(map(int, input().split(' ')))
#print(power)

max_power = [0] * N

for j in range(N):
  max_power[j] = power[j]
#print(max_power)

minus = 0 # 열외시켜야 하는 병사의 수

for n in range(0, N - 1):
  if (power[n] < power[n + 1]):
    if (n == 0):
      max_power[n] = -1
      minus += 1
      
    elif (n > 0 and power[n - 1] > power[n]): # n 번째 병사 열외

      """
      # 남아 있는 병사 리스트 생성 - 잘못 작성한 코드
      max_power = [0]
      max_power[0] = power[0]

      for i in range(1, n):
        max_power.append(power[i])
        
      max_power.append(power[n + 1])
      
      minus += 1
      """      
      
      max_power[n] = -1
      minus += 1

"""
result = 0 # 남아있는 병사의 수
for l in range(N):
  if (max_power[l] != -1):
    result += 1
"""

#print(max_power)
print(minus)
#print(result)
