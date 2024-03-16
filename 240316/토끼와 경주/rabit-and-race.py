Q = int(input())
rabbit_d = []
q = list(map(int, input().split()))
N, M, P = q[1], q[2], q[3]
pid_d = q[4:]
for i in range(len(pid_d) // 2):
    rabbit_d.append((pid_d[2 * i + 0], pid_d[2 * i + 1]))
Q = Q - 1
rabbit_num = len(pid_d) // 2
rabbit_pos = [(0, 0) for _ in range(rabbit_num)]
rabbit_jump = [0 for _ in range(rabbit_num)]
rabbit_score = [0 for _ in range(rabbit_num)]

def pick_rabbit():
    best_idx = 0
    for rabbit_idx in range(rabbit_num):
        if rabbit_idx == 0:
            continue
        # 1. 현재까지의 총 점프 횟수가 적은 토끼
        if rabbit_jump[rabbit_idx] < rabbit_jump[best_idx]:
            best_idx = rabbit_idx
        elif rabbit_jump[rabbit_idx] == rabbit_jump[best_idx]:
            c_r, c_c = rabbit_pos[rabbit_idx]
            best_r, best_c = rabbit_pos[best_idx]
            # 2. 현재 서있는 행 번호 + 열 번호가 작은 토끼
            if c_r + c_c < best_r + best_c:
                best_idx = rabbit_idx
            # 3. 행 번호가 작은 토끼
            elif c_r + c_c == best_r + best_c:
                if c_r < best_r:
                    best_idx = rabbit_idx
                # 4. 열 번호가 작은 토끼
                elif c_r == best_r:
                    if c_c < best_c:
                        best_idx = rabbit_idx
                    elif c_c == best_c:
                        # 5. 고유 번호가 작은 토끼
                        if rabbit_d[rabbit_idx][0] < rabbit_d[best_idx][0]:
                            best_idx = rabbit_idx
    return best_idx


dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def pick_pos(r_idx):
    cr, cc = rabbit_pos[r_idx]
    jump_distance = rabbit_d[r_idx][1]
    best_r, best_c = -1, -1
    for i in range(4):
        nr, nc = cr, cc
        direction = i
        for jd in range(jump_distance):
            nr, nc = nr + dr[direction], nc + dc[direction]
            if nr < 0 or nc < 0 or nr >= N or nc >= M:
                direction = (direction + 2) % 4
                nr, nc = nr + dr[direction] * 2, nc + dc[direction] * 2
        # 1. 행 번호 + 열 번호가 큰 칸
        if nr + nc > best_r + best_c:
            best_r, best_c = nr, nc
        elif nr + nc == best_r + best_c:
            # 2.  행 번호가 큰 칸
            if nr > best_r:
                best_r, best_c = nr, nc
            elif nr == best_r:
                if nc > best_c:
                    best_r, best_c = nr, nc
    return best_r, best_c

def pick_add_s(run_list):
    best_idx = 0
    for rl in range(len(run_list)):
        if run_list[rl] != 0:
            best_idx = rl
        break
    for rabbit_idx in range(rabbit_num):
        if run_list[rabbit_idx] == 0:
            continue
        c_r, c_c = rabbit_pos[rabbit_idx]
        best_r, best_c = rabbit_pos[best_idx]
        # 1. 현재 서있는 행 번호 + 열 번호가 큰 토끼
        if c_r + c_c > best_r + best_c:
            best_idx = rabbit_idx
        # 3. 행 번호가 큰 토끼
        elif c_r + c_c == best_r + best_c:
            if c_r > best_r:
                best_idx = rabbit_idx
            # 4. 열 번호가 큰 토끼
            elif c_r == best_r:
                if c_c > best_c:
                    best_idx = rabbit_idx
                elif c_c == best_c:
                    # 5. 고유 번호가 작은 토끼
                    if rabbit_d[rabbit_idx][0] > rabbit_d[best_idx][0]:
                        best_idx = rabbit_idx
    return best_idx


for q in range(Q):
    command = list(map(int, input().split()))
    if command[0] == 200:
        K, S = command[1], command[2]
        temp_run = [0 for _ in range(rabbit_num)]
        # 경주 진행
        for _ in range(K):
            run_idx = pick_rabbit()
            next_pos = pick_pos(run_idx)
            rabbit_pos[run_idx] = next_pos
            for rs in range(len(rabbit_score)):
                if rs == run_idx:
                    continue
                # (1, 1)이 기준이라 2를 더해줘야 함
                rabbit_score[rs] += (next_pos[0] + next_pos[1] + 2)
            rabbit_jump[run_idx] += 1
            temp_run[run_idx] += 1
        add_idx = pick_add_s(temp_run)
        rabbit_score[add_idx] += S
    elif command[0] == 300:
        # 이동거리 변경
        for rd in range(rabbit_num):
            if rabbit_d[rd][0] == command[1]:
                rabbit_d[rd] = (rabbit_d[rd][0], rabbit_d[rd][1] * command[2])
                break
    elif command[0] == 400:
        print(max(rabbit_score))
        break