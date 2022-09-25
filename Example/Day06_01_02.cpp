// 피보나치 수열 : 단순 재귀 소스 코드 (C++)

#include <bits/stdc++.h>

using namespace std;

int fibo(int x) {
  if (x == 1 || x == 2) {
    return 1;
  }
  return fibo(x - 1) + fibo(x - 2);
}

int main(void) {
  cout << fibo(4) << '\n';
  return 0;
}
