# Algorithm Study D+1
# Difficulty: Class 2, Bronze 3
# Problem URL: https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, raw_input().split())

minX = min(x, w-x)
minY = min(y, h-y)

print(min(minX, minY))