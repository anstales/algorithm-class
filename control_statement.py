# 비교 연산자
# X and Y
# X or Y
# X or not X

# 다수의 데이터를 담는 자료형 앞에 쓰이는 연산자 in
# 리스트, 튜플, 문자열, 딕셔너리
# x in list_name 리스트 안에 x가 들어 있을 때 True
# x not in list_name 리스트 안에 x가 없을 때 True

# pass 키워드
# 조건만 작성하고 실행문은 잠시 비워두고 싶을 때 사용
from unittest import result


X = False
if X :
    pass
elif not X :
    print("false")



# 반복문에서 조건이 ~~일때 다음 인덱스로 건너뛰어라
# continue

result = 0
for i in range(0,10):
    if i%2 == 0:
        continue
    result += i
print(result) # 1 + 3 + 5 + 7 + 9 = 25


# 반복문을 즉시 탈출하고 싶을 때 : break

scores = [90, 85, 77, 65, 97]
cheating_student_list = {2,4}
for i in range(5):
    if i+1 in cheating_student_list:
        continue
    if scores[i] >= 80:
        print(i+1, "번 학생은 합격입니다.")

# 1 번 학생은 합격입니다.
# 5 번 학생은 합격입니다.

# 중첩 반복문 
# 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')