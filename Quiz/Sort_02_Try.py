"""
<문제> 위에서 아래로
난이도 ●○○ | 풀이 시간 15 분 | 시간 제한 1 초 | 메모리 제한 128MB | 기출 T 기업 코딩 테스트

하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를 큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로 정렬하는 프로그램을 만드시오.

- 입력 조건
  - 첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다. (1 <= N <= 500)
  - 둘째 줄부터 N + 1 번째 줄까지 N 개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의 자연수이다.

- 출력 조건
  - 입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는 자유롭게 출력해도 괜찮다.
"""

N = int(input()) # 수열에 속해 있는 수의 개수

# 수열에 속해 있는 수
list = []
for i in range(N):
  list.append(int(input()))

# 내림차순 정렬
list.sort(reverse = True)

# 출력
for j in range(N):
  print(list[j], end = ' ')
  