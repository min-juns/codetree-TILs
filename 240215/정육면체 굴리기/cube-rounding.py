import copy
# n: 말판의 세로 크기, m: 가로 크기, (x, y): 처음 위치, k: 굴리기 횟수
n, m, x, y, k = map(int, input().split())


game_map = [list(map(int, input().split())) for _ in range(n)]
game = list(map(int, input().split()))

dice = [[0], [0, 0, 0, 0], [0]]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

def move_dice(direction, nr, nc):
    global game_map
    global dice
    temp_dice = copy.deepcopy(dice)

    if direction == 0:
        temp_dice[0][0] = dice[1][0]
        temp_dice[1][0] = dice[2][0]
        temp_dice[1][1] = dice[0][0]
        temp_dice[1][2] = dice[1][2]
        temp_dice[1][3] = dice[1][3]
        temp_dice[2][0] = dice[1][1]

    elif direction == 1:
        temp_dice[0][0] = dice[1][1]
        temp_dice[1][0] = dice[0][0]
        temp_dice[1][1] = dice[2][0]
        temp_dice[1][2] = dice[1][2]
        temp_dice[1][3] = dice[1][3]
        temp_dice[2][0] = dice[1][0]

    elif direction == 2:
        temp_dice[0][0] = dice[1][3]
        temp_dice[1][0] = dice[1][0]
        temp_dice[1][1] = dice[1][1]
        temp_dice[1][2] = dice[0][0]
        temp_dice[1][3] = dice[2][0]
        temp_dice[2][0] = dice[1][2]

    elif direction == 3:
        temp_dice[0][0] = dice[1][2]
        temp_dice[1][0] = dice[1][0]
        temp_dice[1][1] = dice[1][1]
        temp_dice[1][2] = dice[2][0]
        temp_dice[1][3] = dice[0][0]
        temp_dice[2][0] = dice[1][3]

    if game_map[nr][nc] == 0:
        game_map[nr][nc] = temp_dice[0][0]
    else:
        temp_dice[0][0] = game_map[nr][nc]
        game_map[nr][nc] = 0

    print(temp_dice[2][0])
    dice = temp_dice


for t in range(k):
    d = game[t] - 1
    nx = x + dr[d]
    ny = y + dc[d]

    if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue

    val = game_map[nx][ny]
    move_dice(d, nx, ny)
    x, y = nx, ny