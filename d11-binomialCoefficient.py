# Algorithm Study D+11
# Difficulty: Class 2, Bronze 1
# Problem URL: https:/www.acmicpc.net/problem/11050

from math import factorial

n, k = map(int, input().split())
coefficient = factorial(n) / (factorial(k) * factorial(n - k))
print(int(coefficient))