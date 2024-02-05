from collections import deque
# r, c : 목표 위치, k 숫자
r, c, k = map(int, input().split())
number_map = [list(map(int, input().split())) for _ in range(3)]
temp_number_map = []
def play():
    global temp_number_map
    for R in range(len(number_map)):
        # num_val_list에 한 행마다 결과 저장해서 append
        num_val_list = []
        value_list = []
        for C in range(len(number_map[R])):
            val = number_map[R][C]
            num = number_map[R].count(val)
            # 값이 0이면 취급하지 않음
            if val == 0 or (len(num_val_list) != 0 and val in value_list):
                continue
            if len(num_val_list) == 0:
                num_val_list.append(val)
                num_val_list.append(num)
                value_list.append(val)
            else:
                for nv in range(len(num_val_list) // 2):
                    if num_val_list[nv * 2 + 1] == num:
                        if val < num_val_list[nv*2]:
                            before = num_val_list[:nv*2]
                            after = num_val_list[nv*2:]
                            num_val_list = before
                            num_val_list.append(val)
                            num_val_list.append(num)
                            value_list.append(val)
                            for num_val in after:
                                num_val_list.append(num_val)
                            break
                        else:
                            if len(num_val_list) == (nv * 2 + 2):
                                num_val_list.append(val)
                                num_val_list.append(num)
                                value_list.append(val)
                                break
                    elif num_val_list[nv*2 + 1] > num:
                        before = num_val_list[:nv*2]
                        after = num_val_list[nv*2:]
                        num_val_list = before
                        num_val_list.append(val)
                        num_val_list.append(num)
                        value_list.append(val)
                        for num_val in after:
                            num_val_list.append(num_val)
                        break
                    elif num_val_list[nv * 2 + 1] < num:
                        if len(num_val_list) == (nv * 2 + 2):
                            num_val_list.append(val)
                            num_val_list.append(num)
                            value_list.append(val)
                            break
        temp_number_map.append(num_val_list)

    TR = len(temp_number_map)
    max_c = 0
    for r_ in range(TR):
        max_c = max(max_c, len(temp_number_map[r_]))
    n_map = [[0 for _ in range(max_c)] for _ in range(TR)]
    for i in range(len(temp_number_map)):
        for j in range(len(temp_number_map[i])):
            n_map[i][j] = temp_number_map[i][j]
    temp_number_map = n_map

t = 0

def cal_t(g_map):
    global t

    t += 1
    if len(g_map) >= r and len(g_map[0]) >= c:
        if g_map[r - 1][c - 1] == k:
            return True
    if t > 100:
        return True
    return False

import sys
if number_map[r - 1][c - 1] == k:
    print(0)
    sys.exit(0)

while True:
    mr = len(number_map)
    mc = len(number_map[0])
    finish = False

    if mr > mc or mr == mc:
        play()
        finish = cal_t(temp_number_map)
        """
        print("{}##############".format(t))
        for tv in temp_number_map:
            print(tv)
        """
        if finish:
            break

    elif mr < mc:
        T_number_map = [[0 for _ in range(len(number_map))] for _ in range(len(number_map[0]))]
        for i in range(len(number_map)):
            for j in range(len(number_map[0])):
                T_number_map[j][i] = number_map[i][j]
        number_map = T_number_map
        play()
        T_number_map = [[0 for _ in range(len(temp_number_map))] for _ in range(len(temp_number_map[0]))]
        for i in range(len(temp_number_map)):
            for j in range(len(temp_number_map[0])):
                T_number_map[j][i] = temp_number_map[i][j]
        temp_number_map = T_number_map
        finish = cal_t(temp_number_map)
        """
        print("{}##############".format(t))
        for tv in temp_number_map:
            print(tv)
        """
        if finish:
            break

    max_R = min(len(temp_number_map), 100)
    max_C = min(len(temp_number_map[0]), 100)
    number_map = [[0 for _ in range(max_C)] for _ in range(max_R)]
    for mR in range(max_R):
        for mC in range(max_C):
            number_map[mR][mC] = temp_number_map[mR][mC]
    temp_number_map = []

if t > 100:
    print(-1)
else:
    print(t)