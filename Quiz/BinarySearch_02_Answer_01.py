"""
<문제> 정렬된 배열에서 특정 수의 개수 구하기 : 문제 설명
- N 개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계산하세요. 예를 들어 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x = 2라면, 현재 수열에서 값이 2인 원소가 4 개이므로 4를 출력합니다.
- 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받습니다.


<문제> 정렬된 배열에서 특정 수의 개수 구하기 : 문제 조건
난이도 ●●○ | 풀이 시간 30 분 | 시간 제한 1 초 | 메모리 제한 128MB | 기출 Zoho 인터뷰

- 입력 조건
  - 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다. (1 <= N <= 1,000,000), (-(10^9) <= x <= 10^9)
  - 둘째 줄에 N 개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-(10^9) <= 각 원소의 값 <= 10^9)

- 출력 조건
  - 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.


<문제> 정렬된 배열에서 특정 수의 개수 구하기 : 문제 해결 아이디어
- 시간 복잡도 O(logN)으로 동작하는 알고리즘을 요구하고 있습니다.
  - 일반적인 선형 탐색(Linear Search)으로는 시간 초과 판정을 받습니다.
  - 하지만 데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있습니다.
- 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제를 해결할 수 있습니다.

- 이진 탐색을 직접 구현해서 작성할 수도 있고, 표준 라이브러리(bisect_left, bisect_right)를 이용해서도 구현할 수 있다.
"""


# <문제> 정렬된 배열에서 특정 수의 개수 구하기 : 답안 예시 (Python)

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
  right_index = bisect_right(array, right_value)
  left_index = bisect_left(array, left_value)
  return right_index - left_index

n, x = map(int, input().split()) # 데이터의 개수 N, 찾고자 하는 값 x 입력받기
array = list(map(int, input().split())) # 전체 데이터 입력받기

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
  print(-1)
# 값이 x인 원소가 존재한다면
else:
  print(count)