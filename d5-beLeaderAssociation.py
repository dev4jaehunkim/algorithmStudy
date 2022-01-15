# Algorithm Study D+5
# Difficulty: Class 2, Bronze 2
# Problem URL: https:/www.acmicpc.net/problem/2775

T = int(input())

for iterator in range(T):
    floor = int(input())
    room = int(input())    
    f0 = [r for r in range(1, room+1)]

    for k in range(floor):
        for i in range(1, room):
            f0[i] += f0[i-1]
    print(f0[-1])