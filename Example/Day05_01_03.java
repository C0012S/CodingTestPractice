import java.util.*;

public class Main {

  // 이진 탐색 소스 코드 구현 (반복문)
  // binarySearch 함수는 하나의 배열의 reference 값을 입력으로 받아서 이와 같이 매 step마다, 현재 중간점 위치의 값이 찾고자 하는 값과 동일한지 검사를 해서 만약 그렇다면 현재의 인덱스 값을 return 할 수 있도록 하고, 그렇지 않은 경우 탐색 범위를 반씩 줄이면서 범위를 좁혀 나가는 것을 확인할 수 있다.
  public static int binarySearch(int[] arr, int target, int start, int end) {
    while (start <= end) {
      int mid = (start + end) / 2;

      // 찾은 경우 중간점 인덱스 반환
      if (arr[mid] == target) return mid;
      // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
      else if (arr[mid] > target) end = mid - 1;
      // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
      else start = mid + 1;
    }

    // 해당 값을 찾지 못했다면 -1 값을 return하도록 해서 찾지 못했다는 정보를 이 함수를 호출한 위치에서 알 수 있도록 한다.
    return -1;
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    // 원소의 개수(n)과 찾고자 하는 값(target)을 입력 받기
    int n = sc.nextInt();
    int target = sc.nextInt();

    // 전체 원소 입력 받기
    int[] arr = new int[n];
    for (int i = 0; i < n; i++) {
      arr[i] = sc.nextInt();
    }

    // 이진 탐색 수행 결과 출력
    int result = binarySearch(arr, target, 0, n - 1);
    if (result == -1) {
      System.out.println("원소가 존재하지 않습니다.");
    }
    else {
      System.out.println(result + 1);
    }
  }
}