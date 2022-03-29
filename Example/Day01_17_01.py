a = 10

def func():
  # a = 0 # 이 구문이 없으면 func 내부에는 a 변수가 아직 선언되지 않은 상태이기 때문에 바깥쪽에 있는 a를 참조하지 않고 그냥 a라는 변수 자체가 없다고 인식하는 걸 확인할 수 있다. # print 했을 때 1 출력
  global a # 바깥쪽에 있는 a 변수를 참조하고자 한다면, global 키워드를 이용해서 바깥쪽에 있는 a를 참조하겠다고 명시한다. # print 했을 때 11 출력
  a += 1
  print(a)

func()