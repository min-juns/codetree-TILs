import copy
N, M = map(int, input().split())
#  #: 장애물, .: 빈칸, B: 파란색 사탕, R: 빨간색 사탕, O: 출구
game_map = [list(input()) for _ in range(N)]
for n in range(N):
    for m in range(M):
        if game_map[n][m] == "R":
            red_candy = (n, m)
        elif game_map[n][m] == "B":
            blue_candy = (n, m)

def move_pos(d):
    global red_candy
    global blue_candy
    # 오른쪽으로 기울이는 경우
    same_pos = False
    red_first = False
    # 좌우로 움직이는 경우
    if d == 0 or d == 2:
        if red_candy[0] == blue_candy[0]:
            same_pos = True
            # 오른쪽
            if d == 0:
                for k in range(min(red_candy[1], blue_candy[1]), max(red_candy[1], blue_candy[1]) + 1):
                    if game_map[red_candy[0]][k] == "#" or game_map[red_candy[0]][k] == "O":
                        same_pos = False
                if same_pos:
                    if red_candy[1] > blue_candy[1]:
                        red_first = True
            elif d == 2:
                for k in range(min(red_candy[1], blue_candy[1]), max(red_candy[1], blue_candy[1]) + 1):
                    if game_map[red_candy[0]][k] == "#" or game_map[red_candy[0]][k] == "O":
                        same_pos = False
                if same_pos:
                    if red_candy[1] < blue_candy[1]:
                        red_first = True
    # 위아래로 움직이는 경우
    elif d == 1 or d == 3:
        if red_candy[1] == blue_candy[1]:
            same_pos = True
            if d == 1:
                for k in range(min(red_candy[0], blue_candy[0]), max(red_candy[0], blue_candy[0]) + 1):
                    if game_map[k][red_candy[1]] == "#" or game_map[k][red_candy[1]] == "O":
                        same_pos = False
                if same_pos:
                    if red_candy[0] > blue_candy[0]:
                        red_first = True
            elif d == 3:
                for k in range(min(red_candy[0], blue_candy[0]), max(red_candy[0], blue_candy[0]) + 1):
                    if game_map[k][red_candy[1]] == "#" or game_map[k][red_candy[1]] == "O":
                        same_pos = False
                if same_pos:
                    if red_candy[0] < blue_candy[0]:
                        red_first = True

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    if not same_pos:
        r_r, r_c = red_candy
        for i in range(10):
            n_r = r_r + dr[d]
            n_c = r_c + dc[d]
            if game_map[n_r][n_c] == "#":
                red_candy = (r_r, r_c)
                break
            elif game_map[n_r][n_c] == "O":
                return "success"
            else:
                r_r, r_c = n_r, n_c

        b_r, b_c = blue_candy
        for i in range(10):
            n_r = b_r + dr[d]
            n_c = b_c + dc[d]
            if game_map[n_r][n_c] == "#":
                blue_candy = (b_r, b_c)
                break
            elif game_map[n_r][n_c] == "O":
                return "fail"
            else:
                b_r, b_c = n_r, n_c

    else:
        if red_first:
            r_r, r_c = red_candy
            for i in range(10):
                n_r = r_r + dr[d]
                n_c = r_c + dc[d]
                if game_map[n_r][n_c] == "#":
                    red_candy = (r_r, r_c)
                    blue_candy = (r_r - dr[d], r_c - dc[d])
                    break
                elif game_map[n_r][n_c] == "O":
                    return "fail"
                else:
                    r_r, r_c = n_r, n_c
        else:
            r_r, r_c = blue_candy
            for i in range(10):
                n_r = r_r + dr[d]
                n_c = r_c + dc[d]
                if game_map[n_r][n_c] == "#":
                    blue_candy = (r_r, r_c)
                    red_candy = (r_r - dr[d], r_c - dc[d])
                    break
                elif game_map[n_r][n_c] == "O":
                    return "fail"
                else:
                    r_r, r_c = n_r, n_c
    return "go"


min_num = 10
def find_min_num(num):
    global min_num
    global blue_candy
    global red_candy

    if num >= 10:
        return
    if num >= min_num:
        return
    else:
        current_b_candy = copy.deepcopy(blue_candy)
        current_r_candy = copy.deepcopy(red_candy)
        for i in range(4):
            res = move_pos(i)
            if res == "success":
                if min_num > num:
                    min_num = num + 1
                    return
            elif res == "go":
                find_min_num(num + 1)
            blue_candy = copy.deepcopy(current_b_candy)
            red_candy = copy.deepcopy(current_r_candy)

find_min_num(0)
if min_num == 10:
    print(-1)
else:
    print(min_num)