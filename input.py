# input() 함수는 문자열을 입력받는 함수
# 따라서 여러 숫자를 한번에 입력받으려면 map() 함수를 같이 써주어야함
n = int(input())
data = list(map(int, input().split())) 
data.sort(reverse=True)

print(data)

# 사용자로부터 입력을 최대한 빠르게 받아야 하는 경우
# sys.stdin.readline()
# 엔터도 입력값이 되므로 rstrip() 메서드 함께 사용

import sys
data = sys.stdin.readline().rstrip()
print(data)