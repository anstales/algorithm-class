# 사전 자료형은 키(key)와 값(value)의 쌍을 데이터로 가지는 자료형입니다.
#  1. 앞서 다루었던 리스트나 튜플이 값을 순차적으로 저장하는 것과 대비됨
# 사전 자료형은 키와 값의 쌍을 데이터로 가지며, 원하는 "변경 불가능한(Immutable) 자료형"을 키로 사용할 수 있음
# 파이썬의 사전 자료형은 해시 테이블(Hash Table)을 이용하므로 데이터의 조회 및 수정에 있어서 O(1)의 시간에 처리 가능

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'
print(data) # {'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'}

if '사과' in data : 
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

# 사전 자료형 관련 함수
# 사전 자료형에서는 키와 값을 별도로 뽑아내기 위한 함수를 지원합니다.
#  1. 키 데이터만 뽑아서 리스트로 이용 : keys()
#  2. 값 데이터만 뽑아서 리스트로 이용 : values()

key_list = data.keys()
print(key_list)         # dict_keys(['사과', '바나나', '코코넛'])
print(list(key_list))   # ['사과', '바나나', '코코넛']
value_list = data.values()
print(value_list)       # dict_values(['Apple', 'Banana', 'Coconut'])
print(list(value_list)) #['Apple', 'Banana', 'Coconut']

for key in key_list :
    print(data[key])
    # Apple
    # Banana
    # Coconut