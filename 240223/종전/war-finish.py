n = int(input())
hr_map = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, -1, 1, 1]
dc = [1, -1, -1, 1]

total_score = 0
for r in range(n):
    for c in range(n):
        total_score += hr_map[r][c]

# 1번 부족: 기울어진 직사각형의 경계와 그 안의 지역 (
# 2번 부족: 기울어진 직사각형의 좌측 상단 경계의 윗부분에 해당하는 지역 (위쪽 꼭짓점의 위에 있는 칸들은 포함, 왼쪽 꼭짓점은 미포함)
# 3번 부족: 기울어진 직사각형의 우측 상단 경계의 윗부분에 해당하는 지역 (오른쪽 꼭짓점의 위에 있는 칸들은 포함, 위쪽 꼭짓점은 미포함)
# 4번 부족: 기울어진 직사각형의 좌측 하단 경계의 아랫부분에 해당하는 지역 (왼쪽 꼭짓점의 위에 있는 칸들은 포함, 아랫 꼭짓점은 미포함)
# 5번 부족: 기울어진 직사각형의 우측 하단 경계의 윗부분에 해당하는 지역 (아랫쪽 꼭짓점의 위에 있는 칸들은 포함, 오른쪽 꼭짓점은 미포함)

def cal_min(pr, pc, l1, l2):
    area1, area2, area3, area4, area5 = 0, 0, 0, 0, 0
    length = l1 + l2
    # cal area 1
    area1 = area1 + hr_map[pr][pc] + hr_map[pr + dr[0] * l1 + dr[1] * l2][pc + dc[0] * l1 + dc[1] * l2]
    nc_1 = pc
    nc_2 = pc
    nr = pr
    for l in range(1, length):
        if l1 >= l:
            nc_1 += dc[0]
        elif l1 < l:
            nc_1 += dc[1]
        if l2 >= l:
            nc_2 -= 1
        elif l2 < l:
            nc_2 += 1
        nr -= 1
        for r_p1 in range(nc_2, nc_1 + 1):
            area1 += hr_map[nr][r_p1]

    # cal area 2
    p3_r, p3_c = pr + dr[0] * l1 + dr[1] * l2, pc + dc[0] * l1 + dc[1] * l2
    p4_r, p4_c = p3_r + dr[2] * l1, p3_c + dc[2] * l1

    for ar2 in range(0, p3_r):
        for ac2 in range(0, p3_c + 1):
            area2 += hr_map[ar2][ac2]

    for ar2 in range(p3_r, p4_r):
        for ac2 in range(0, p4_c):
            area2 += hr_map[ar2][ac2]

    for ar2 in range(p3_r, p4_r):
        for ac2 in range(p4_r - ar2):
            area2 += hr_map[ar2][ac2 + p4_c]

    # cal area 3
    p2_r, p2_c = pr + dr[0] * l1, pc + dc[0] * l1

    for ar3 in range(0, p3_r + 1):
        for ac3 in range(p3_c+1, n):
            area3 += hr_map[ar3][ac3]

    for ar3 in range(p3_r + 1, p2_r + 1):
        for ac3 in range(p2_c + 1, n):
            area3 += hr_map[ar3][ac3]

    for ar3 in range(p3_r + 1, p2_r):
        for ac3 in range(p2_r - ar3):
            area3 += hr_map[ar3][p2_c - ac3]

    # cal area 4
    p1_r, p1_c = pr, pc

    for ar4 in range(p4_r, n):
        for ac4 in range(0, p4_c):
            area4 += hr_map[ar4][ac4]

    for ar4 in range(p1_r, n):
        for ac4 in range(p4_c, p1_c):
            area4 += hr_map[ar4][ac4]

    for ar4 in range(p4_r + 1, p1_r):
        for ac4 in range(ar4 - p4_r):
            area4 += hr_map[ar4][p4_c + ac4]

    area5 = total_score - area1 - area2 - area3 - area4
    area = [area1, area2, area3, area4, area5]
    min_val = 10000000
    max_val = 0

    for ar in area:
        if ar < min_val:
            min_val = ar
        if ar > max_val:
            max_val = ar

    return max_val - min_val

best_min = 100000
for r in range(n):
    for c in range(n):
        length = r + 1
        if r < 2 or c < 1:
            continue
        for l1 in range(1, length):
            if c + dc[0] * l1 >= n:
                continue
            for l2 in range(1, length - l1 + 1):
                if c + dc[0] * l1 + dc[1] * l2 < 0:
                    continue
                if c - 1 * l2 < 0:
                    continue
                temp_min = cal_min(r, c, l1, l2)
                if best_min > temp_min:
                    best_min = temp_min
print(best_min)