from collections import deque
# n: 배지의 크기, m: 바이러스 개수, k: 사이클의 수
n, m, k = map(int, input().split())
n_map = [[5 for _ in range(n)] for _ in range(5)]
plus_n_map = [list(map(int, input().split())) for _ in range(n)]
v_map = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, age = map(int, input().split())
    v_map[r-1][c-1] = deque([age])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for t in range(k):
    # 양분 섭취
    for r in range(n):
        for c in range(n):
            virus = v_map[r][c]
            if virus != 0:
                for v in range(len(virus)):
                    # 양분 섭취할 수 있는 경우
                    if n_map[r][c] >= virus[v]:
                        n_map[r][c] -= virus[v]
                        virus[v] += 1
                    # 양분 섭취 못하는 경우 나이 = - //2 * 나이로 변경
                    else:
                        virus[v] = -(virus[v] // 2)

    # 죽은 바이러스 양분으로 변경
    for r in range(n):
        for c in range(n):
            virus = v_map[r][c]
            temp_virus = deque([])
            if virus == 0:
                continue
            for v in range(len(virus)):
                if virus[v] > 0:
                    temp_virus.append(virus[v])
                elif virus[v] < 0:
                    n_map[r][c] -= virus[v]
            if len(temp_virus) == 0:
                v_map[r][c] = 0
            else:
                v_map[r][c] = temp_virus

    # 5의 배수의 나이를 가진 바이러스 번식
    for r in range(n):
        for c in range(n):
            virus = v_map[r][c]
            if virus == 0:
                continue
            for v in range(len(virus)):
                if virus[v] % 5 == 0 and virus[v] != 0:
                    for i in range(8):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if nr < 0 or nc < 0 or nr >= n or nc >= n:
                            continue
                        if v_map[nr][nc] == 0:
                            v_map[nr][nc] = deque([1])
                        else:
                            v_map[nr][nc].appendleft(1)

    # 양분 추가
    for r in range(n):
        for c in range(n):
            n_map[r][c] += plus_n_map[r][c]

res = 0
for r in range(n):
    for c in range(n):
        if v_map[r][c] != 0:
            res += len(v_map[r][c])

print(res)