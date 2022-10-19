/*
<문제> 1로 만들기 : 문제 설명
  - 정수 X가 주어졌을 때, 정수 X에 사용할 수 있는 연산은 다음과 같이 4 가지입니다.
    1. X가 5로 나누어 떨어지면, 5로 나눕니다.
    2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
    3. X가 2로 나누어 떨어지면, 2로 나눕니다.
    4. X에서 1을 뺍니다.
  - 정수 X가 주어졌을 때, 연산 4 개를 적절히 사용해서 값을 1로 만들고자 합니다. 연산을 사용하는 횟수의 최솟값을 출력하세요. 예를 들어 정수가 26이면 다음과 같이 계산해서 3 번의 연산이 최솟값입니다.
    - 26 → 25 → 5 → 1


<문제> 1로 만들기 : 문제 조건
  난이도 ●◐○ | 풀이 시간 20 분 | 시간 제한 1 초 | 메모리 제한 128MB
  
  - 입력 조건
    - 첫째 줄에 정수 X가 주어집니다. (1 <= X <= 30,000)
  
  - 출력 조건
    - 첫째 줄에 연산을 하는 횟수의 최솟값을 출력합니다.


<문제> 1로 만들기 : 문제 해결 아이디어
  - 피보나치 수열 문제를 도식화한 것처럼 함수가 호출되는 과정을 그림으로 그려보면 다음과 같습니다.
    - 최적 부분 구조와 중복되는 부분 문제를 만족합니다.
                         f(6)
           f(5)          f(3)          f(2)
        f(4)  f(1)    f(2)  f(1)    f(1)  f(1)

  - a_i = i를 1로 만들기 위한 최소 연산 횟수
  - 점화식은 다음과 같습니다.
    a_i = min(a_(i - 1), a_(i / 2), a_(i / 3), a_(i / 5)) + 1
  - 단, 1을 빼는 연산을 제외하고는 해당 수로 나누어떨어질 때에 한해 점화식을 적용할 수 있습니다.
*/


// <문제> 1로 만들기 : 답안 예시 (C++)

#include <bits/stdc++.h>

using namespace std;

// 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
int d[30001];
int x;

int main(void) {
  cin >> x;
  // 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
  for (int i = 2; i <= x; i++) {
    // 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1;
    // 현재의 수가 2로 나누어 떨어지는 경우
    if (i % 2 == 0)
      d[i] = min(d[i], d[i / 2] + 1);
    // 현재의 수가 3으로 나누어 떨어지는 경우
    if (i % 3 == 0)
      d[i] = min(d[i], d[i / 3] + 1);
    // 현재의 수가 5로 나누어 떨어지는 경우
    if (i % 5 == 0)
      d[i] = min(d[i], d[i / 5] + 1);
  }
  cout << d[x] << '\n';
  return 0;
}
