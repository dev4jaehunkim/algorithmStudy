# Algorithm Study D+12
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/1181

arr = []
n = int(input())

for _ in range(n):
    arr.append(input())

arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for i in range(0, len(arr)):
    print(arr[i])