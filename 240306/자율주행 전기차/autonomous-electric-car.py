from collections import deque
# n: 격자의 크기, m: 승객의 수, c: 초기 배터리 충전량
n, m, battery = map(int, input().split())

game_map = [list(map(int, input().split())) for _ in range(n)]
car_r, car_c = map(int, input().split())
car_r, car_c = car_r - 1, car_c - 1
customer_s = []
customer_d = []
for _ in range(m):
    a, b, c, d = map(int, input().split())
    customer_s.append([a-1, b-1])
    customer_d.append([c-1, d-1])

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def find_min_distance(s_r, s_c):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    queue = deque([(s_r, s_c)])
    visited[s_r][s_c] = 0
    while queue:
        c_r, c_c = queue.popleft()
        l = visited[c_r][c_c]
        for i in range(4):
            n_r, n_c = c_r + dr[i], c_c + dc[i]
            if n_r < 0 or n_c < 0 or n_r >= n or n_c >= n:
                continue
            if game_map[n_r][n_c] == 0 and visited[n_r][n_c] == -1:
                queue.append((n_r, n_c))
                visited[n_r][n_c] = l + 1
    return visited


def del_idx(temp_list, idx):
    t_list = temp_list[:idx]
    for i in range(len(temp_list)):
        if i > idx:
            t_list.append(temp_list[i])
    return t_list


do_break = False
while True:
    l_map = find_min_distance(car_r, car_c)
    cus_id = -1
    min_len = 1e+10
    best_r, best_c = -1, -1
    nothing = True
    if len(customer_s) != 1:
        for c in range(len(customer_s)):
            c_r, c_c = customer_s[c]
            if l_map[c_r][c_c] == -1:
                continue
            if l_map[c_r][c_c] < min_len:
                cus_id = c
                min_len = l_map[c_r][c_c]
                best_r, best_c = c_r, c_c
            elif l_map[c_r][c_c] == min_len:
                if c_r < best_r:
                    cus_id = c
                    min_len = l_map[c_r][c_c]
                    best_r, best_c = c_r, c_c
                elif c_r == best_r:
                    if c_c < best_c:
                        cus_id = c
                        min_len = l_map[c_r][c_c]
                        best_r, best_c = c_r, c_c
    elif len(customer_s) == 1:
        cus_id = 0

    if l_map[customer_s[cus_id][0]][customer_s[cus_id][0]] == -1:
        do_break = True
        break

    start_r, start_c = customer_s[cus_id]
    arrive_r, arrive_c = customer_d[cus_id]
    battery = battery - l_map[start_r][start_c]
    if battery < 0:
        do_break = True
        break
    else:
        car_r, car_c = start_r, start_c

    l2_map = find_min_distance(car_r, car_c)
    battery = battery - l2_map[arrive_r][arrive_c]
    if battery < 0:
        do_break = True
        break
    else:
        car_r, car_c = arrive_r, arrive_c
    battery = battery + l2_map[arrive_r][arrive_c] * 2

    customer_s = del_idx(customer_s, cus_id)
    customer_d = del_idx(customer_d, cus_id)
    if len(customer_s) == 0:
        break


if do_break:
    print(-1)
else:
    print(battery)