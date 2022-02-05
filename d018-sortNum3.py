# Algorithm Study D+18
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/10989
# 참고: https://somjang.tistory.com/entry/Mxmxmxm

import sys

N = int(input())

# 문제에서 제한한 최대 길이에 맞는 크기만큼 0으로 된 딕셔너리를 생성
# 리스트가 딕셔너리보다 상대적으로 메모리 사용량이 많기 때문에
checkList = [0] * 10001
            
for i in range(N):
    tmp = int(sys.stdin.readline())
    
    # 입력된 값으로 딕셔너리 조회, 그 다음 새 값을 다음 위치로 저장
    # 이로 하여 삽입될 때마다 자동으로 오름차순으로 값이 삽입됨
    checkList[tmp] = checkList[tmp] + 1

# 딕셔너리에서 값이 0이 아닌 경우,
# 즉 값이 삽입된 경우만 출력
for i in range(10001):
    if checkList[i] != 0:
        for j in range(checkList[i]):
            print(i)