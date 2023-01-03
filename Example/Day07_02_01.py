"""
우선순위 큐(Priority Queue)
  - 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조입니다.
  - 예를 들어 여러 개의 물건 데이터를 자료구조에 넣었다가 가치가 높은 물건 데이터부터 꺼내서 확인해야 하는 경우에 우선순위 큐를 이용할 수 있습니다.
  - Python, C++, Java를 포함한 대부분의 프로그래밍 언어에서 표준 라이브러리 형태로 지원합니다.
    자료구조                      추출되는 데이터
    스택(Stack)                    가장 나중에 삽입된 데이터
    큐(Queue)                      가장 먼저 삽입된 데이터
    우선순위 큐(Priority Queue)     가장 우선순위가 높은 데이터


힙(Heap)
  - 우선순위 큐(Priority Queue)를 구현하기 위해 사용하는 자료구조 중 하나입니다.
  - 최소 힙(Min Heap)과 최대 힙(Max Heap)이 있습니다.
    * 최소 힙 : 값이 낮은 데이터부터 꺼내는 방식으로 동작
    * 최대 힙 : 값이 높은 데이터부터 꺼내는 방식으로 동작
  - 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용됩니다.
    우선순위 큐 구현 방식    삽입 시간      삭제 시간
    리스트                  O(1)          O(N)
    힙(Heap)               O(logN)        O(logN)
      * 힙은 데이터를 삽입하거나 삭제하는 과정에서 logN만큼의 시간 복잡도가 소요되기 때문에 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 사용된다.
      * 이때 만약에 우선순위 큐를 구현하기 위해서 단순히 리스트를 이용한다면, 데이터를 삽입할 때는 그냥 데이터를 맨 뒤에 차례대로 넣으면 되기 때문에 상수 시간이 걸린다고 할 수 있다. 반면에 데이터를 삭제할 때는 전체 데이터를 순회하며 우선순위가 가장 높은 데이터가 무엇인지 확인해야 되기 때문에 이와 같이 선형 시간이 걸리는 것을 확인할 수 있다.
      * 반면에 힙은 내부적으로 트리 구조를 이용하여 데이터의 삽입과 삭제에 있어서 O(logN)만큼의 수행 시간을 보장할 수 있는 형태로 구현된 자료구조이기 때문에 이를 이용해서 우선순위 큐를 구현하게 되면, 삽입과 삭제에 있어서 모두 logN만큼의 수행 시간이 걸리게 된다.
"""


# 힙 라이브러리 사용 예제 : 최소 힙

import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for i in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

"""
실행 결과
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

#heappush : 특정 리스트에 어떠한 데이터를 넣을 때 사용할 수 있는 메소드
#heappop : 특정 리스트에서 데이터를 꺼낼 때 사용하는 메소드
#힙 라이브러리는 데이터를 꺼낼 때 우선순위가 높은 데이터부터 차례대로 나온다는 특징 때문에 이러한 힙 자료구조의 특성을 이용해서 정렬을 수행할 수 있다.
#기본적으로 Python은 힙 라이브러리를 그대로 사용하게 되면 최소 힙 즉, Min Heap 방식으로 힙 라이브러리가 구현되어 있기 때문에 우선순위가 낮은 원소부터 차례대로 꺼내지게 된다. 
#따라서 오름차순으로 데이터를 정렬하고자 한다면, 단순히 힙에 모든 데이터를 다 넣었다가 이제 그 힙 자료구조에서 다시 모든 데이터를 다 꺼내게 되면 그렇게 꺼내진 데이터 순서 자체가 오름차순 정렬이 이루어진 형태가 된다.
#힙 자료구조는 기본적으로 데이터를 넣을 때 O(logN)만큼의 수행 시간이 소요되기 때문에 이와 같이 N 개의 데이터를 차례대로 힙에 넣었다가 꺼내는 과정을 수행하게 되면 전체 시간 복잡도는 O(NlogN)이다. 이는 기본적으로 표준 라이브러리에서 제공하는 병합 정렬 혹은 퀵 정렬 기반의 정렬 알고리즘과 동일한 시간 복잡도라고 할 수 있다. 즉, 힙 정렬 또한 마찬가지로 이와 같이 단순히 힙에 데이터를 모두 넣었다가 꺼내는 과정만으로 최악의 경우에도 O(NlogN)을 보장할 수 있기 때문에 이러한 힙을 이용해서도 정렬을 NlogN으로 수행할 수 있는 것이다.
