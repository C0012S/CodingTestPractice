"""
다이나믹 프로그래밍 VS 분할 정복
  - 다이나믹 프로그래밍과 분할 정복은 모두 최적 부분 구조를 가질 때 사용할 수 있습니다.
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있는 상황
  - 다이나믹 프로그래밍과 분할 정복의 차이점은 부분 문제의 중복입니다.
    - 다이나믹 프로그래밍 문제에서는 각 부분 문제들이 서로 영향을 미치며 부분 문제가 중복됩니다.
    - 분할 정복 문제에서는 동일한 부분 문제가 반복적으로 계산되지 않습니다.

  - 분할 정복의 대표적인 예시인 퀵 정렬을 살펴봅시다.
    - 한 번 기준 원소(Pivot)가 자리를 변경해서 자리를 잡으면 그 기준 원소의 위치는 바뀌지 않습니다.
    - 분할 이후에 해당 피벗을 다시 처리하는 부분 문제는 호출하지 않습니다.


다이나믹 프로그래밍 문제에 접근하는 방법
  - 주어진 문제가 다이나믹 프로그래밍 유형임을 파악하는 것이 중요합니다.
  - 가장 먼저 그리디, 구현, 완전 탐색 등의 아이디어로 문제를 해결할 수 있는지 검토할 수 있습니다.
    - 다른 알고리즘으로 풀이 방법이 떠오르지 않으면 다이나믹 프로그래밍을 고려해 봅시다.
  - 일단 재귀 함수로 비효율적인 완전 탐색 프로그램을 작성한 뒤에 (탑다운) 작은 문제에서 구한 답이 큰 문제에서 그대로 사용될 수 있으면, 코드를 개선하는 방법을 사용할 수 있습니다.
  - 일반적인 코딩 테스트 수준에서는 기본 유형의 다이나믹 프로그래밍 문제가 출제되는 경우가 많습니다.
"""