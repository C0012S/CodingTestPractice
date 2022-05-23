// 이진 탐색 소스 코드 : 반복문 구현 (C++)

#include <bits/stdc++.h>

using namespace std;

// 하나의 array 정보를 입력 받을 때, 포인터를 사용하거나 이와 같이 vector 라이브러리를 사용하되 별도로 변수를 카피하지 않고, 이미 존재하는 그 vector 변수의 reference를 전달할 수 있도록 한다. 만약 &를 떼어 주게 되면, 이 함수를 호출할 때 기존의 vector에 담겨 있던 값을 카피하기 때문에 시간 복잡도가 O(N)이 된다. 그렇기 때문에 반드시 이렇게 vector를 넘겨 줄 때는 reference를 넘겨 줄 수 있도록 한다.
int binarySearch(vector<int>& arr, int target, int start, int end) {
  while (start <= end) {
    int mid = (start + end) / 2;

    // 찾은 경우 중간점 인덱스 반환
    if (arr[mid] == target) return mid;
    // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    else if (arr[mid] > target) end = mid - 1;
    // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else start = mid + 1;
  }

  return -1;
}

int n, target;
vector<int> arr;

int main(void) {
  // n(원소의 개수)과 target(찾고자 하는 값)을 입력 받기
  cin >> n >> target;
  // 전체 원소 입력 받기
  for (int i = 0; i < n; i++) {
    int x;
    cin >> x;
    arr.push_back(x);
  }

  // 이진 탐색 수행 결과 출력
  int result = binarySearch(arr, target, 0, n - 1);
  if (result == -1) {
    cout << "원소가 존재하지 않습니다." << "\n";
  }
  else {
    cout << result + 1 << '\n';
  }

  return 0;
}