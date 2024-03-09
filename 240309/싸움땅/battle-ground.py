# n: 격자의 크기, m: 플레이어의 수, k: 라운드 수
N, M, K = map(int, input().split())
gun_map = [list(map(int, input().split())) for _ in range(N)]
for r in range(N):
    for c in range(N):
        gun_map[r][c] = [gun_map[r][c]]

player_idx = [(-1, -1) for _ in range(M)]
player_gun = [0 for _ in range(M)]
player_d = [-1 for _ in range(M)]
player_str = [0 for _ in range(M)]
for m in range(M):
    x, y, d, s = map(int, input().split())
    player_idx[m] = (x-1, y-1)
    player_d[m] = d
    player_str[m] = s

def del_idx(clist, idx):
    temp_list = clist[:idx]
    for k in range(len(clist)):
        if k > idx:
            temp_list.append(clist[k])
    return temp_list

def get_gun(p_id, p_r, p_c):
    global player_gun
    global gun_map
    gun_list = gun_map[p_r][p_c]
    # 플레이어한테 총이 없는 경우
    if player_gun[p_id] == 0:
        # 해당 map에 총이 있는 경우
        if len(gun_list) >= 1:
            max_idx, max_gun = -1, -1
            for gun_idx in range(len(gun_list)):
                if max_gun < gun_list[gun_idx]:
                    max_idx = gun_idx
                    max_gun = gun_list[gun_idx]
            player_gun[p_id] = max_gun
            gun_map[p_r][p_c] = del_idx(gun_list, max_idx)
    else:
        if len(gun_list) >= 1:
            max_idx, max_gun = -1, -1
            for gun_idx in range(len(gun_list)):
                if max_gun < gun_list[gun_idx]:
                    max_idx = gun_idx
                    max_gun = gun_list[gun_idx]
            # 리스트의 총의 공격력이 플레이어가 가진 총보다 클 경우엔
            if player_gun[p_id] < max_gun:
                current_gun = player_gun[p_id]
                player_gun[p_id] = max_gun
                gun_list = del_idx(gun_list, max_idx)
                gun_list.append(current_gun)
                gun_map[p_r][p_c] = gun_list

total_point = [0 for _ in range(M)]
def who_win(first_idx, second_idx):
    # 진 사람이 True임
    global total_point
    first_player, second_player = False, False
    if player_str[first_idx] + player_gun[first_idx] > player_str[second_idx] + player_gun[second_idx]:
        second_player = True
    elif player_str[first_idx] + player_gun[first_idx] < player_str[second_idx] + player_gun[second_idx]:
        first_player = True
    elif player_str[first_idx] + player_gun[first_idx] == player_str[second_idx] + player_gun[second_idx]:
        if player_str[first_idx] > player_str[second_idx]:
            second_player = True
        elif player_str[second_idx] > player_str[first_idx]:
            first_player = True

    if first_player:
        total_point[second_idx] += player_str[second_idx] + player_gun[second_idx] - player_str[first_idx] - player_gun[first_idx]
    if second_player:
        total_point[first_idx] += player_str[first_idx] + player_gun[first_idx] - player_str[second_idx] - player_gun[second_idx]
    #print(first_idx, second_idx)
    #print("score: ", player_str[second_idx], player_gun[second_idx], player_str[first_idx], player_gun[first_idx])
    return (first_player, second_player)


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
def player_move(p_idx, dest_r, dest_c):
    global player_idx
    global player_d
    global gun_map
    # 다음 공간에 다른 player가 없는 경우, 총을 줍거나 혹은 줍지 않는다.
    fight = False
    fight_id = -1
    for kk in range(len(player_idx)):
        if (dest_r, dest_c) == player_idx[kk]:
            fight = True
            fight_id = kk
            break
    if not fight:
        get_gun(p_idx, dest_r, dest_c)
        player_idx[p_idx] = (dest_r, dest_c)
    else:
        # 이동한 사람: first player, # 기존에 있던 사람 second_player
        # True 면 진거임
        first_player, second_player = who_win(p_idx, fight_id)
        # 기존에 있던 사람이 진 경우, 기존 사람 이동 + 진 사람 다시 이동
        if second_player:
            # 이동한 사람의 위치 조정
            player_idx[p_idx] = (dest_r, dest_c)
            # 기존에 있던 플레이어는 총을 해당 격자에 내려놓고 이동.
            if player_gun[fight_id] != 0:
                lose_gun = player_gun[fight_id]
                player_gun[fight_id] = 0
                gun_map[dest_r][dest_c].append(lose_gun)

            for i in range(4):
                real_d = (player_d[fight_id] + i) % 4
                nnr, nnc = dest_r + dr[real_d], dest_c + dc[real_d]
                if nnr < 0 or nnr >= N or nnc < 0 or nnc >= N:
                    continue
                if (nnr, nnc) in player_idx:
                    continue
                break
            player_d[fight_id] = real_d
            player_move(fight_id, nnr, nnc)
            # 이긴 플레이어는 승리한 칸에 떨어져 있는 총과 들고있던 총 중 높은 것 선택
            get_gun(p_idx, dest_r, dest_c)
        # 이동한 사람이 진 경우
        if first_player:
            player_idx[p_idx] = (dest_r, dest_c)
            if player_gun[p_idx] != 0:
                lose_gun = player_gun[p_idx]
                player_gun[p_idx] = 0
                gun_map[dest_r][dest_c].append(lose_gun)
            next_d = player_d[p_idx]
            for i in range(4):
                real_d = (next_d + i) % 4
                nnr, nnc = dest_r + dr[real_d], dest_c + dc[real_d]
                if nnr < 0 or nnc < 0 or nnr >= N or nnc >= N:
                    continue
                if (nnr, nnc) in player_idx:
                    continue
                break
            player_d[p_idx] = real_d
            #player_idx[fight_id] = (dest_r, dest_c)
            player_move(p_idx, nnr, nnc)
            # 이긴 플레이어는 승리한 칸에 떨어져 있는 총과 들고있던 총 중 높은 것 선택
            get_gun(fight_id, dest_r, dest_c)


for k in range(K):
    for current_M in range(M):
        cr, cc = player_idx[current_M]
        p_d = player_d[current_M]
        nr, nc = cr + dr[p_d], cc + dc[p_d]
        if nr < 0 or nc < 0 or nr >= N or nc >= N:
            p_d = (p_d + 2) % 4
            player_d[current_M] = p_d
            nr, nc = cr + dr[p_d], cc + dc[p_d]
        player_move(current_M, nr, nc)
for tp in total_point:
    print(tp, end=" ")