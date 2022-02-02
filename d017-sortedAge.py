# Algorithm Study D+17
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/10814

N = int(input())
arr = []

for i in range(N):
    age, name = input().split()
    arr.append((int(age),name,i))

arr.sort(key=lambda x: x[0])

for i in arr:
    print(i[0], end=" ")
    print(i[1])