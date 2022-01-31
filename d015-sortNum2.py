# Algorithm Study D+15
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/2751

import sys

arr = []
n = int(input())

for _ in range(n):
    arr.append(int(sys.stdin.readline()))

arr.sort()

for i in range(0, len(arr)):
    print(arr[i])