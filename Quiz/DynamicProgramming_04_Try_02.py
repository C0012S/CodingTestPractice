"""
<문제> 금광 : 문제 설명
  - n ⅹ m 크기의 금광이 있습니다. 금광은 1 ⅹ 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
  - 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다. 이후에 m - 1 번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3 가지 중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.
    1  3  3  2
    2  1  4  1        → 얻을 수 있는 금의 최대 크기 : 19
    0  6  4  7


<문제> 금광 : 문제 조건
  난이도 ●◐○ | 풀이 시간 30 분 | 시간 제한 1 초 | 메모리 제한 128MB | 기출 Flipkart 인터뷰

  - 입력 조건
    - 첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
    - 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20) 둘째 줄에 n ⅹ m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1 <= 각 위치에 매장된 금의 개수 <= 100)
  
  - 출력 조건
    - 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다. 각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.
"""


# 다시 풀어 봐야 한다. 
# 현재 행마다 오른쪽으로 이동하여 값을 확인하는 식으로 코드 작성
# 행마다 말고 열 기준으로 아래로 이동하며 값을 확인하는 식으로 코드 작성해 보기


# 점화식 : max_gold[i][j] = gold_list[i][j] + max(max_gold[i - 1][j - 1], max_gold[i][j - 1], max_gold[i + 1][j - 1])

T = int(input())

for t in range(T):
  n, m = map(int, input().split(' '))

  gold_list = [[0] * m for _ in range(n)] # 각 위치에 매장된 금의 개수를 담을 2 차원 리스트
  g = list(input().split(' ')) # 매장된 금의 개수 입력 # 리스트로 변환

  x = 0
  for r in range(n):
    for c in range(m):
      gold_list[r][c] = int(g[x]) # 입력받은 매장된 금의 개수를 2 차원 리스트에 담기
      x += 1

#  print(gold_list)

  max_gold = [[0] * m for _ in range(n)] # 각 위치의 채굴자가 얻을 수 있는 금의 최대 크기를 담는 2 차원 리스트
  max_gold = gold_list

  for r in range(n):
    for c in range(1, m):
      if r == 0: # 왼쪽 위가 존재하지 않는 경우
        leftUp = 0
      else:
        leftUp = r - 1
        
      if r == n - 1: # 왼쪽 아래가 존재하지 않는 경우
        leftDown = 0
      else:
        leftDown = r + 1
        
      # 왼쪽
      left = r
      
      max_gold[r][c] = gold_list[r][c] + max(max_gold[leftUp][c - 1], max_gold[left][c - 1], max_gold[leftDown][c - 1])

  result = max_gold[0][m - 1]
  for r in range(1, n):
    result = max(result, max_gold[r][m - 1]) # max_gold 2 차원 리스트의 마지막 열에서 가장 큰 값

  print(result)
