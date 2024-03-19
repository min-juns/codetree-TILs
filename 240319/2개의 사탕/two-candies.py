import copy
N, M = map(int, input().split())
#  #: 장애물, .: 빈칸, B: 파란색 사탕, R: 빨간색 사탕, O: 출구

game_map = [list(input()) for _ in range(N)]

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

min_num = 10
def find_min_num(num):
    global game_map
    global min_num

    if num > 10:
        return
    if num > min_num:
        return
    else:
        current_game_map = copy.deepcopy(game_map)
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
            game_map = copy.deepcopy(current_game_map)

find_min_num(0)
move_pos(0)
if min_num == 10:
    print(-1)
else:
    print(min_num)