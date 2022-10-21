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


# 점화식 : max_gold[i] = max(max_gold[i - 1] + storage[k - 1][m - 1], max_gold[i - 1] + storage[k][m - 1], max_gold[i - 1] + storage[k + 1][m - 1])

T = int(input())

for t in range(T):
  n, m = map(int, input().split(' '))
#  print("n : ", n, ", m : ", m)

#  storage = [[0] * m] * n
  storage = [[0] * m for _ in range(n)] # 위와 다르다
#  print(storage)

  array = list(input().split(' '))
#  print(array)
  x = 0
  for i in range(0, n):
    for j in range(0, m):
#      print(array[x])
      storage[i][j] = array[x]
#      print(storage)
      x += 1      
#  print("n ⅹ m 확인 : " + "\n")
#  print(storage)

  max_gold = [0] * m
  max_gold[0] = int(storage[0][0])
  k = 0
  for l in range(1, n):
    max_gold[0] = max(max_gold[0], int(storage[l][0])) # 첫 번째 열에서 가장 큰 금의 개수를 가진 위치를 선택
    if (max_gold[0] == int(storage[l][0])):
      k = l # 가장 큰 금의 개수를 가진 위치 인덱스
#  print("max_gold : ", max_gold[0])
#  print("k : ", k)
  
  for i in range(n):
    for j in range(1, m):
      if (-1 <= k - i <= 1):
        max_gold[j] = max(max_gold[j], max_gold[j - 1] + int(storage[i][j]))
#        print("max_gold[j] :", max_gold[j], "j : ", j, "i : ", i)

  print(max_gold[m - 1])
