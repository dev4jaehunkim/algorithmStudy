# Algorithm Study D+14
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/2609

def getGcd(n1, n2):
    if n1 % n2 == 0:
        return n2
    else:
        return getGcd(n2, n1 % n2)

def getLcm(n1, n2):
    return int(n1 * n2 / getGcd(n1, n2))

n1, n2 = map(int, input().split())
print(getGcd(n1, n2))
print(getLcm(n1, n2))