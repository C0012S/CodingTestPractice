/*
<문제> 효율적인 화폐 구성 : 문제 설명
  - N 가지 종류의 화폐가 있습니다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M 원이 되도록 하려고 합니다. 이때 각 종류의 화폐는 몇 개라도 사용할 수 있습니다.
  - 예를 들어 2 원, 3 원 단위의 화폐가 있을 때는 15 원을 만들기 위해 3 원을 5 개 사용하는 것이 가장 최소한의 화폐 개수입니다.
  - M 원을 만들기 위한 최소한의 화폐 개수를 출력하는 프로그램을 작성하세요.


<문제> 효율적인 화폐 구성 : 문제 조건
  난이도 ●●○ | 풀이 시간 30 분 | 시간 제한 1 초 | 메모리 제한 128MB
  
  - 입력 조건
    - 첫째 줄에 N, M이 주어진다. (1 <= N <= 100, 1 <= M <= 10,000)
    - 이후의 N 개의 줄에는 각 화폐의 가치가 주어진다. 화폐의 가치는 10,000보다 작거나 같은 자연수이다.
  
  - 출력 조건
    - 첫째 줄에 최소 화폐 개수를 출력한다.
    - 불가능할 때는 -1을 출력한다.


<문제> 효율적인 화폐 구성 : 문제 해결 아이디어
  - a_i = 금액 i를 만들 수 있는 최소한의 화폐 개수
  - k = 각 화폐의 단위
  - 점화식 : 각 화폐 단위인 k를 하나씩 확인하며
    - a_(i - k)를 만드는 방법이 존재하는 경우, a_i = min(a_i, a_(i - k) + 1)
    - a_(i - k)를 만드는 방법이 존재하지 않는 경우, a_i = INF

  - N = 3, M = 7이고, 각 화폐의 단위가 2, 3, 5인 경우 확인해 봅시다.
  - Step 0 (초기화)
    - 먼저 각 인덱스에 해당하는 값으로 INF(무한)의 값을 설정합니다.
    - INF은 특정 금액을 만들 수 있는 화폐 구성이 가능하지 않다는 의미를 가집니다.
    - 본 문제에서는 10,001을 사용할 수 있습니다.
    인덱스 0의 값 0 / 인덱스 1의 값 10,001 / 인덱스 2의 값 10,001 / 인덱스 3의 값 10,001 / 인덱스 4의 값 10,001 / 인덱스 5의 값 10,001 / 인덱스 6의 값 10,001 / 인덱스 7의 값 10,001

  - Step 1
    - 첫 번째 화폐 단위인 2를 확인합니다.
    - 점화식에 따라서 다음과 같이 리스트가 갱신됩니다.
    인덱스 0의 값 0 / 인덱스 1의 값 10,001 / 인덱스 2의 값 1 / 인덱스 3의 값 10,001 / 인덱스 4의 값 2 / 인덱스 5의 값 10,001 / 인덱스 6의 값 3 / 인덱스 7의 값 10,001
      - 4 원을 만들기 위한 개수는 2 개 : (2 원 + 2 원)
      - 7 원을 만드는 방법이 없음

  - Step 2
    - 두 번째 화폐 단위인 3을 확인합니다.
    - 점화식에 따라서 다음과 같이 리스트가 갱신됩니다.
    인덱스 0의 값 0 / 인덱스 1의 값 10,001 / 인덱스 2의 값 1 / 인덱스 3의 값 1 / 인덱스 4의 값 2 / 인덱스 5의 값 2 / 인덱스 6의 값 2 / 인덱스 7의 값 3
      - 7 원을 만들기 위한 개수는 3 개 : (2 원 + 2 원 + 3 원)

  - Step 3
    - 세 번째 화폐 단위인 5를 확인합니다.
    - 점화식에 따라서 다음과 같이 최종적으로 리스트가 갱신됩니다.
    인덱스 0의 값 0 / 인덱스 1의 값 10,001 / 인덱스 2의 값 1 / 인덱스 3의 값 1 / 인덱스 4의 값 2 / 인덱스 5의 값 1 / 인덱스 6의 값 2 / 인덱스 7의 값 2
      - 7 원을 만들기 위한 개수는 2 개 : (2 원 + 5 원)
*/


// <문제> 효율적인 화폐 구성 : 답안 예시 (C++)

#include <bits/stdc++.h>

using namespace std;

int n, m;
vector<int> arr;

int main(void) {
  cin >> n >> m;
  // N 개의 화폐 단위 정보를 입력받기
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    arr.push_back(x);
  }
  vector<int> d(m + 1, 10001); // DP 테이블 초기화
  // 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
  d[0] = 0;
  for (int i = 0; i < n; i++) {
    for (int j = arr[i]; j <= m; j++) {
      if (d[j - arr[i]] != 10001) { // (i - k) 원을 만드는 방법이 존재하는 경우
        d[j] = min(d[j], d[j - arr[i]] + 1);
      }
    }
  }
  if (d[m] == 10001) cout << -1 << '\n';
  else cout << d[m] << '\n';
}
