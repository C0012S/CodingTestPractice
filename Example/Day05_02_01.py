# 추가적으로 코딩 테스트 문제 풀이를 위해 알아 두면 좋은 라이브러리
# 파이썬 이진 탐색 라이브러리

"""
bisect_left(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 정렬된 순서를 유지하면서 배열 a에 x를 삽입할 가장 오른쪽 인덱스를 반환

Python에서의 bisect_left는 C++에서의 lower_bound와 동일하며, bisect_right는 C++에서의 upper_bound와 사실상 같다고 볼 수 있다.
"""

from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))
print(bisect_right(a, x))