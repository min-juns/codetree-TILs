from collections import deque
# n: 격자의 크기, m: 팀의 개수, k: 라운드 수
n, m, k = map(int, input().split())
game_map = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def find_line(fr, fc):
    visited = [(fr, fc)]
    queue = deque([(fr, fc)])
    while queue:
        c_r, c_c = queue.popleft()
        current_p = game_map[c_r][c_c]
        for i in range(4):
            n_r, n_c = c_r + dr[i], c_c + dc[i]
            if n_r < 0 or n_c < 0 or n_r >= n or n_c >= n:
                continue
            if (n_r, n_c) in visited:
                continue
            if game_map[n_r][n_c] == current_p or game_map[n_r][n_c] == current_p + 1:
                queue.append((n_r, n_c))
                visited.append((n_r, n_c))
    return visited

line_list = []
for r in range(n):
    for c in range(n):
        if game_map[r][c] == 1:
            line_list.append(find_line(r, c))

person_list = []
for M in range(m):
    c_line = line_list[M]
    temp_person_pos = []
    count = 1
    for cl in c_line:
        if game_map[cl[0]][cl[1]] == 4:
            temp_person_pos.append(0)
        else:
            temp_person_pos.append(count)
            count += 1
    person_list.append(temp_person_pos)


def move_person(list_id):
    global person_list
    person_pos = person_list[list_id]

    first_p = 1e+3
    for id in range(len(person_pos)):
        if person_pos[id] == 1:
            first_p = id
            break
    num_person = len(person_pos)
    if person_pos[(first_p + 1) % num_person] == 2:
        left = True
    elif person_pos[(first_p - 1 + num_person) % num_person] == 2:
        left = False

    next_person_pos = [0 for _ in range(num_person)]
    # person_pos 상에서 왼쪽으로 움직임
    if left:
        for i in range(num_person):
            if person_pos[i] > 0:
                next_person_pos[i - 1] = person_pos[i]
    elif not left:
        for i in range(num_person):
            if person_pos[i] > 0:
                next_person_pos[(i + 1) % num_person] = person_pos[i]
    person_list[list_id] = next_person_pos

total_score = 0
def throw_ball(round_idx):
    global total_score
    global person_list
    ball_direction, idx = (round_idx // n) % 4, round_idx % n
    if ball_direction == 0:
        ball_order = [(idx, i) for i in range(n)]
    elif ball_direction == 1:
        ball_order = [(i, idx) for i in range(n-1, -1, -1)]
    elif ball_direction == 2:
        ball_order = [(n - idx - 1, i) for i in range(n-1, -1, -1)]
    elif ball_direction == 3:
        ball_order = [(i, n - idx - 1) for i in range(n)]

    # 모든 팀을 다 하기 위해
    for team_idx in range(m):
        person_pos = person_list[team_idx]
        line_order = line_list[team_idx]
        get_ball = False
        for ba in ball_order:
            if ba in line_order:
                first_idx = line_order.index(ba)
                if person_pos[first_idx] > 0:
                    # point를 얻고
                    total_score += person_pos[first_idx] ** 2
                    # 순서 바꾸기
                    temp_pos = []
                    max_num_person = max(person_pos)
                    for pp in person_pos:
                        if pp == 0:
                            temp_pos.append(pp)
                        elif pp > 0:
                            temp_pos.append(max_num_person + 1 - pp)
                    person_list[team_idx] = temp_pos
                    get_ball = True
            if get_ball:
                break

for n_round in range(k):
    for M in range(m):
        move_person(M)
    throw_ball(n_round)
print(total_score)