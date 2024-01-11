# N: map size, M: total years
N, M = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]
med = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

dy = [1, 1, -1, -1]
dx = [-1, 1, -1, 1]

for m in range(M):
    # step 1: move
    d, p = map(int, input().split())

    for me in med:
        me[0] = (me[0] + (dr[d-1]) * p) % N
        me[1] = (me[1] + (dc[d-1]) * p) % N

    # step 2: 영양제 (+1) 성장
    for me in med:
        _map[me[0]][me[1]] += 1
        
    # step 3: 대각선
    for mr, mc in med:
        count_plus = 0
        for i in range(4):
            nr = mr + dy[i]
            nc = mc + dx[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if _map[nr][nc] >= 1:
                count_plus += 1
        _map[mr][mc] += count_plus

    new_med = []
    # step 4: 2이상 자르기 + 영양제 투입
    for r in range(N):
        for c in range(N):
            if [r, c] in med:
                continue

            if _map[r][c] >= 2:
                _map[r][c] -= 2
                new_med.append([r, c])
    med = new_med

total_res = 0
for r in range(N):
    for c in range(N):
        total_res += _map[r][c]

print(total_res)