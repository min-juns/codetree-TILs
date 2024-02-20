from collections import deque
# n: 격자판의 크기
n = int(input())
robot_map = [list(map(int, input().split())) for _ in range(n)]

robot_r, robot_c, robot_level = 0, 0, 2
for r in range(n):
    for c in range(n):
        if robot_map[r][c] == 9:
            robot_r, robot_c = r, c
            robot_map[r][c] = 0

# 이동 룰
# 1. 1초에 상하좌우 인접한 한 칸씩 이동함
# 2. 자신의 레벨보다 큰 몬스터가 있는 칸을 지나칠 수 없음.
# 3. 나머지 칸은 모두 지날 수 있음
# 4. 전투 로봇은 자신의 레벨보다 낮은 몬스터만 없앨 수 있음.
# 5. 같은 레벨의 몬스터는 없앨 수는 없지만, 해당 칸을 지나칠 수는 있음

# 어디로 이동할 지 정하는 규칙
# 1. 없앨 수 있는 몬스터가 있으면 해당 몬스터를 없애러 간다
# 2. 없앨 수 있는 몬스터가 하나 이상이라면, 거리가 가장 가까운 몬스터를 없애러 간다.
#    --> 거리는 해당 칸으로 이동할 때 지나야하는 칸의 개수의 최소값
#    --> 가장 가까운 거리의 없앨 수 있는 몬스터가 하나 이상이면, 가장 위에 존재하는 몬스터를, 가장 위에 존재하는 몬스터가 여럿이라면,
#    --> 가장 왼쪽에 존재하는 몬스터부터 없앤다
# 3. 없앨 수 있는 몬스터가 없다면 일을 끝낸다.

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def check_distance():
    visited = [[False for _ in range(n)] for _ in range(n)]
    visit_queue = deque([(robot_r, robot_c)])
    visited[robot_r][robot_c] = 1
    while visit_queue:
        c_r, c_c = visit_queue.popleft()
        current_val = visited[c_r][c_c]
        for i in range(4):
            n_r, n_c = c_r + dr[i], c_c + dc[i]
            if n_r < 0 or n_c < 0 or n_r >= n or n_c >= n:
                continue
            if visited[n_r][n_c] == False and robot_map[n_r][n_c] <= robot_level:
                visited[n_r][n_c] = current_val + 1
                visit_queue.append((n_r, n_c))

    return visited


res = 0
eat_count = 0
while True:
    poss_list = []
    for r in range(n):
        for c in range(n):
            if robot_map[r][c] < robot_level and robot_map[r][c] != 0:
                poss_list.append([r, c])

    if len(poss_list) == 0:
        break

    temp_dis_map = check_distance()
    shortest_dis = 10000
    best_r, best_c = 100, 100
    for poss in poss_list:
        temp_r, temp_c = poss
        if temp_dis_map[temp_r][temp_c] == False:
            continue
        if shortest_dis > temp_dis_map[temp_r][temp_c]:
            shortest_dis = temp_dis_map[temp_r][temp_c]
            best_r, best_c = temp_r, temp_c

    if shortest_dis == 10000:
        break

    res += (shortest_dis - 1)
    eat_count += 1
    robot_r, robot_c = best_r, best_c
    robot_map[best_r][best_c] = 0

    if eat_count == robot_level:
        robot_level += 1
        eat_count = 0

    # 다 0으로 먹었으면 종료
    finish = True
    for r in range(n):
        for c in range(n):
            if robot_map[r][c] != 0:
                finish = False
    if finish:
        break

print(res)