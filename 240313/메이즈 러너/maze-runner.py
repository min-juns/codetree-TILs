import copy
# N: 미로의 크기, M: 참가자 수, K: 게임 시간
N, M, K = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(N)]
player_list = []

for _ in range(M):
    pr, pc = map(int, input().split())
    player_list.append((pr-1, pc-1))

e_r, e_c = map(int, input().split())
exit_pos = (e_r - 1, e_c - 1)
def distance(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

total_move = 0
def move_player():
    global player_list
    global total_move

    exit_r, exit_c = exit_pos
    for p in range(len(player_list)):
        c_r, c_c = player_list[p]
        current_distance = distance(exit_r, exit_c, c_r, c_c)
        min_distance = 1e+9
        next_step = -1
        for i in range(4):
            n_r, n_c = c_r + dr[i], c_c + dc[i]
            # 격자를 벗어나거나 벽이 있을 경우 넘어감
            if n_r < 0 or n_c < 0 or n_r >= N or n_c >= N or game_map[n_r][n_c] > 0:
                continue
            temp_distance = distance(exit_r, exit_c, n_r, n_c)
            if temp_distance < current_distance and temp_distance < min_distance:
                min_distance = temp_distance
                next_step = i

        # 적절한 다음 칸이 나올 경우
        if next_step != -1:
            total_move += 1
            next_r, next_c = c_r + dr[next_step], c_c + dc[next_step]
            player_list[p] = (next_r, next_c)

    # 출구 도달할 사람이 있을 경우 player list에서 제거

    exited_count = player_list.count(exit_pos)
    if exited_count > 0:
        for _ in range(exited_count):
            player_list.remove(exit_pos)


def find_turn_map():
    min_l = 1e+9
    best_case = (-1, -1)
    for r in range(N):
        for c in range(N):
            avail_max_l = N - max(r, c)
            if avail_max_l <= 1:
                continue
            # al이 실제 길이
            for al in range(2, avail_max_l + 1):
                find_p, find_e = False, False
                for p_list in player_list:
                    if r <= p_list[0] <= r + al - 1 and c <= p_list[1] <= c + al - 1:
                        find_p = True
                if r <= exit_pos[0] <= r + al - 1 and c <= exit_pos[1] <= c + al - 1:
                    find_e = True
                if find_p and find_e:
                    if min_l > al:
                        min_l = al
                        best_case = (r, c)

    return best_case, min_l

def turn_map():
    global game_map
    global player_list
    global exit_pos

    temp_game_map = copy.deepcopy(game_map)

    best_pos, best_l = find_turn_map()
    best_r, best_c = best_pos
    for r in range(best_r, best_r + best_l):
        for c in range(best_c, best_c + best_l):
            temp_r, temp_c = r - best_r, c - best_c
            next_r, next_c = temp_c, best_l - temp_r - 1
            next_r, next_c = next_r + best_r, next_c + best_c
            if game_map[r][c] > 0:
                temp_game_map[next_r][next_c] = game_map[r][c] - 1
            else:
                temp_game_map[next_r][next_c] = game_map[r][c]

    temp_e_r, temp_e_c = exit_pos[0] - best_r, exit_pos[1] - best_c
    next_r, next_c = temp_e_c, best_l - temp_e_r - 1
    exit_pos = (next_r + best_r, next_c + best_c)

    for p in range(len(player_list)):
        p_r, p_c = player_list[p]
        if best_r <= p_r <= best_r + best_l - 1 and best_c <= p_c <= best_c + best_l - 1:
            temp_p_r, temp_p_c = p_r - best_r, p_c - best_c
            next_r, next_c = temp_p_c, best_l - temp_p_r - 1
            player_list[p] = (next_r + best_r, next_c + best_c)
    game_map = temp_game_map


for k in range(K):
    move_player()
    if len(player_list) == 0:
        break
    turn_map()


print(total_move)
for ep in exit_pos:
    print(ep + 1, end=" ")