# Algorithm Study D+8
# Difficulty: Class 2, Bronze 1
# Problem URL: https:/www.acmicpc.net/problem/1259

while True:
    palindrome = list(map(int, input()))
    reversedPal = list(reversed(palindrome))
    
    if (palindrome[0] == 0):
        break

    if (palindrome == reversedPal):
        print("yes")
    else:
        print("no")