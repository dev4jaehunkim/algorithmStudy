# 벌집, Algorithm Study D+4
# Difficulty: Class 2, Bronze 2
# Problem URL: https:/www.acmicpc.net/problem/2292

n = int(input())
cnt = 1
honeycomb = 1

while n > honeycomb:
    honeycomb += 6 * cnt
    cnt += 1

print(cnt)
