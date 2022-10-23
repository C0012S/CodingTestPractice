"""
<문제> 병사 배치하기 : 문제 설명
  - N 명의 병사가 무작위로 나열되어 있습니다. 각 병사는 특정한 값의 전투력을 보유하고 있습니다.
  - 병사를 배치할 때는 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다. 다시 말해 앞쪽에 있는 병사의 전투력이 항상 뒤쪽에 있는 병사보다 높아야 합니다.
  - 또한 배치 과정에서는 특정한 위치에 있는 병사를 열외시키는 방법을 이용합니다. 그러면서도 남아 있는 병사의 수가 최대가 되도록 하고 싶습니다.

  - 예를 들어, N = 7일 때 나열된 병사들의 전투력이 다음과 같다고 가정하겠습니다.
    병사 번호    1    2    3    4    5    6    7
    전투력      15   11    4    8    5    2    4
  - 이때 3 번 병사와 6 번 병사를 열외시키면, 다음과 같이 남아 있는 병사의 수가 내림차순의 형태가 되며 5 명이 됩니다. 이는 남아 있는 병사의 수가 최대가 되도록 하는 방법입니다.
    병사 번호    1    2    4    5    7
    전투력      15   11    8    5    4
      * 이 경우에서는 구하고자 하는 정답 즉, 최적의 해가 5이다.
  - 병사에 대한 정보가 주어졌을 때, 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력하는 프로그램을 작성하세요.


<문제> 병사 배치하기 : 문제 조건
  난이도 ●◐○ | 풀이 시간 40 분 | 시간 제한 1 초 | 메모리 제한 256MB | 기출 핵심 유형

  - 입력 조건
    - 첫째 줄에 N이 주어집니다. (1 <= N <= 2,000) 둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례대로 주어집니다. 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수입니다.
      * N이 최대 2000까지 들어올 수 있기 때문에 시간 제한이 1 초인 상황에서 가능하면 O(N^2) 이하의 시간 복잡도를 가지는 알고리즘을 설계할 필요가 있다.
  
  - 출력 조건
    - 첫째 줄에 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력합니다.


<문제> 병사 배치하기 : 문제 해결 아이디어
  - 이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열(Longest Increasing Subsequence, LIS)로 알려진 전형적인 다이나믹 프로그래밍 문제의 아이디어와 같습니다.
  - 예를 들어 하나의 수열 array = {4, 2, 5, 8, 4, 11, 15}이 있다고 합시다.
    - 이 수열의 가장 긴 증가하는 부분 수열은 {4, 5, 8, 11, 15}입니다.
  - 본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치환할 수 있으므로, LIS 알고리즘을 조금 수정하여 적용함으로써 정답을 도출할 수 있습니다.

  - 가장 긴 증가하는 부분 수열(LIS) 알고리즘을 확인해 봅시다.
  - D[i] = array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이
  - 점화식은 다음과 같습니다.
    모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
      * 이때 이 i는 각각의 원소가 된다. 이제 그 원소의 앞에 있는(j), 다른 원소에 대한 정보를 확인하도록 하는 것이다.
      * 다시 말해서 이 i보다 앞쪽에 있는 모든 원소를 확인하면서 이제 그 원소가 현재 확인하고 있는 원소보다 작다면, 이러한 점화식에 따라서 테이블을 갱신할 수 있는 것이다.
      * 이렇게 해 주는 이유는, 우리가 구하고자 하는 내용이 가장 긴 증가하는 부분 수열이기 때문이다. 따라서 증가하는 형태가 되어야 하기 때문에 이 앞에 있는 원소가 뒤에 있는 원소보다 더 작을 때에만 이러한 점화식에 따라서 갱신한다고 보면 된다.
      * 따라서 모든 원소(i)를 하나씩 확인하면서, 그 원소를 마지막 원소로 가지는 부분 수열의 최대의 길이를 구하기 위해서 이 앞에 있는 원소들(j)을 매번 확인해야 하기 때문에 전체 시간 복잡도는 최악의 경우 O(N^2)이라고 표현할 수 있다.
      * 그래서 결과적으로 우리는 부분 수열의 최대의 길이를 구하는 것이기 때문에 현재 확인하고 있는 원소보다 더 작은 원소인 j를 마지막 원소로 가지는 부분 수열의 최대의 길이를 D[j]라고 표현할 수 있다. 거기에서 길이가 하나 늘어난 것이기 때문에 D[j] + 1의 값과 현재까지의 D[i] 값과 비교해서 더 큰 값이 들어갈 수 있도록 테이블을 갱신하면 된다. 이로써 부분 수열의 최대의 길이를 구할 수 있다.

  모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
                      4  2  5  8  4  11  15
    초기 상태 i = 0    1  1  1  1  1   1   1
      * 테이블이 갱신되는 과정
      * i가 0일 때, 이때 부분 수열을 만들 때, 그냥 단순하게 각각의 원소 하나만 이용해서 수열을 만든다고 하더라도 그 길이는 1이 된다. 그렇기 때문에 기본적으로 각 원소를 마지막 원소로 가지는 부분 수열의 최대의 길이를 구한다고 했을 때, 일단 다 이렇게 값이 1이 될 수 있도록 초기화하는 것이다.
             i = 1    1  1  1  1  1   1   1
      * 인덱스는 0부터 출발하기 때문에 i가 1일 때는 두 번째 원소인 2를 마지막 원소로 가지는 부분 수열의 최대의 길이가 구해지는 것이다.
             i = 2    1  1  2  1  1   1   1
      * i가 2일 때 즉, 이 세 번째 원소를 마지막 원소로 가지는 부분 수열의 최대의 길이를 구하면 된다.
      * 먼저 4와 비교했을 때, 5가 더 크기 때문에 이 첫 번째 원소 위치까지의 optimal solution인 1에다가 1을 더한 값인 2가 들어갈 수 있도록 한다. 또 마찬가지로, 2 또한 5보다 작기 때문에 이 1에다가 1을 더한 값인 2와 비교해서 더 큰 값이 들어갈 수 있도록 한다. 다만 먼저 2라는 값이 들어가 있기 때문에 이 두 번째 원소에 대해서는 업데이트가 이루어지지 않을 것이다. 따라서 우리는 이와 같이 이 세 번째 원소를 마지막 원소로 가지는 부분 수열의 최대의 길이가 2라는 것을 알 수 있다.
             i = 3    1  1  2  3  1   1   1
             i = 4    1  1  2  3  2   1   1
             i = 5    1  1  2  3  2   4   1
             i = 6    1  1  2  3  2   4   5
      * 마찬가지의 로직으로, 네 번째 원소, 다섯 번째 원소, 여섯 번째 원소, 일곱 번째 원소까지 각각 다 이러한 점화식에 따라서 테이블을 갱신해 주면 최종적으로 남아 있는 이 1 차원 DP 테이블에 남겨 있는 값은 이와 같다. 확인해 보면 이렇게 일곱 번째 원소를 마지막 원소로 가지는 부분 수열의 최대의 길이는 5로 설정되는 것을 확인할 수 있다.
      * 따라서 이와 같이 DP 테이블을 갱신한 뒤, 최종적으로 DP 테이블에 남아 있는 값 중에서 가장 큰 값을 출력하도록 만들면 우리가 만들 수 있는 증가하는 부분 수열 중에서 가장 긴 수열의 길이를 찾은 것이라고 할 수 있다.

  - 가장 먼저 입력 받은 병사 정보의 순서를 뒤집습니다.
  - 가장 긴 증가하는 부분 수열(LIS) 알고리즘을 수행하여 정답을 도출합니다.
    * 다만, 우리가 풀고자 하는 병사 배치하기 문제는 가장 긴 감소하는 부분 수열을 구하는 문제와 같기 때문에, 먼저 입력 받은 병사 정보의 순서를 뒤집은 뒤 이 LIS 알고리즘을 그대로 적용해서 답을 도출할 수 있다.
"""


# <문제> 병사 배치하기 : 답안 예시 (Python)

n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1 차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
  for j in range(0, i):
    if array[j] < array[i]:
      dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))
