// 다익스트라 알고리즘 : 간단한 구현 방법 (Java)

import java.util.*;

//Java에서는 별도로 튜플이나 페어와 같은 라이브러리를 바로 제공하지 않기 때문에 별도로 Node라는 이름의 클래스를 정의해서 특정 노드 번호까지의 거리가 얼마인지를 기록할 수 있는 하나의 자료 구조를 정의한다.
class Node { //이때 여기에서 이 노드는 인접한 노드를 의미하는 하나의 클래스라고 보면 된다.

  private int index;
  private int distance;

  public Node(int index, int distance) {
    this.index = index;
    this.distance = distance;
  }

  public int getIndex() {
    return this.index;
  }

  public int getDistance() {
    return this.distance;
  }
}

public class Main {

  public static final int INF = (int) 1e9; // 무한을 의미하는 값으로 10억을 설정
  // 노드의 개수(N), 간선의 개수(M), 시작 노드 번호(Start)
  // 노드의 개수는 최대 100,000 개라고 가정
  public static int n, m, start;
  // 각 노드에 연결되어 있는 노드에 대한 정보를 담는 배열
  public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>(); //ArrayList에서 각각의 노드에 대하여 그 노드와 인접한 노드에 대한 정보를 이 Node 인스턴스 형태로 담아 준다. //이와 같이 ArrayList를 중첩해서 사용함으로써 전체 그래프 형태를 담을 수 있도록 한다.
  // 방문한 적이 있는지 체크하는 목적의 배열 만들기
  public static boolean[] visited = new boolean[100001];
  // 최단 거리 테이블 만들기
  public static int[] d = new int[100001];

  // 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
  public static int getSmallestNode() {
    int min_value = INF;
    int index = 0; // 가장 최단 거리가 짧은 노드(인덱스)
    for (int i = 1; i <= n; i++) {
      if (d[i] < min_value && !visited[i]) {
        min_value = d[i];
        index = i;
      }
    }
    return index;
  }

  public static void dijkstra(int start) {
    // 시작 노드에 대해서 초기화
    d[start] = 0;
    visited[start] = true;
    for (int j = 0; j < graph.get(start).size(); j++) {
      d[graph.get(start).get(j).getIndex()] = graph.get(start).get(j).getDistance(); //ArrayList의 경우 특정 인덱스의 값에 접근하기 위해 get 메소드를 호출해야 한다.
    }
    // 시작 노드를 제외한 전체 n - 1개의 노드에 대해 반복
    for (int i = 0; i < n - 1; i++) {
      // 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
      int now = getSmallestNode();
      visited[now] = true;
      // 현재 노드와 연결된 다른 노드를 확인
      for (int j = 0; j < graph.get(now).size(); j++) {
        int cost = d[now] + graph.get(now).get(j).getDistance();
        // 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if (cost < d[graph.get(now).get(j).getIndex()]) {
          d[graph.get(now).get(j).getIndex()] = cost;
        }
      }
    }
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    n = sc.nextInt();
    m = sc.nextInt();
    start = sc.nextInt();

    // 그래프 초기화
    for (int i = 0; i <= n; i++) {
      graph.add(new ArrayList<Node>());
    }

    // 모든 간선 정보를 입력받기
    for (int i = 0; i < m; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      int c = sc.nextInt();
      // a 번 노드에서 b 번 노드로 가는 비용이 c라는 의미
      graph.get(a).add(new Node(b, c));
    }

    // 최단 거리 테이블을 모두 무한으로 초기화
    Arrays.fill(d, INF);

    // 다익스트라 알고리즘을 수행
    dijkstra(start);

    // 모든 노드로 가기 위한 최단 거리를 출력
    for (int i = 1; i <= n; i++) {
      // 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
      if (d[i] == INF) {
        System.out.println("INFINITY");
      }
      // 도달할 수 있는 경우, 거리를 출력
      else {
        System.out.println(d[i]);
      }
    }
  }
}
