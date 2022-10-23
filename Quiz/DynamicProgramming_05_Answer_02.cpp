/*
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
  - 병사에 대한 정보가 주어졌을 때, 남아 있는 병사의 수가 최대가 되도록 하기 위해서 열외시켜야 하는 병사의 수를 출력하는 프로그램을 작성하세요.


<문제> 병사 배치하기 : 문제 조건
  난이도 ●◐○ | 풀이 시간 40 분 | 시간 제한 1 초 | 메모리 제한 256MB | 기출 핵심 유형

  - 입력 조건
    - 첫째 줄에 N이 주어집니다. (1 <= N <= 2,000) 둘째 줄에 각 병사의 전투력이 공백으로 구분되어 차례대로 주어집니다. 각 병사의 전투력은 10,000,000보다 작거나 같은 자연수입니다.
  
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

  모든 0 <= j < i에 대하여, D[i] = max(D[i], D[j] + 1) if array[j] < array[i]
                      4  2  5  8  4  11  15
    초기 상태 i = 0    1  1  1  1  1   1   1
             i = 1    1  1  1  1  1   1   1
             i = 2    1  1  2  1  1   1   1
             i = 3    1  1  2  3  1   1   1
             i = 4    1  1  2  3  2   1   1
             i = 5    1  1  2  3  2   4   1
             i = 6    1  1  2  3  2   4   5

  - 가장 먼저 입력 받은 병사 정보의 순서를 뒤집습니다.
  - 가장 긴 증가하는 부분 수열(LIS) 알고리즘을 수행하여 정답을 도출합니다.
*/


// <문제> 병사 배치하기 : 답안 예시 (C++)

#include <bits/stdc++.h>

using namespace std;

int n;
vector<int> v;

int main(void) {
  cin >> n;
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    v.push_back(x);
  }
  // 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
  reverse(v.begin(), v.end());
  // 다이나믹 프로그래밍을 위한 1 차원 DP 테이블 초기화
  int dp[2000]; //병사의 수는 최대 2000 명까지 들어올 수 있기 때문에 총 2000까지의 데이터가 담길 수 있는 dp 테이블을 초기화한다.
  for (int i = 0; i < n; i++) dp[i] = 1;
  // 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
  for (int i = 0; i < n; i++)
    for (int j = 0; j < i; j++)
      if (v[j] < v[i]) dp[i] = max(dp[i], dp[j] + 1);
  // 열외해야 하는 병사의 최소 수를 출력
  int maxValue = 0;
  for (int i = 0; i < n; i++) maxValue = max(maxValue, dp[i]);
  cout << n - maxValue << '\n';
}