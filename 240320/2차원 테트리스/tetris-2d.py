k = int(input())

yellow_map = [[0 for _ in range(4)] for _ in range(6)]
red_map = [[0 for _ in range(6)] for _ in range(4)]
total_point = 0
def put_yellow(num_type, pos_c):
    global yellow_map
    put_r_num = 1e-3
    if num_type == 1 or num_type == 3:
        for r in range(6):
            if yellow_map[r][pos_c] == 1:
                put_r_num = r - 1
                break
        else:
            put_r_num = 5
    elif num_type == 2:
        for r in range(6):
            if yellow_map[r][pos_c] == 1:
                put_r_num = r - 1
                break
            elif yellow_map[r][pos_c + 1] == 1:
                put_r_num = r - 1
                break
        else:
            put_r_num = 5

    if num_type == 1:
        yellow_map[put_r_num][pos_c] = 1
    elif num_type == 2:
        yellow_map[put_r_num][pos_c] = 1
        yellow_map[put_r_num][pos_c + 1] = 1
    elif num_type == 3:
        yellow_map[put_r_num][pos_c] = 1
        yellow_map[put_r_num - 1][pos_c] = 1

def remove_line_yellow(remove_r):
    global yellow_map
    next_yellow_map = [[0 for _ in range(4)] for _ in range(6)]
    for c in range(4):
        for r in range(5, -1, -1):
            if r == remove_r:
                continue
            elif r > remove_r:
                if yellow_map[r][c] == 1:
                    next_yellow_map[r][c] = 1
            else:
                if yellow_map[r][c] == 1:
                    next_yellow_map[r+1][c] = 1
    yellow_map = next_yellow_map

def check_remove_yellow():
    global total_point
    while True:
        for r in range(5, 1, -1):
            if yellow_map[r] == [1, 1, 1, 1]:
                total_point += 1
                remove_line_yellow(r)
        else:
            break

    check_times = 0
    for r in range(2):
        for c in range(4):
            if yellow_map[r][c] == 1:
                if r == 0:
                    check_times = 2
                if r == 1:
                    check_times = max(check_times, r)

    for _ in range(check_times):
        remove_line_yellow(5)


def put_red(num_type, pos_r):
    global red_map
    put_c_num = 1e-3
    if num_type == 1 or num_type == 2:
        for c in range(6):
            if red_map[pos_r][c] == 1:
                put_c_num = c - 1
                break
        else:
            put_c_num = 5
    elif num_type == 3:
        for c in range(6):
            if red_map[pos_r][c] == 1:
                put_c_num = c - 1
                break
            elif red_map[pos_r + 1][c] == 1:
                put_c_num = c - 1
                break
        else:
            put_c_num = 5

    if num_type == 1:
        red_map[pos_r][put_c_num] = 1
    elif num_type == 2:
        red_map[pos_r][put_c_num] = 1
        red_map[pos_r][put_c_num - 1] = 1
    elif num_type == 3:
        red_map[pos_r][put_c_num] = 1
        red_map[pos_r + 1][put_c_num] = 1

def remove_line_red(remove_c):
    global red_map
    next_red_map = [[0 for _ in range(6)] for _ in range(4)]
    for r in range(4):
        for c in range(5, -1, -1):
            if c == remove_c:
                continue
            elif c > remove_c:
                if red_map[r][c] == 1:
                    next_red_map[r][c] = 1
            else:
                if red_map[r][c] == 1:
                    next_red_map[r][c+1] = 1
    red_map = next_red_map

def check_remove_red():
    global total_point
    while True:
        anything = True
        for c in range(5, 1, -1):
            check = True
            for r in range(4):
                if red_map[r][c] == 0:
                    check = False
            if check:
                total_point += 1
                anything = False
                remove_line_red(c)
        # 뭔가 하나라도 돌아갔으면 다시 돌리기
        if anything:
            break

    check_times = 0
    for c in range(2):
        for r in range(4):
            if red_map[r][c] == 1:
                if c == 0:
                    check_times = 2
                if c == 1:
                    check_times = max(check_times, c)

    for _ in range(check_times):
        remove_line_red(5)



for _ in range(k):
    t, x, y = map(int, input().split())
    put_yellow(t, y)
    check_remove_yellow()
    put_red(t, x)
    check_remove_red()

print(total_point)

left_blocks = 0
for i in range(4):
    for j in range(6):
        if yellow_map[j][i] == 1:
            left_blocks += 1
        if red_map[i][j] == 1:
            left_blocks += 1
print(left_blocks)