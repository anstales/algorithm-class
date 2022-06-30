# 내장 함수 : 기본

# itertools 
# - 모든 경우의 수를 처리해야할 때(순열, 조합)

# heapq
# - 우선순위 큐 기능을 구현해야 할 때

# bisect
# - 이진 탐색 기능을 제공

# collections
# - 덱(deque), 카운터(Counter) 자료구조를 제공

# math
# - 수학식 제공

# 내장함수
result = sum([1,2,3,4,5,6,7,8,9])
print(result)
min_result = min(9,1,6,7)
max_result = max(6,7,8,1)
print(min_result)
print(max_result)

# 문자열로 된 식을 알아서 계산해줌
result = eval("(3+5)*7")
print(result)

# sorted()
# sorted(리스트, 정렬기준키값, 정렬옵션)
# sorted(list, key=lambda x:x[1], reverse=True)

# nPr = 앞! / 뺀!
# nCr = 앞! / 뒷! 뺀!