N = int(input())
game_map = [list(map(int, input().split())) for _ in range(N)]
def up(g_map):
    new_map = [[0 for _ in range(N)] for _ in range(N)]
    # 세로방향으로 모으기
    for c in range(N):
        temp_list = []
        new_list = []
        for r in range(N):
            content = g_map[r][c]
            if content != 0:
                temp_list.append(content)
        num_idx = len(temp_list)
        visited = [False for _ in range(num_idx)]
        for t in range(num_idx):
            if t != num_idx - 1:
                if temp_list[t] == temp_list[t+1] and not visited[t] and not visited[t+1]:
                    new_list.append(temp_list[t] * 2)
                    visited[t] = True
                    visited[t+1] = True
                elif not visited[t]:
                    new_list.append(temp_list[t])
            else:
                if not visited[t]:
                    new_list.append(temp_list[t])
        for r in range(N):
            if r < len(new_list):
                new_map[r][c] = new_list[r]
            else:
                new_map[r][c] = 0
    return new_map


def down(g_map):
    new_map = [[0 for _ in range(N)] for _ in range(N)]
    # 세로방향으로 모으기
    for c in range(N):
        temp_list = []
        new_list = []
        for r in range(N):
            content = g_map[r][c]
            if content != 0:
                temp_list.append(content)

        num_idx = len(temp_list)
        visited = [False for _ in range(num_idx)]
        for t in range(num_idx-1, -1, -1):
            if t != 0:
                if temp_list[t] == temp_list[t-1] and not visited[t] and not visited[t-1]:
                    new_list.append(temp_list[t] * 2)
                    visited[t] = True
                    visited[t-1] = True
                elif not visited[t]:
                    new_list.append(temp_list[t])
            else:
                if not visited[t]:
                    new_list.append(temp_list[t])

        for r in range(N):
            if r < len(new_list):
                new_map[-r-1][c] = new_list[r]
            else:
                new_map[-r-1][c] = 0
    return new_map


def left(g_map):
    new_map = [[0 for _ in range(N)] for _ in range(N)]
    # 세로방향으로 모으기
    for r in range(N):
        temp_list = []
        new_list = []
        for c in range(N):
            content = g_map[r][c]
            if content != 0:
                temp_list.append(content)
        num_idx = len(temp_list)
        visited = [False for _ in range(num_idx)]
        for t in range(num_idx):
            if t != num_idx - 1:
                if temp_list[t] == temp_list[t+1] and not visited[t] and not visited[t+1]:
                    new_list.append(temp_list[t] * 2)
                    visited[t] = True
                    visited[t+1] = True
                elif not visited[t]:
                    new_list.append(temp_list[t])
            else:
                if not visited[t]:
                    new_list.append(temp_list[t])
        for c in range(N):
            if c < len(new_list):
                new_map[r][c] = new_list[c]
            else:
                new_map[r][c] = 0
    return new_map


def right(g_map):
    new_map = [[0 for _ in range(N)] for _ in range(N)]
    # 세로방향으로 모으기
    for r in range(N):
        temp_list = []
        new_list = []
        for c in range(N):
            content = g_map[r][c]
            if content != 0:
                temp_list.append(content)

        num_idx = len(temp_list)
        visited = [False for _ in range(num_idx)]
        for t in range(num_idx-1, -1, -1):
            if t != 0:
                if temp_list[t] == temp_list[t-1] and not visited[t] and not visited[t-1]:
                    new_list.append(temp_list[t] * 2)
                    visited[t] = True
                    visited[t-1] = True
                elif not visited[t]:
                    new_list.append(temp_list[t])
            else:
                if not visited[t]:
                    new_list.append(temp_list[t])

        for c in range(N):
            if c < len(new_list):
                new_map[r][-c-1] = new_list[c]
            else:
                new_map[r][-c-1] = 0
    return new_map


def get_max(g_map):
    max_val = 0
    for r in range(N):
        for c in range(N):
            if g_map[r][c] > max_val:
                max_val = g_map[r][c]
    return max_val


def run_game(val, g_map):
    if val == 0:
        return up(g_map)
    elif val == 1:
        return down(g_map)
    elif val == 2:
        return left(g_map)
    elif val == 3:
        return right(g_map)


total_max = 0
def dfs(count, gmap):
    global total_max
    if count == 5:
        temp_val = get_max(gmap)
        total_max = max(temp_val, total_max)
        return
    else:
        for i in range(4):
            next_map = run_game(i, gmap)
            dfs(count+1, next_map)

dfs(0, game_map)
print(total_max)