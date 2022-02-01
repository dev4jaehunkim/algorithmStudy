# Algorithm Study D+16
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/7568

k = int(input())
arr = []

for _ in range(k):
    weight, height = map(int, input().split())
    arr.append((weight, height))

# 튜플을 담고 있는 리스트를 for each로 돌리면 for 안에서 튜플을 인덱스로 접근할 수 있다.
for i in arr:
    rank = 1
    for j in arr:
        if i[0] < j[0] and i[1] < j[1]:
            # 모든 사람의 덩치를 비교하여 rank를 더하면 사람의 수만큼 덩치의 수가 계산된다.
            rank += 1
    print(rank, end=" ")