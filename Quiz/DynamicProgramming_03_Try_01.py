"""
<문제> 효율적인 화폐 구성 : 문제 설명
  - N 가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M 원이 되도록 하려고 합니다. 이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
  - 예를 들어 2 원, 3 원 단위의 화폐가 있을 때는 15 원을 만들기 위해 3 원을 5 개 사용하는 것이 가장 최소한의 화폐 개수입니다.
  - M 원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.


<문제> 효율적인 화폐 구성 : 문제 조건
  난이도 ●●○ | 풀이 시간 30 분 | 시간 제한 1 초 | 메모리 제한 128MB
  
  - 입력 조건
    - 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)
    - 이후의 N 개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.
  
  - 출력 조건
    - 첫째 줄에 최소 화폐 개수를 출력한다.
    - 불가능할 때는 -1을 출력한다.
"""


# 다시 풀어 봐야 한다.


# 점화식 : min_money_count[n] = min(min_money_count[n - money1] + 1, min_money_count[n - money2] + 1)

N, M = map(int, input().split(' '))

money = [0] * N

for i in range(0, N):
  money[i] = int(input())

min_money_count = [0] * 10001 # min_money_count[0] = 0

"""
for i in range(1, M + 1):
  for j in range(1, N + 1):
    min_money_count[i] = min(min_money_count[i] + 1, min_money_count[i - j] + 1)
"""    

for i in range(1, M + 1):
  for j in range(0, N):
    min_money_count[i] = min(min_money_count[i] + 1, min_money_count[i - money[j]] + 1)

print(min_money_count[M])
