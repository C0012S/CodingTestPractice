// 피보나치 수열 : 보텀업 다이나믹 프로그래밍 소스 코드 (C++)

#include <bits/stdc++.h>

using namespace std;

// 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
long long d[100]; //long long 자료형은 표현 가능 범위가 제한되어 있어 99 번째 피보나치 수를 구하고자 한다면 그 범위를 벗어나서 overflow 발생

int main(void) {
  // 첫 번째 피보나치 수와 두 번째 피보나치 수는 1
  d[1] = 1;
  d[2] = 1;
  int n = 50; // 50 번째 피보나치 수를 계산

  // 피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
  for (int i = 3; i <= n; i++) {
    d[i] = d[i - 1] + d[i - 2];
  }
  cout << d[n] << '\n';
  return 0;
}
