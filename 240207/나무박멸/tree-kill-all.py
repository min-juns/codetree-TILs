n, m, k, c = map(int, input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int, input().split())))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

dk_x = [-1, -1, 1, 1]
dk_y = [1, -1, 1, -1]

no_tree = [[0 for _ in range(n)] for _ in range(n)]
total_e_tree = 0
for _ in range(m):
    # 나무 성장
    for x in range(n):
        for y in range(n):
            tree_count = 0
            if _map[x][y] > 0:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    if _map[nx][ny] > 0:
                        tree_count += 1
                _map[x][y] += tree_count

    # 나무 번식
    temp_map = [[0 for _ in range(n)] for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if _map[x][y] <= 0:
                continue

            zero_count = 0
            for d in range(4):
                if x + dx[d] < 0 or x + dx[d] >= n or y + dy[d] < 0 or y + dy[d] >= n:
                    continue
                if _map[x + dx[d]][y + dy[d]] == 0 and no_tree[x + dx[d]][y + dy[d]] == 0:
                    zero_count += 1
            if zero_count != 0:
                for d in range(4):
                    if x + dx[d] < 0 or x + dx[d] >= n or y + dy[d] < 0 or y + dy[d] >= n:
                        continue
                    if _map[x + dx[d]][y + dy[d]] == 0 and no_tree[x + dx[d]][y + dy[d]] == 0:
                        temp_map[x + dx[d]][y + dy[d]] += (_map[x][y] // zero_count)
    for x in range(n):
        for y in range(n):
            #if no_tree[x][y] == 0 and _map[x][y] == 0:
            _map[x][y] += temp_map[x][y]

    # 제초제 위치 선정
    best_x, best_y, best_tree_e_count = 0, 0, 0
    for x in range(n):
        for y in range(n):
            if _map[x][y] <= 0:
                continue
            temp_tree_e_count = _map[x][y]
            for ddk in range(4):
                for dk in range(1, k + 1):
                    nx = x + (dk_x[ddk]*dk)
                    ny = y + (dk_y[ddk]*dk)
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        break
                    if _map[nx][ny] <= 0:
                        break
                    temp_tree_e_count += _map[nx][ny]
            if best_tree_e_count < temp_tree_e_count:
                best_tree_e_count = temp_tree_e_count
                best_x = x
                best_y = y

    total_e_tree += _map[best_x][best_y]

    #제초제 살포
    if _map[best_x][best_y] > 0:
        _map[best_x][best_y] = 0
        no_tree[best_x][best_y] = c + 1

        for ddk in range(4):
            for dk in range(1, k + 1):
                nr = best_x + dk_x[ddk]*dk
                nc = best_y + dk_y[ddk]*dk
                if nr < 0 or nr >= n or nc < 0 or nc >= n:
                    break
                if _map[nr][nc] < 0:
                    break
                if _map[nr][nc] == 0:
                    no_tree[nr][nc] = c + 1
                    break
                total_e_tree += _map[nr][nc]
                _map[nr][nc] = 0
                no_tree[nr][nc] = c + 1
                """
                if _map[best_x + (dk_x[ddk]) * dk][best_y + dk_y[ddk] * dk] >= 0:
                    total_e_tree += _map[best_x + (dk_x[ddk]) * dk][best_y + dk_y[ddk] * dk]
                    _map[best_x + (dk_x[ddk]) * dk][best_y + dk_y[ddk] * dk] = 0
                    no_tree[best_x + (dk_x[ddk]) * dk][best_y + dk_y[ddk] * dk] += c + 1
                """
    for x in range(n):
        for y in range(n):
            if no_tree[x][y] != 0:
                no_tree[x][y] -= 1


print(total_e_tree)