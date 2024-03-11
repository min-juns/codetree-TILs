# N: 게임판의 크기, M: 게임 턴 수, P: 산타의 수, C: 루돌프의 힘, D: 산타의 힘
N, M, P, C, D = map(int, input().split())
r_r, r_c = map(int, input().split())
r_pos = (r_r - 1, r_c - 1)
santa_map = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(P):
    p_id, p_r, p_c = map(int, input().split())
    santa_map[p_r - 1][p_c - 1] = p_id


def distance(r1, c1, r2, c2):
    return (r1 - r2) ** 2 + (c1 - c2) ** 2

def find_min_santa():
    min_santa, min_d, santa_pos = -1, 1000000, (-1, -1)
    ru_r, ru_c = r_pos
    for r in range(N):
        for c in range(N):
            if santa_map[r][c] != 0:
                temp_d = distance(ru_r, ru_c, r, c)
                if temp_d <= min_d:
                    min_santa = santa_map[r][c]
                    santa_pos = (r, c)
                    min_d = temp_d

    return santa_pos, min_santa


dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]
def move_rudolf():
    global r_pos
    pos, santa_id = find_min_santa()
    santa_r, santa_c = pos
    ru_r, ru_c = r_pos
    min_dis = 1000000000
    next_r, next_c = -1, -1
    best_i = -1
    for i in range(8):
        n_r, n_c = ru_r + dr[i], ru_c + dc[i]
        if n_r < 0 or n_c < 0 or n_r >= N or n_r >= N:
            continue
        temp_d = distance(santa_r, santa_c, n_r, n_c)
        if temp_d < min_dis:
            min_dis = temp_d
            next_r, next_c = n_r, n_c
            best_i = i
    r_pos = (next_r, next_c)
    return best_i


def santa_push(moved_santa, before_move_r, before_move_c, direction, power):
    global santa_map
    next_r, next_c = before_move_r + dr[direction] * power, before_move_c + dc[direction] * power

    # 칸 밖으로 나가는 경우 그냥 종료
    if next_r < 0 or next_c < 0 or next_r >= N or next_c >= N:
        return
    # 상호작용을 하는 경우
    if santa_map[next_r][next_c] != 0:
        next_santa_id = santa_map[next_r][next_c]
        santa_map[next_r][next_c] = moved_santa
        santa_push(next_santa_id, next_r, next_c, direction, 1)
    elif santa_map[next_r][next_c] == 0:
        santa_map[next_r][next_c] = moved_santa


def move_next_santa(move_id, c_r, c_c, o_d):
    global temp_santa
    n_r, n_c = c_r + santa_dr[o_d], c_c + santa_dc[o_d]
    temp_santa[move_id - 1] = (move_id, n_r, n_c)

    if n_r < 0 or n_c < 0 or n_r >= N or n_c >= N:
        return

    if santa_map[n_r][n_c] != 0:
        next_santa = santa_map[n_r][n_c]
        santa_map[n_r][n_c] = move_id
        move_next_santa(next_santa, n_r, n_c, o_d)
    # 비어있으면
    else:
        santa_map[n_r][n_c] = move_id



santa_score = [0 for _ in range(P)]
santa_stun = [0 for _ in range(P)]

santa_dr = [-1, 0, 1, 0]
santa_dc = [0, 1, 0, -1]
for m in range(M):
    rudolf_d = move_rudolf()
    ru_r, ru_c = r_pos
    # 루돌프가 움직여서 충돌이 일어난 경우 해당 산타는 C 만큼의 점수를 얻는다.
    if santa_map[ru_r][ru_c] != 0:
        selected_santa_id = santa_map[ru_r][ru_c]
        santa_score[selected_santa_id - 1] += C
        santa_map[ru_r][ru_c] = 0
        santa_stun[selected_santa_id - 1] = 2
        santa_push(selected_santa_id, ru_r, ru_c, rudolf_d, C)

    ################# 산타 이동
    temp_santa = [(-1) for _ in range(P)]
    for r in range(N):
        for c in range(N):
            santa_id = santa_map[r][c]
            if santa_id != 0:
                # 순서대로 하기 위해 temp_santa에 저장
                temp_santa[santa_id - 1] = (santa_id, r, c)

    # 루돌프 위치: ru_r, ru_c
    for ts in range(len(temp_santa)):
        # 산타가 사라진 경우
        if temp_santa[ts] == (-1):
            continue
        # 산타가 스턴맞은 경우
        if santa_stun[ts] > 0:
            continue
        
        santa_ids, santa_r, santa_c = temp_santa[ts]
        current_distance = distance(ru_r, ru_c, santa_r, santa_c)
        min_distance = 1e+10
        best_d = -1
        for i in range(4):
            next_santa_r, next_santa_c = santa_r + santa_dr[i], santa_c + santa_dc[i]
            if next_santa_r < 0 or next_santa_c < 0 or next_santa_r >= N or next_santa_c >= N:
                continue
            if santa_map[next_santa_r][next_santa_c] != 0:
                continue
            temp_distance = distance(ru_r, ru_c, next_santa_r, next_santa_c)
            if temp_distance < min_distance and temp_distance < current_distance:
                min_distance = temp_distance
                best_d = i
        # 산타가 움직이는 경우
        if best_d != -1:
            ns_r, ns_c = santa_r + santa_dr[best_d], santa_c + santa_dc[best_d]
            # 이동한 곳에 루돌프가 있는 경우엔
            if ns_r == ru_r and ns_c == ru_c:
                # score 올림
                santa_score[santa_ids - 1] += D
                # 이동 전 위치 없앰
                santa_map[santa_r][santa_c] = 0
                opposite_d = (best_d + 2) % 4
                n_ns_r, n_ns_c = ns_r + santa_dr[opposite_d] * D, ns_c + santa_dc[opposite_d] * D
                
                # 격자 벗어나면 그냥 종료
                if n_ns_r < 0 or n_ns_c < 0 or n_ns_r >= N or n_ns_c >= N:
                    continue
                # 편하게 이동할 수 있는 경우
                if santa_map[n_ns_r][n_ns_c] == 0:
                    santa_map[n_ns_r][n_ns_c] = santa_ids
                    # 산타 스턴
                    santa_stun[santa_ids - 1] = 2
                # 충돌 후 착지하는 곳에 상호작용 (santa list도 바꿔주어야 함)
                elif santa_map[n_ns_r][n_ns_c] != 0:
                    next_move_id = santa_map[n_ns_r][n_ns_c]
                    santa_map[n_ns_r][n_ns_c] = santa_ids
                    santa_stun[santa_ids - 1] = 2
                    move_next_santa(next_move_id, n_ns_r, n_ns_c, opposite_d)
            else:
                santa_map[santa_r][santa_c] = 0
                santa_map[ns_r][ns_c] = santa_ids

    game_stop = True
    for r in range(N):
        for c in range(N):
            if santa_map[r][c] != 0:
                temp_san_id = santa_map[r][c]
                santa_score[temp_san_id - 1] += 1
                game_stop = False

    if game_stop:
        break

    # 기절한 산타 깨우기
    for ss in range(len(santa_stun)):
        if santa_stun[ss] > 0:
            santa_stun[ss] = santa_stun[ss] - 1

for ss in santa_score:
    print(ss, end=" ")