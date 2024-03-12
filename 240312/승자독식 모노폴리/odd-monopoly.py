# n: 격자의 크기, m: 플레이어의 수, k: 독점계약 턴 수
N, M, K = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(N)]
player_d = list(map(int, input().split()))


player_priority = [[] for _ in range(M)]

for m in range(M):
    for _ in range(4):
        player_priority[m].append(list(map(int, input().split())))


for m in range(M):
    for i in range(4):
        for c in range(4):
            player_priority[m][i][c] -= 1
    player_d[m] -= 1

player_land = [[(-1, -1) for _ in range(N)] for _ in range(N)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def move_player(player_id, p_r, p_c):
    global player_d
    # 다음 위치만 넘겨주는 function
    player_plist = player_priority[player_id - 1][player_d[player_id - 1]]

    # 비어있는 칸이 있는지 확인.
    get_place = False
    for pp in player_plist:
        n_r, n_c = p_r + dr[pp], p_c + dc[pp]
        if n_r < 0 or n_c < 0 or n_r >= N or n_c >= N:
            continue
        if player_land[n_r][n_c] == (-1, -1):
            get_place = True
            player_d[player_id - 1] = pp
            break

    if not get_place:
        for pp in player_plist:
            n_r, n_c = p_r + dr[pp], p_c + dc[pp]
            if n_r < 0 or n_c < 0 or n_r >= N or n_c >= N:
                continue
            if player_land[n_r][n_c][0] == player_id:
                player_d[player_id - 1] = pp
                break

    return (n_r, n_c)


def mark_land(idx):
    for r in range(N):
        for c in range(N):
            if game_map[r][c] != 0:
                player_id = game_map[r][c]
                player_land[r][c] = (player_id, idx)


mark_land(K)
turn = 0
while True:
    turn += 1
    next_game_map = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if game_map[r][c] != 0:
                p_id = game_map[r][c]
                next_r, next_c = move_player(p_id, r, c)
                if next_game_map[next_r][next_c] == 0:
                    next_game_map[next_r][next_c] = p_id
                elif next_game_map[next_r][next_c] != 0:
                    if next_game_map[next_r][next_c] > p_id:
                        next_game_map[next_r][next_c] = p_id
    game_map = next_game_map
    mark_land(K+1)

    #### 독점 계약 turn 감소
    for r in range(N):
        for c in range(N):
            if player_land[r][c] != (-1, -1):
                land_id, d = player_land[r][c]
                # 마지막 1턴이었으면
                if d == 1:
                    player_land[r][c] = (-1, -1)
                elif d > 1:
                    player_land[r][c] = (land_id, d - 1)

    finish = True
    for r in range(N):
        for c in range(N):
            if game_map[r][c] > 1:
                finish = False
    if finish:
        break

    if turn >= 1000:
        turn = -1
        break

print(turn)