# Algorithm Study D+9
# Difficulty: Class 2, Bronze 1
# Problem URL: https:/www.acmicpc.net/problem/2839

N = int(input())
result = 0

while True:
    if N % 5 == 0:
        result += (N // 5)
        print(result)
        break

    N -= 3
    result += 1

    if N < 0:
        print(-1)
        break