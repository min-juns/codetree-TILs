n, m = map(int, input().split())
x, y, d = map(int, input().split())

road = [list(map(int, input().split())) for _ in range(n)]
road[x][y] = 2

direction_r = [-1, 0, 1, 0]
direction_c = [0, 1, 0, -1]

run = True
visited = []
visited.append([x, y])

while run:
    current_r = visited[-1][0]
    current_c = visited[-1][1]

    do_drive = False

    for i in range(4):
        d = ((d - 1) + 4) % 4
        # step 1
        if road[current_r + direction_r[d]][current_c + direction_c[d]] == 0:
            current_r = current_r + direction_r[d]
            current_c = current_c + direction_c[d]
            road[current_r][current_c] = 2
            visited.append([current_r, current_c])
            do_drive = True
            break

    if do_drive:
        continue

    next_r = current_r - direction_r[d]
    next_c = current_c - direction_c[d]

    if road[next_r][next_c] == 1:
        run = False
    else:
        current_r = next_r
        current_c = next_c
        road[current_r][current_c] = 2
        visited.append([current_r, current_c])

count_res = 0
for r in range(n):
    for c in range(m):
        if road[r][c] == 2:
            count_res += 1

print(count_res)