# 패킹과 언패킹
# 여러개의 반환값을 갖는 함수 만들기 : 반환값 패킹

from unittest import result


def operator(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
    return add, sub, mul, div # 패킹

add, sub, mul, div = operator(10, 5)
print(add, sub, mul, div) # 15 5 50 2.0

# 람다 표현식 lambda
# 이름없는 함수식
print((lambda a,b:a+b)(1,2))

array = [('이순신',50),('홍길동',20),('이황',80)]
def get_key(x):
    return x[1] # 두 번째 원소를 반환

print(sorted(array, key=get_key))
print(sorted(array, key=lambda x:x[1]))
# [('홍길동', 20), ('이순신', 50), ('이황', 80)]

list1 = [ 1, 2, 3, 4, 5]
list2 = [10,20,30,40,50]
result = map(lambda a,b:a+b, list1, list2)
print(list(result)) #[11, 22, 33, 44, 55]

