import copy
N = int(input())
game_map = [list(map(int, input().split())) for _ in range(N)]
def up():
    global game_map
    # 세로방향으로 모으기
    for c in range(N):
        temp_list = []
        new_list = []
        for r in range(N):
            content = game_map[r][c]
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
                game_map[r][c] = new_list[r]
            else:
                game_map[r][c] = 0


def down():
    global game_map
    # 세로방향으로 모으기
    for c in range(N):
        temp_list = []
        new_list = []
        for r in range(N):
            content = game_map[r][c]
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
                game_map[-r-1][c] = new_list[r]
            else:
                game_map[-r-1][c] = 0


def left():
    global game_map
    # 세로방향으로 모으기
    for r in range(N):
        temp_list = []
        new_list = []
        for c in range(N):
            content = game_map[r][c]
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
                game_map[r][c] = new_list[c]
            else:
                game_map[r][c] = 0


def right():
    global game_map
    # 세로방향으로 모으기
    for r in range(N):
        temp_list = []
        new_list = []
        for c in range(N):
            content = game_map[r][c]
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
                game_map[r][-c-1] = new_list[c]
            else:
                game_map[r][-c-1] = 0


def get_max():
    max_val = 0
    for r in range(N):
        for c in range(N):
            if game_map[r][c] > max_val:
                max_val = game_map[r][c]
    return max_val


def run_game(val):
    if val == 0:
        up()
    elif val == 1:
        down()
    elif val == 2:
        left()
    elif val == 3:
        right()


total_max = 0
def dfs(count):
    global total_max
    global game_map
    if count == 5:
        temp_val = get_max()
        total_max = max(temp_val, total_max)
        return
    else:
        temp_map = copy.deepcopy(game_map)
        for i in range(4):
            run_game(i)
            dfs(count+1)
            game_map = temp_map

dfs(0)
print(total_max)