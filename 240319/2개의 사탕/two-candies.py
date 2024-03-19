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


"""
def move_pos(d):
    global game_map
    # 오른쪽으로 기울이는 경우
    next_game_map = []
    if d == 0:
        for n in range(N):
            game_list = game_map[n]
            next_game_list = ["." for _ in range(M)]
            temp_list = []
            for m in range(M):
                if game_list[m] == "B" or game_list[m] == "R":
                    temp_list.append(game_list[m])
                elif game_list[m] == "#":
                    next_game_list[m] = "#"
                    if len(temp_list) > 0:
                        for l in range(len(temp_list)):
                            next_game_list[m - l - 1] = temp_list[-l - 1]
                        temp_list = []
                elif game_list[m] == "O":
                    next_game_list[m] = "O"
                    if len(temp_list) == 2:
                        return "fail"
                    elif len(temp_list) == 1:
                        if temp_list[0] == "R":
                            return "success"
                        else:
                            return "fail"
            next_game_map.append(next_game_list)
    # 아래로 이동
    elif d == 1:
        next_game_map = [["." for _ in range(M)] for _ in range(N)]
        for m in range(M):
            temp_list = []
            for n in range(N):
                if game_map[n][m] == "B" or game_map[n][m] == "R":
                    temp_list.append(game_map[n][m])
                elif game_map[n][m] == "#":
                    next_game_map[n][m] = "#"
                    if len(temp_list) > 0:
                        for l in range(len(temp_list)):
                            next_game_map[n - l - 1][m] = temp_list[-l - 1]
                        temp_list = []
                elif game_map[n][m] == "O":
                    next_game_map[n][m] = "O"
                    if len(temp_list) == 2:
                        return "fail"
                    elif len(temp_list) == 1:
                        if temp_list[0] == "R":
                            return "success"
                        else:
                            return "fail"
    # 왼쪽으로 이동
    elif d == 2:
        for n in range(N):
            game_list = game_map[n]
            next_game_list = ["." for _ in range(M)]
            temp_list = []
            for m in range(M-1, -1, -1):
                if game_list[m] == "B" or game_list[m] == "R":
                    temp_list.append(game_list[m])
                elif game_list[m] == "#":
                    next_game_list[m] = "#"
                    if len(temp_list) > 0:
                        for l in range(len(temp_list)):
                            next_game_list[m + l + 1] = temp_list[-l - 1]
                        temp_list = []
                elif game_list[m] == "O":
                    next_game_list[m] = "O"
                    if len(temp_list) == 2:
                        return "fail"
                    elif len(temp_list) == 1:
                        if temp_list[0] == "R":
                            return "success"
                        else:
                            return "fail"
            next_game_map.append(next_game_list)

    # 위로 이동
    elif d == 3:
        next_game_map = [["." for _ in range(M)] for _ in range(N)]
        for m in range(M):
            temp_list = []
            for n in range(N-1, -1, -1):
                if game_map[n][m] == "B" or game_map[n][m] == "R":
                    temp_list.append(game_map[n][m])
                elif game_map[n][m] == "#":
                    next_game_map[n][m] = "#"
                    if len(temp_list) > 0:
                        for l in range(len(temp_list)):
                            next_game_map[n + l + 1][m] = temp_list[-l - 1]
                        temp_list = []
                elif game_map[n][m] == "O":
                    next_game_map[n][m] = "O"
                    if len(temp_list) == 2:
                        return "fail"
                    elif len(temp_list) == 1:
                        if temp_list[0] == "R":
                            return "success"
                        else:
                            return "fail"
    game_map = next_game_map
            
    return "go"
"""

def move_pos(d):
    global red_candy
    global blue_candy
    # 오른쪽으로 기울이는 경우
    next_game_map = []
    same_pos = False
    red_first = False
    # 좌우로 움직이는 경우
    if d == 0 or d == 2:
        if red_candy[0] == blue_candy[0]:
            same_pos = True
            # 오른쪽
            if d == 0:
                if red_candy[1] > blue_candy[1]:
                    red_first = True
            elif d == 2:
                if red_candy[1] < blue_candy[1]:
                    red_first = True
    # 위아래로 움직이는 경우
    elif d == 1 or d == 3:
        if red_candy[1] == blue_candy[1]:
            same_pos = True
            if d == 1:
                if red_candy[0] > blue_candy[0]:
                    red_first = True
            elif d == 3:
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
            if res == "fail":
                return
            elif res == "success":
                if min_num > num:
                    min_num = num + 1
                    return
            elif res == "go":
                find_min_num(num + 1)
            blue_candy = copy.deepcopy(current_b_candy)
            red_candy = copy.deepcopy(current_r_candy)

"""
move_pos(1)
print(red_candy)
print(blue_candy)
print("###################")

"""
find_min_num(0)
if min_num == 10:
    print(-1)
else:
    print(min_num)