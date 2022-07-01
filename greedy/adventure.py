N = 5
X = [2,3,1,2,2]

def solution(N, X):
    group_count = 0
    person_count = 0

    # 1. X 오름차순 정렬 [1, 2, 2, 2, 3]
    X.sort()
    print(X)

    # 2. 공포도를 낮은 것부터 하나씩 확인하며
    for x in X:
        person_count += 1       # 3. 현재 그룹에 해당 모험가 포함시키기
        if person_count >= x:   # 4. 그룹 안 모험가 수보다 공포도가 크다면 그룹결성
            group_count += 1    # 4.1 출발시킨 그룹 수 증가시키기
            person_count = 0    # 4.2 그룹 안 모험가 수 초기화

    return print(group_count)

solution(N, X)