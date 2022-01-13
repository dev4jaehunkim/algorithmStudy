# Algorithm Study D+3
# Difficulty: Class 2, Bronze 2
# Problem URL: https:/www.acmicpc.net/problem/2231

def getDecompose(n): 
    strN = str(n)
    s = n
    for i in range(len(strN)):
        s = s + int(strN[i])
    return s

def getConstructor(m):
    for i in range(m):
        if m == getDecompose(i):
            return i
    return 0

n = int(input())
print(getConstructor(n))