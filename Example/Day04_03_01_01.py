# 퀵 정렬이 빠른 이유 : 이상적인 경우 분할이 절반씩 일어난다면 전체 연산 횟수로 O(NlogN)를 기대할 수 있다.  - 너비 x 높이 = N x logN = NlogN
# 퀵 정렬은 평균의 경우 O(NlogN)의 시간 복잡도를 가진다. 하지만 최악의 경우 O(N^2)의 시간 복잡도를 가진다.  # 첫 번째 원소를 피벗으로 삼을 때, 이미 정렬된 배열에 대해서 퀵 정렬을 수행하면, 매번 분할이 이루어질 때마다 오른쪽 데이터만 남는 형태로 분할이 이루어지기 때문에 최악의 경우에는 분할이 수행되는 횟수가 N과 비례하고 분하을 하기 위해서 매번 선형 탐색을 수행해야 되기 때문에 전체 시간 복잡도가 O(N^2)이 된다.
# 다양한 프로그래밍 언어에서 표준 정렬 라이브러리를 제공할 때, 퀵 정렬을 기반으로 라이브러리가 작성되어 있다면 최악의 경우에도 NlogN을 보장할 수 있는 형태로 구현한다.  # 첫 번째 원소를 피벗으로 설정하는 방식으로 퀵 정렬을 직접 구현한다면 최악의 경우 N^2이 나올 수도 있다.  # 표준 라이브러리를 이용하는 경우에는 기본적으로 NlogN을 항상 보장한다.

# 퀵 정렬 소스 코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1 개인 경우 종료
    return
  
  pivot = start # 피벗은 첫 번째 원소
  left = start + 1
  right = end

  while(left <= right):
    # 피벗보다 큰 데이터를 찾을 때까지 반복
    while(left <= end and array[left] <= array[pivot]):
      left += 1
    # 피벗보다 작은 데이터를 찾을 때까지 반복
    while(left > start and array[right] >= array[pivot]):
      right -= 1
    if (left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
