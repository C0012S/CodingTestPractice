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


# 점화식 : min_money_count[n] = min(min_money_count[n], min_money_count[n - value[k]] + 1) (min_money_count[n - value[k]]가 존재하는 경우)

N, M = map(int, input().split(' ')) # N : 화폐의 개수, M : 화폐를 이용해 만들 가치 값

value = list() # 화폐의 가치 리스트
for i in range(N):
  value.append(int(input()))

min_money_count = [10001] * (M + 1) # M 원을 만들기 위한 화폐의 최소 개수 리스트 # min_money_count[n - value[k]]가 존재하는 경우가 존재하지 않을 경우 10001 값을 가지도록 초기화
min_money_count[0] = 0 # 0 원을 만들기 위한 화폐의 최소 개수

for i in range(0, N):
  for j in range(value[i], M + 1):
    if (min_money_count[j - value[i]] != 10001): # min_money_count[n - value[k]]가 존재하는 경우
      min_money_count[j] = min(min_money_count[j], min_money_count[j - value[i]] + 1)

if (min_money_count[M] != 10001):
  print(min_money_count[M])
else:
  print(-1)
