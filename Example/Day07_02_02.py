# 힙 라이브러리 사용 예제 : 최대 힙

import heapq

# 내림차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

"""
실행 결과
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

#기본적으로 Python에서는 최소 힙을 제공하며, 별도로 최대 힙을 제공하지는 않는다.
#그렇기 때문에 최대 힙을 이용하고 싶다면 데이터를 힙에 넣기 전에 그 데이터의 부호를 바꿔서 넣은 뒤, 다시 데이터를 꺼낼 때 마찬가지로 부호를 바꿔서 꺼내 주게 되면 내부적으로 최대 힙을 이용하는 것과 같은 효과를 낼 수 있다.
#내림차순으로 힙 정렬을 수행하고자 한다면, 이렇게 단순히 최대 힙 형태로 힙이 동작하도록 만들어서 데이터를 모두 힙에 넣었다가 꺼내는 작업만으로 내림차순 정렬을 수행할 수 있다.
