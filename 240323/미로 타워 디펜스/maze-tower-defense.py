n, m = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

line_map = [[0 for _ in range(n)] for _ in range(n)]
index_order = []
line_map[n//2][n//2] = 1
def line_order():
    global line_map
    d = 0

    dr = [0, 1, 0, -1]
    dc = [-1, 0, 1, 0]

    cr, cc = n // 2, n // 2
    while True:
        nr, nc = cr + dr[d], cc + dc[d]
        line_map[nr][nc] = line_map[cr][cc] + 1
        index_order.append((nr, nc))
        if nr == 0 and nc == 0:
            break

        # 방향을 틀어야하는지 check
        turn = True
        if d == 0 or d == 2:
            for i in range(n):
                if i == nr:
                    continue
                if line_map[i][nc] != 0:
                    turn = False
                    break
        elif d == 1 or d == 3:
            for j in range(n):
                if j == nc:
                    continue
                if line_map[nr][j] != 0:
                    turn = False
                    break
        if turn:
            d = (d + 1) % 4

        cr, cc = nr, nc

player_point = [0 for _ in range(3)]
# 0: 우, 1: 아래, 2: 좌, 3: 상
def attack(d, l):
    global player_point
    global game_map
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    player_r, player_c = n//2, n//2

    for k in range(l):
        check_r, check_c = player_r + dr[d] * (k+1), player_c + dc[d] * (k+1)
        num_monster = game_map[check_r][check_c]
        if num_monster != 0:
            player_point[num_monster - 1] += 1
            game_map[check_r][check_c] = 0

def organize_line():
    global game_map

    temp_list = []
    for io in index_order:
        if game_map[io[0]][io[1]] != 0:
            temp_list.append(game_map[io[0]][io[1]])
    game_map = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(temp_list)):
        game_map[index_order[i][0]][index_order[i][1]] = temp_list[i]

def find_repeated_idx():
    global player_point
    global game_map

    check_true = False
    repeat_idx = -1
    repeated_num = 0
    for i, (cr, cc) in enumerate(index_order):
        if game_map[cr][cc] == 0:
            if repeated_num >= 4:
                check_true = True
                player_point[repeat_idx - 1] += repeated_num
                for ll in range(repeated_num):
                    remove_idx = i - (ll + 1)
                    remove_r, remove_c = index_order[remove_idx]
                    game_map[remove_r][remove_c] = 0

            repeat_idx = -1
            repeated_num = 0
            continue
        # 이전 index까지의
        if game_map[cr][cc] == repeat_idx:
            repeated_num += 1
        elif game_map[cr][cc] != repeat_idx:
            # repleat_num이 4이상인지 확인
            if repeated_num >= 4:
                check_true = True
                player_point[repeat_idx - 1] += repeated_num
                for ll in range(repeated_num):
                    remove_idx = i - (ll + 1)
                    remove_r, remove_c = index_order[remove_idx]
                    game_map[remove_r][remove_c] = 0

            repeat_idx = game_map[cr][cc]
            repeated_num = 1

    return check_true

def expand_monster():
    global game_map
    monster_list = []
    for (cr, cc) in index_order:
        if game_map[cr][cc] != 0:
            monster_list.append(game_map[cr][cc])
        else:
            break

    if len(monster_list) == 0:
        return

    new_monster_list = []
    repeat_idx = monster_list[0]
    repeat_num = 1
    for i in range(1, len(monster_list)):
        if monster_list[i] == repeat_idx:
            repeat_num += 1
        else:
            # 총 갯수, 숫자의 크기
            new_monster_list.append(repeat_num)
            new_monster_list.append(repeat_idx)
            # 새로운 것 저장
            repeat_num = 1
            repeat_idx = monster_list[i]
    new_monster_list.append(repeat_num)
    new_monster_list.append(repeat_idx)

    game_map = [[0 for _ in range(n)] for _ in range(n)]
    for k in range(min(len(new_monster_list), len(index_order))):
        game_map[index_order[k][0]][index_order[k][1]] = new_monster_list[k]





line_order()

for _ in range(m):
    attack_d, attack_l = map(int, input().split())
    attack(attack_d, attack_l)
    organize_line()
    while True:
        check_run = find_repeated_idx()
        if not check_run:
            break
        organize_line()
    expand_monster()

total_point = 0
for i in range(len(player_point)):
    total_point += (i + 1) * player_point[i]
print(total_point)