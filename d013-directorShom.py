# Algorithm Study D+13
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/1436

doomNum = 0
cnt = 0
N = int(input())

while cnt < N:
    doomNum += 1
    if '666' in str(doomNum):
        cnt += 1

print(doomNum)