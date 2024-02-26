# n: 윷놀이 판의 크기, k: 말의 개수
n, k = map(int, input().split())

# 0: 흰색판, 1: 빨간색 판, 2: 파란색 판
# 이동하려는 칸이 빨간색인 경우 이동하기 전 순서를 뒤집음.
game_map = [list(map(int, input().split())) for _ in range(n)]
horse_map = [[[] for _ in range(n)] for _ in range(n)]

# 1: 오른쪽, 2: 왼쪽, 3: 윗쪽, 4: 아랫쪽
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
horse_list = []
for K in range(k):
    r, c, d = map(int, input().split())
    # id, 이동 방향 저장
    horse_map[r-1][c-1].append(K+1)
    # id, 현재 위치, 이동 방향
    horse_list.append([K+1, r-1, c-1, d-1])

def move_horse(move_list, move_r, move_c, color):
    global horse_map
    if color == 0:
        horse_map[move_r][move_c] = move_list + horse_map[move_r][move_c]
        return True
    elif color == 1:
        if len(move_list) >= 2:
            move_list.reverse()
        horse_map[move_r][move_c] = move_list + horse_map[move_r][move_c]
        return True
    elif color == 2:
        if move_r < 0 or move_c < 0 or move_r >= n or move_c >= n or game_map[move_r][move_c] == 2:
            return False
        else:
            if game_map[move_r][move_c] == 1:
                move_list.reverse()
            horse_map[move_r][move_c] = move_list + horse_map[move_r][move_c]
            return True

def reverse_direction(c_d):
    if c_d == 0:
        return 1
    elif c_d == 1:
        return 0
    elif c_d == 2:
        return 3
    elif c_d == 3:
        return 2

def check_game_over():
    for r in range(n):
        for c in range(n):
            if len(horse_map[r][c]) >= 4:
                return True
    return False


# 말이 4개 이상 겹쳐지면 그 즉시 게임 종료
turn = 0
fail = False
while True:
    finish = False
    turn += 1
    for horse in horse_list:
        horse_id = horse[0]
        cr = horse[1]
        cc = horse[2]
        cd = horse[3]
        # 움직이는 말 저장
        temp_move = []
        # 안움직이는 말 저장
        temp_no_move = []
        horse_index = 0
        move_or_not = True
        for hm in range(len(horse_map[cr][cc])):
            if move_or_not:
                temp_move.append(horse_map[cr][cc][hm])
            else:
                temp_no_move.append(horse_map[cr][cc][hm])
            if horse_map[cr][cc][hm] == horse_id:
                move_or_not = False
        nr, nc = cr + dr[cd], cc + dc[cd]
        if nr < 0 or nc < 0 or nr >= n or nc >= n:
            color = 2
        else:
            color = game_map[nr][nc]
        if color == 2:
            # 파란색이면 색깔 변경
            cd = reverse_direction(cd)
            horse[3] = cd
            # 다음 위치 변경
            nr, nc = cr + dr[cd], cc + dc[cd]

        moved = move_horse(temp_move, nr, nc, color)
        if moved:
            horse_map[cr][cc] = temp_no_move
            for hid in temp_move:
                for hl in horse_list:
                    if hl[0] == hid:
                        hl[1], hl[2] = nr, nc
        else:
            horse_map[cr][cc] = temp_move
            if len(temp_no_move) >= 1:
                horse_map[cr][cc].append(temp_no_move)

        finish = check_game_over()
        if finish:
            break
    if finish:
        break
    if turn >= 1000:
        fail = True
        break

if fail:
    print(-1)
else:
    print(turn)