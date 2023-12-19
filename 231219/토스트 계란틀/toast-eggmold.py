from collections import deque
n, L, R = map(int, input().split())
eggs = []
for _ in range(n):
    eggs.append(list(map(int, input().split())))

visited = [[False for _ in range(n)] for _ in range(n)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    res = []
    total_val = 0
    while queue:
        cr, cc = queue.popleft()
        res.append((cr, cc))
        total_val += eggs[cr][cc]

        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if L <= abs(eggs[cr][cc] - eggs[nr][nc]) <= R and visited[nr][nc] == False:
                queue.append((nr, nc))
                visited[nr][nc] = True

    temp_res = total_val // len(res)
    for r_, c_ in res:
        eggs[r_][c_] = temp_res

    return res

count = 0
while True:
    current_res = []
    for ir in range(n):
        for ic in range(n):
            if not visited[ir][ic]:
                current_res.append(bfs(ir, ic))
    if len(current_res) == (n * n):
        break
    else:
        count += 1
        visited = [[False for _ in range(n)] for _ in range(n)]

print(count)