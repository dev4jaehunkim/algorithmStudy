# Algorithm Study D+11
# Difficulty: Class 2, Silver 5
# Problem URL: https:/www.acmicpc.net/problem/1018

n, m = map(int, input().split())
board = []
correctionCount = []

for _ in range(n):
    board.append(input())

# 체스보드를 8x8 크기로 잘랐을 때 원래 보드의 크기를 넘지 않도록 하기 위해 -7
for y in range(n-7):
    for x in range(m-7):
        indexWhite = 0 # 흰색으로 바꿔야하는 칸 수
        indexBlack = 0 # 검은색으로 바꿔야하는 칸 수

        # 시작 지점부터 끝 지점까지 8칸이기 때문에 range(시작, 시작+8)
        for i in range(y, y+8):
            for j in range(x, x+8):
                # 행과 열의 합으로 홀수, 짝수 여부를 계산합니다.
                # 짝수 크기의 체스판일 때 시작이 흰색이라면 끝은 검은색입니다.
                if (i+j) % 2 == 0:   
                    if board[i][j] == 'B':
                        # 짝수 크기일 때는 시작과 끝이 다르므로 시작이 검은색일 때,
                        # 검은색이 아닌 칸을 흰색으로 다시 칠하는 경우의 수를 구합니다.
                        indexWhite += 1
                    else:
                        indexBlack += 1
                else:
                    if board[i][j] == 'B':
                        # 홀수 크기일 때는 시작과 끝이 같으므로 시작이 검은색일 때,
                        # 그대로 검은색으로 칠하는 경우의 수를 구합니다.
                        indexBlack += 1
                    else:
                        indexWhite += 1
        
        # 흰색으로 칠해야 하는 경우와 검은색으로 칠해야 하는 경우의 수 중 더 작은 값을 회차마다 비교하여 리스트에 추가합니다.
        correctionCount.append(min(indexWhite, indexBlack))

# 모든 기록된 경우의 수 중 가장 작은 값을 출력합니다.
print(min(correctionCount))