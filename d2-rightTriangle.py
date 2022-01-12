# Algorithm Study D+2
# Difficulty: Class 2, Bronze 3
# Problem URL: https://www.acmicpc.net/problem/4153

results = []

while True:
    inputNumber = list(map(int, input().split()))
    if (sum(inputNumber) == 0):
        break
    
    hypotenuse = max(inputNumber)
    inputNumber.remove(hypotenuse)
    if (hypotenuse ** 2 == inputNumber[0] ** 2 + inputNumber[1] ** 2):
        results.append("right")
    else:
        results.append("wrong")

for result in results:
    print(result)