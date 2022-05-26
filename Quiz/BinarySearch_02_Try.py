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
"""


# 다시 풀어 봐야 한다.

# 이진 탐색
def binary_search(list, target, start, end):
  if start > end:
    return None
  mid = (start + end) // 2
  
  if target == list[mid]:
    return mid
  elif target > list[mid]:
    start = mid + 1
    return binary_search(list, target, start, end)
  else: # target < list[mid]
    end = mid - 1
    return binary_search(list, target, start, end)

# 개수 구하기
def search_x(list, target, start, end):
  if start > end:
    return 0
  mid = (start + end) // 2
  
  left_target = binary_search(list, target, start, mid - 1)
  right_target = binary_search(list, target, mid + 1, end)
  return right_target - left_target + 1

N, x = map(int, input().split(' '))
list = list(map(int, input().split()))

count = search_x(list, x, 0, N - 1)

if count <= 0:
  print(-1)
else:
  print(count)
