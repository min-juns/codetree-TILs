import copy
N, M = map(int, input().split())
org_chess_map = [list(map(int, input().split())) for _ in range(N)]
# direction. 0이면 r: -1, 1이면 r: +1, 2면 c:-1, 3이면 c:+1
# chess type 1: 4가지, 2: 2가지, 3: 4가지, 4: 4가지, 5: 1가지


def cal_area(chess_case_list):
    chess_map = copy.deepcopy(org_chess_map)
    list_num = len(chess_case_list)
    for num in range(list_num):
        chess_type, current_r, current_c, d = chess_case_list[num]
        dr = []
        dc = []
        if chess_type == 1:
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]
            dr = dr[d]
            dc = dc[d]
            cr = current_r
            cc = current_c
            while True:
                nr = cr + dr
                nc = cc + dc
                if nr < 0 or nc < 0 or nr >= N or nc >= M:
                    break
                if chess_map[nr][nc] == 6:
                    break
                else:
                    chess_map[nr][nc] = 1
                cr = nr
                cc = nc

        elif chess_type == 2:
            if d == 0:
                dr = [0, 0]
                dc = [-1, 1]
            elif d == 1:
                dr = [1, -1]
                dc = [0, 0]

            for i in range(2):
                cr = current_r
                cc = current_c
                while True:
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if nr < 0 or nc < 0 or nr >= N or nc >= M:
                        break
                    if chess_map[nr][nc] == 6:
                        break
                    else:
                        chess_map[nr][nc] = 2
                    cr = nr
                    cc = nc

        if chess_type == 3:
            if d == 0:
                dr = [-1, 0]
                dc = [0, 1]
            elif d == 1:
                dr = [0, 1]
                dc = [1, 0]
            elif d == 2:
                dr = [1, 0]
                dc = [0, -1]
            elif d == 3:
                dr = [0, -1]
                dc = [-1, 0]

            for i in range(2):
                cr = current_r
                cc = current_c
                while True:
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if nr < 0 or nc < 0 or nr >= N or nc >= M:
                        break
                    if chess_map[nr][nc] == 6:
                        break
                    else:
                        chess_map[nr][nc] = 3
                    cr = nr
                    cc = nc

        if chess_type == 4:
            if d == 0:
                dr = [0, -1, 0]
                dc = [-1, 0, 1]
            elif d == 1:
                dr = [-1, 0, 1]
                dc = [0, 1, 0]
            elif d == 2:
                dr = [0, 1, 0]
                dc = [1, 0, -1]
            elif d == 3:
                dr = [1, 0, -1]
                dc = [0, -1, 0]

            for i in range(3):
                cr = current_r
                cc = current_c
                while True:
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if nr < 0 or nc < 0 or nr >= N or nc >= M:
                        break
                    if chess_map[nr][nc] == 6:
                        break
                    else:
                        chess_map[nr][nc] = 4
                    cr = nr
                    cc = nc

        if chess_type == 5:
            dr = [1, 0, -1, 0]
            dc = [0, -1, 0, 1]

            for i in range(4):
                cr = current_r
                cc = current_c
                while True:
                    nr = cr + dr[i]
                    nc = cc + dc[i]
                    if nr < 0 or nc < 0 or nr >= N or nc >= M:
                        break
                    if chess_map[nr][nc] == 6:
                        break
                    else:
                        chess_map[nr][nc] = 5
                    cr = nr
                    cc = nc

    result = 0
    for n_ in range(N):
        for m_ in range(M):
            if chess_map[n_][m_] == 0:
                result += 1

    return result

###### 최솟값 구하기
chess_info = []
for n in range(N):
    for m in range(M):
        if org_chess_map[n][m] == 1:
            chess_info.append([1, n, m])
        elif org_chess_map[n][m] == 2:
            chess_info.append([2, n, m])
        elif org_chess_map[n][m] == 3:
            chess_info.append([3, n, m])
        elif org_chess_map[n][m] == 4:
            chess_info.append([4, n, m])
        elif org_chess_map[n][m] == 5:
            chess_info.append([5, n, m])

chess_case = []
min_val = 10000000000
def find_min(choose_num):
    global min_val
    if choose_num == len(chess_info):
        temp_min_val = cal_area(chess_case)
        if temp_min_val < min_val:
            min_val = temp_min_val

    else:
        c_list = chess_info[choose_num]
        if c_list[0] == 1:
            for i in range(4):
                chess_case.append([1, c_list[1], c_list[2], i])
                find_min(choose_num + 1)
                chess_case.pop()
        elif c_list[0] == 2:
            for i in range(2):
                chess_case.append([2, c_list[1], c_list[2], i])
                find_min(choose_num + 1)
                chess_case.pop()
        elif c_list[0] == 3:
            for i in range(4):
                chess_case.append([3, c_list[1], c_list[2], i])
                find_min(choose_num + 1)
                chess_case.pop()
        elif c_list[0] == 4:
            for i in range(4):
                chess_case.append([4, c_list[1], c_list[2], i])
                find_min(choose_num + 1)
                chess_case.pop()
        elif c_list[0] == 5:
            chess_case.append([5, c_list[1], c_list[2], 0])
            find_min(choose_num + 1)
            chess_case.pop()

find_min(0)
print(min_val)