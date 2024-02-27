from collections import deque
import copy

n = int(input())
game_map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def find_group(cr, cc, number):
    global visited
    queue = deque([])
    queue.append((cr, cc))
    val = game_map[cr][cc]
    visited[cr][cc] = str(number)

    while queue:
        tr, tc = queue.popleft()
        for i in range(4):
            nr, nc = tr + dr[i], tc + dc[i]
            if nr < 0 or nc < 0 or nr >= n or nc >= n:
                continue
            if game_map[nr][nc] == val and visited[nr][nc] == False:
                queue.append((nr, nc))
                visited[nr][nc] = str(number)


def make_group():
    count = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                find_group(r, c, count)
                count += 1

def turn_square(g_m, sr, sc, length):
    for k in range(length // 2):
        cr, cc = sr + k, sc + k
        cl = length - 2 * k
        temp_list = []
        for l in range(cl):
            temp_list.append(g_m[cr][cc+l])
        for l in range(cl-1):
            temp_list.append(g_m[cr+1+l][cc+cl-1])
        for l in range(cl-1):
            temp_list.append(g_m[cr+cl-1][cc+cl-2-l])
        for l in range(cl-2):
            temp_list.append(g_m[cr+cl-2-l][cc])

        count = 0
        for l in range(cl):
            g_m[cr+l][cc+cl-1] = temp_list[count]
            count += 1
        for l in range(cl-1):
            g_m[cr+cl-1][cc+cl-2-l] = temp_list[count]
            count += 1
        for l in range(cl-1):
            g_m[cr+cl-2-l][cc] = temp_list[count]
            count += 1
        for l in range(cl-2):
            g_m[cr][cc+1+l] = temp_list[count]
            count += 1

    return g_m

def turn_map():
    global game_map
    temp_g_map = copy.deepcopy(game_map)
    m = n // 2
    g_list = []
    for i in range(m):
        g_list.append(game_map[i][m])
    for i in range(m):
        g_list.append(game_map[m][-1-i])
    for i in range(m):
        g_list.append(game_map[-1-i][m])
    for i in range(m):
        g_list.append(game_map[m][i])

    c = 0
    for i in range(m):
        temp_g_map[m][i] = g_list[c]
        c += 1
    for i in range(m):
        temp_g_map[i][m] = g_list[c]
        c += 1
    for i in range(m):
        temp_g_map[m][-1-i] = g_list[c]
        c += 1
    for i in range(m):
        temp_g_map[-1-i][m] = g_list[c]
        c += 1

    for kr in range(2):
        for kc in range(2):
            temp_g_map = turn_square(temp_g_map, 0 + (m + 1) * kr, 0 + (m + 1) * kc, m)

    game_map = temp_g_map

comb_result = []
def get_comb(num, avail_list, c_list):
    global comb_result
    if num == 2:
        return c_list
    elif num < 2 and len(avail_list) == 0:
        return
    if num < 2:
        for i in range(len(avail_list)):
            res = get_comb(num+1, avail_list[i+1:], c_list + [avail_list[i]])
            if res:
                comb_result.append(res)

def get_res():
    num_len = 0
    for r in range(n):
        for c in range(n):
            if int(visited[r][c]) > num_len:
                num_len = int(visited[r][c])

    num_number = [0 for _ in range(num_len+1)]
    for r in range(n):
        for c in range(n):
            num_number[int(visited[r][c])] += 1

    real_number = [0 for _ in range(num_len+1)]
    for r in range(n):
        for c in range(n):
            num_index = int(visited[r][c])
            real_number[num_index] = game_map[r][c]

    ava_list = [i for i in range(num_len+1)]
    get_comb(0, ava_list, [])

    total_res = 0
    for cr in comb_result:
        num_line = 0
        for r in range(n):
            for c in range(n):
                if visited[r][c] == str(cr[0]):
                    for i in range(4):
                        nr = r + dr[i]
                        nc = c + dc[i]
                        if nr < 0 or nc < 0 or nr >= n or nc >= n:
                            continue
                        if visited[nr][nc] == str(cr[1]):
                            num_line += 1
        if num_line > 0:
            total_res += ((num_number[cr[0]] + num_number[cr[1]]) * real_number[cr[0]] * real_number[cr[1]]
                          * num_line)
    return total_res


result = 0
for turn in range(4):
    # 분할한 그룹 --> visited에 저장
    make_group()
    result += get_res()
    #print(get_res())
    visited = [[False for _ in range(n)] for _ in range(n)]
    comb_result = []
    turn_map()
print(result)