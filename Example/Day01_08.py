a = dict()
a['홍길동'] = 97
a['이순신'] = 98 # 사전 자료형 초기화

print(a)

b = {
  '홍길동': 97,
  '이순신': 98
}

print(b)
print(b['이순신']) # 사전 자료형에 접근하는 방법

# key_list = b.keys()
key_list = list(b.keys()) # keys() 함수는 사전 키라는 하나의 객체로써 반환되기 때문에 list 함수를 이용해서 리스트형 데이터로 형변환을 수행해 주면 정상적으로 리스트 형태로써 출력되는 것을 확인할 수 있다.
print(key_list) # 사전 자료형에서 key 혹은 value만 뽑아내는 방법