/*
<문제> 금광 : 문제 설명
  - n ⅹ m 크기의 금광이 있습니다. 금광은 1 ⅹ 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어 있습니다.
  - 채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작합니다. 맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있습니다. 이후에 m - 1 번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3 가지 중 하나의 위치로 이동해야 합니다. 결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램을 작성하세요.
    1  3  3  2
    2  1  4  1        → 얻을 수 있는 금의 최대 크기 : 19
    0  6  4  7


<문제> 금광 : 문제 조건
  난이도 ●◐○ | 풀이 시간 30 분 | 시간 제한 1 초 | 메모리 제한 128MB | 기출 Flipkart 인터뷰

  - 입력 조건
    - 첫째 줄에 테스트 케이스 T가 입력됩니다. (1 <= T <= 1000)
    - 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력됩니다. (1 <= n, m <= 20) 둘째 줄에 n ⅹ m 개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력됩니다. (1 <= 각 위치에 매장된 금의 개수 <= 100)
  
  - 출력 조건
    - 테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기를 출력합니다. 각 테스트 케이스는 줄 바꿈을 이용해 구분합니다.


<문제> 금광 : 문제 해결 아이디어
  - 금광의 모든 위치에 대하여 다음의 세 가지만 고려하면 됩니다.
    1. 왼쪽 위에서 오는 경우
    2. 왼쪽 아래에서 오는 경우
    3. 왼쪽에서 오는 경우
  - 세 가지 경우 중에서 가장 많은 금을 가지고 있는 경우를 테이블에 갱신해 주어 문제를 해결합니다.
    □ ↘ □   □
    □ → ■   □
    □ ↗ □   □

  - array[i][j] = i 행 j 열에 존재하는 금의 양
  - dp[i][j] = i 행 j 열까지의 최적의 해 (얻을 수 있는 금의 최댓값)
  - 점화식은 다음과 같습니다.
    dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i][j - 1], dp[i + 1][j - 1])
  - 이때 테이블에 접근할 때마다 리스트의 범위를 벗어나지 않는지 체크해야 합니다.
  - 편의상 초기 데이터를 담는 변수 array를 사용하지 않아도 됩니다.
    - 바로 DP 테이블에 초기 데이터를 담아서 다이나믹 프로그래밍을 적용할 수 있습니다.

  - 금광 문제를 다이나믹 프로그래밍으로 해결하는 과정을 확인합시다.
    1 3 3                     1 □ □
    2 1 4  → DP 테이블 초기화   2 □ □
    0 6 4                     0 □ □
                                ↓ DP 테이블 갱신
                        1 → 5   □      1 ↘ 5   □
                        2 ↗ □   □      2 → 3   □  ...
                        0   □   □      0 ↗ □   □  (반복)
*/


// <문제> 금광 : 답안 예시 (C++)

#include <bits/stdc++.h>

using namespace std;

int testCase, n, m;
int arr[20][20];
int dp[20][20];

int main(void) {
  // 테스트 케이스(Test Case) 입력
  cin >> testCase;
  for (int tc = 0; tc < testCase; tc++) {
    // 금광 정보 입력
    cin >> n >> m;
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        cin >> arr[i][j]; // 데이터가 한 줄에 들어온다고 하더라도 공백 기준으로 들어오기 때문에 2 차원 테이블에 바로 하나씩 넣어 줄 수 있다.
      }
    }
    // 다이나믹 프로그래밍을 위한 2 차원 DP 테이블 초기화
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        dp[i][j] = arr[i][j]; // 별도로 DP 테이블로 해당 값들을 옮긴다.
      }
    }
    // 다이나믹 프로그래밍 진행 // 보텀업 방식
    for (int j = 1; j < m; j++) {
      for (int i = 0; i < n; i++) {
        int leftUp, leftDown, left;
        // 왼쪽 위에서 오는 경우
        if (i == 0) leftUp = 0;
        else leftUp = dp[i - 1][j - 1];
        // 왼쪽 아래에서 오는 경우
        if (i == n - 1) leftDown = 0;
        else leftDown = dp[i + 1][j - 1];
        // 왼쪽에서 오는 경우
        left = dp[i][j - 1];
        dp[i][j] = dp[i][j] + max(leftUp, max(leftDown, left));
      }
    }
    int result = 0;
    for (int i = 0; i < n; i++) {
      result = max(result, dp[i][m - 1]);
    }
    cout << result << '\n';
  }
}
