# Algorithm Study D+9
# Difficulty: Class 2, Bronze 1
# Problem URL: https:/www.acmicpc.net/problem/2869

import math
A, B, V = map(int, input().split())
snail = (V-B) / (A-B)
print(math.ceil(snail))