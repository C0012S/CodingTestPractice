# 정렬 알고리즘 비교
# 추가적으로 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는 최악의 경우에도 O(NlogN)을 보장하도록 설계되어 있다.
  # 별도로 문제에서 정렬 함수를 구현하도록 요구하지 않는다면, 일반적으로 정렬 기능을 위해서 단순히 표준 정렬 라이브러리를 호출해서 정렬을 수행하는 것을 추천한다.

# 선택 정렬 - 평균 시간 복잡도 : O(N^2)  공간 복잡도 : O(N)  특징 : 아이디어가 매우 간단하다. + 구현 또한 쉬운 편이다.
# 삽입 정렬 - 평균 시간 복잡도 : O(N^2)  공간 복잡도 : O(N)  특징 : 데이터가 거의 정렬되어 있을 때는 가장 빠르다. + 일반적으로 선택 정렬에 비해서 조금 더 빠르게 동작한다. 특히 데이터가 거의 정렬되어 있을 때는 O(N)으로 가장 빠르게 동작한다.
# 퀵 정렬 - 평균 시간 복잡도 : O(NlogN)  공간 복잡도 : O(N)  특징 : 대부분의 경우에 가장 적합하며, 충분히 빠르다. + 퀵 정렬은 구현 방식에 따라서 최악의 경우 시간 복잡도가 O(N^2)이 나올 수 있다.
# 계수 정렬 - 평균 시간 복잡도 : O(N + K)  공간 복잡도 : O(N + K)  특징 : 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작한다.