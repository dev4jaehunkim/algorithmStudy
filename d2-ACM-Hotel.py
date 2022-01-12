# Algorithm Study D+2
# Difficulty: Class 2, Bronze 3
# Problem URL: https://www.acmicpc.net/problem/10250

t = input()
hotel = []

for i in range(int(t)):
    h, w, n = map(int, input().split())

    for x in range(w):
        for y in range(h):
            hotel.append((str(y+1) + str(x+1).zfill(2)))

    if (n == 0):
       print(hotel[n])
    else:
       print(hotel[n-1])
    
    hotel.clear()