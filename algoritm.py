# 크기가 N이며, 값이 x인 1차원 리스트 A 만들기
N = 10
x = 5
A = [x] * N
print(A) #[5,5,5,5,5,5,5,5,5,5]

# 음의 정수 인덱싱
B = [1,2,3,4,5,6,7,8,9,10]
# 두 번째 원소 출력
print(B[1])
# 뒤에서 첫 번째 원소 출력
print(B[-1]) # 10


# 리스트 슬라이싱
C = [1,2,3,4,5,6,7,8,9,10]
print(C[5])
# (0, 5]
print(C[0:5]) # [1, 2, 3, 4, 5]


# 리스트 컴프리헨션 : 매우 간결한 리스트 초기화 방법
D = [i for i in range(10)]
print(D) # [0,1,2,3,4,5,6,7,8,9]
D = [i for i in range(20) if i%2 == 1]
print(D) # 홀수값만 초기화 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
D = [i*i for i in range(1,10)]
print(D) # 제곱값만 초기화 [1, 4, 9, 16, 25, 36, 49, 64, 81]

# row * col 크기의 2차원 리스트 초기화(by 리스트 컴프리헨션)
row = 4
col = 3
array = [[0]* col for _ in range(row)]
print(array) 
# [
#  [0, 0, 0], 
#  [0, 0, 0], 
#  [0, 0, 0], 
#  [0, 0, 0]
# ]

# 반복문에서의 언더바(_) 사용 : 반복문에서 변수 사용 필요없을 때 넣음
for _ in range(5):
    print("Hi") # Hi Hi Hi Hi Hi 

# 리스트 관련 함수
A = [1,2,3]
A.append(4)
print(A) # [1, 2, 3, 4]
A.sort(reverse=True) 
print(A) # [4, 3, 2, 1]
A.sort()
print(A) # [1, 2, 3, 4]
A.insert(2,10) # array.insert(index, value)
print(A) # [1, 2, 10, 3, 4]
print(A.count(10)) # 1
A.remove(10)
print(A) # [1, 2, 3, 4]

# 리스트에서 특정 값을 가지는 원소 모두 제거
A = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}
result = [i for i in A if i not in remove_set]
print(result) # [1, 2, 4]