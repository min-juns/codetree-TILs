# n: 격자 크기, m: 도망자 수, h: 나무 수, k: 라운드 수
n, m, h, k = map(int, input().split())

game_map = [[0 for _ in range(n)] for _ in range(n)]
runner_list = []
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
runner_list = []
# 술래 위치랑 방향 저장
for _ in range(m):
    # d: 0이면 좌우, 1이면 상하
    # 따라서, d == 2인 경우 아래를 보고 시작, d == 1면 오른쪽 보고 시작
    x, y, d = map(int, input().split())
    runner_list.append((x-1, y-1, d-1))

for _ in range(h):
    tr, tc = map(int, input().split())
    # game map에 tree가 있을 경우 1.
    game_map[tr-1][tc-1] = 1

def distance(r1,c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)


finder_pos = (n//2, n//2)
finder_d = 3
# 0이면 미방문, 1이면 그냥 이동, 2면 turn
finder_visited_map = [[0 for _ in range(n)] for _ in range(n)]
finder_visited_map[n//2][n//2] = 1
def move_finder(red):
    global finder_pos
    global finder_d
    global finder_visited_map
    cr, cc = finder_pos

    if red:
        current_val = finder_visited_map[cr][cc]
        nr, nc = cr + dr[finder_d], cc + dc[finder_d]
        # 빨간 선 라인
        if finder_d % 2 == 0:
            up_down = False
        elif finder_d % 2 != 0:
            up_down = True
        turn = True
        if up_down:
            for check_c in range(n):
                if finder_visited_map[nr][check_c] > 0:
                    turn = False
                    break
        elif not up_down:
            for check_r in range(n):
                if finder_visited_map[check_r][nc] > 0:
                    turn = False
                    break
        finder_visited_map[nr][nc] = current_val + 1
        if turn:
            finder_d = (finder_d + 1) % 4
        if (nr, nc) == (0, 0):
            finder_d = 1
        finder_pos = (nr, nc)
    # 파란 선 방향
    else:
        nr, nc = cr + dr[finder_d], cc + dc[finder_d]
        finder_pos = (nr, nc)
        next_val = finder_visited_map[nr][nc]
        nnr, nnc = nr + dr[finder_d], nc + dc[finder_d]
        if nnr < 0 or nnc < 0 or nnr >= n or nnc >= n or finder_visited_map[nnr][nnc] != next_val - 1:
            for k in range(4):
                temp_nr, temp_nc = nr + dr[k], nc + dc[k]
                if temp_nr < 0 or temp_nc < 0 or temp_nr >= n or temp_nc >= n:
                    continue
                if finder_visited_map[temp_nr][temp_nc] == next_val - 1:
                    finder_d = k
        if finder_pos == (2, 2):
            finder_d = 3

def runner_move():
    global runner_list
    next_runner_list = []
    for rl in range(len(runner_list)):
        runner_r, runner_c, runner_d = runner_list[rl]
        if distance(runner_r, runner_c, finder_pos[0], finder_pos[1]) <= 3:
            nr, nc = runner_r + dr[runner_d], runner_c + dc[runner_d]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                runner_d = (runner_d + 2) % 4
                nr, nc = runner_r + dr[runner_d], runner_c + dc[runner_d]
            # 가려는 칸에 술래가 있는 경우
            if (nr, nc) == finder_pos:
                next_runner_list.append((runner_r, runner_c, runner_d))
            else:
                next_runner_list.append((nr, nc, runner_d))
        else:
            next_runner_list.append((runner_r, runner_c, runner_d))
    runner_list = next_runner_list

total_score = 0
def detection():
    global runner_list
    temp_score = 0
    cr, cc = finder_pos
    remove_list = []
    while True:
        if cr < 0 or cc < 0 or cr >= n or cc >= n:
            break
        for k in range(len(runner_list)):
            if runner_list[k][0] == cr and runner_list[k][1] == cc:
                if game_map[cr][cc] != 0:
                    continue
                temp_score += 1
                remove_list.append((runner_list[k][0], runner_list[k][1], runner_list[k][2]))
        cr, cc = cr + dr[finder_d], cc + dc[finder_d]

    if len(remove_list) >= 1:
        for rl in remove_list:
            runner_list.remove(rl)
    return temp_score

red = True
for i in range(k):
    runner_move()
    if finder_pos == (n//2, n//2):
        red = True
        finder_visited_map = [[0 for _ in range(n)] for _ in range(n)]
        finder_visited_map[n // 2][n // 2] = 1
    elif finder_pos == (0, 0):
        red = False
    move_finder(red)
    score = detection()
    total_score += (score * (i + 1))

print(total_score)