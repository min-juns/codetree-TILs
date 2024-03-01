import copy
# L: map의 크기, N: 기사 개수, Q: 왕의 명령
L, N, Q = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(L)]
# r, c, w, h, k
# r, c: 위치, h: 세로 길이, w: 가로 길이, k: 초기 체력
# 1번 기사부터, N번 기사까지
hp = [0 for _ in range(N+1)]
horse_map = [[0 for _ in range(L)] for _ in range(L)]
for n in range(1, N+1):
    r, c, h, w, k = map(int, input().split())
    r, c = r - 1, c - 1
    for gr in range(r, r + h):
        for gc in range(c, c + w):
            horse_map[gr][gc] = n
    # 기사 id에 hp 저장
    hp[n] = k
initial_hp = copy.deepcopy(hp)

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
temp_horse_map = copy.deepcopy(horse_map)
def move_horse(horse_id, direction):
    global temp_horse_map
    global visited
    visited[horse_id] = True
    horse_list = []
    for r in range(L):
        for c in range(L):
            if horse_map[r][c] == horse_id:
                # 해당 id 말의 위치
                horse_list.append((r, c))
    for hl in horse_list:
        cr, cc = hl
        nr, nc = cr + dr[direction], cc + dc[direction]
        if nr < 0 or nc < 0 or nr >= L or nc >= L or game_map[nr][nc] == 2:
            return False
        if horse_map[nr][nc] == 0 or visited[horse_map[nr][nc]]:
            continue
        move_true = move_horse(horse_map[nr][nc], direction)
        if not move_true:
            return move_true
    for hl in horse_list:
        cr, cc = hl
        temp_horse_map[cr][cc] = 0
    for hl in horse_list:
        cr, cc = hl
        nr, nc = cr + dr[direction], cc + dc[direction]
        temp_horse_map[nr][nc] = horse_id
    moved_list.append(horse_id)

    return True

# 밀린 기사는 피해 X
# 움직인 기사들만 피해를 받음
def damage(attack_id):
    global total_damage
    global hp
    for r in range(L):
        for c in range(L):
            horse_id = horse_map[r][c]
            if horse_id == 0 or not (horse_id in moved_list) or horse_id == attack_id:
                continue
            if game_map[r][c] == 1:
                if hp[horse_id] > 0:
                    hp[horse_id] -= 1



for q in range(Q):
    moved_list = []
    visited = [False for _ in range(N + 1)]
    # 상 우 하 좌
    id, d = map(int, input().split())
    if hp[id] <= 0:
        continue
    moved = move_horse(id, d)
    if moved:
        horse_map = copy.deepcopy(temp_horse_map)
    else:
        temp_horse_map = copy.deepcopy(horse_map)
    if moved:
        damage(id)
        # hp가 0으로 떨어진 기사는 제외
        for hid, h in enumerate(hp):
            if h == 0 and (hid in moved_list):
                for r in range(L):
                    for c in range(L):
                        if horse_map[r][c] == hid:
                            horse_map[r][c] = 0

total_damage = 0
for i in range(len(hp)):
    if hp[i] != 0:
        total_damage += (initial_hp[i] - hp[i])
print(total_damage)