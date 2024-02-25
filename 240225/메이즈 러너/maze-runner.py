import math
from collections import deque

N, M, K = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(N)]

location = []
for m in range(M):
    r, c = map(int, input().split())
    location.append([r-1, c-1])
location = deque(location)

exit_r, exit_c = map(int, input().split())
exit_r -= 1
exit_c -= 1
_map[exit_r][exit_c] = "exit"

def out_range(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return False
    else:
        return True

def rotation(lt_r, lt_c, rb_r, rb_c, length):
    global _map
    temp_o = deque()
    for l in range(length):
        temp_o.append(_map[lt_r][lt_c + l])
    for l in range(length-1):
        temp_o.append(_map[lt_r+l+1][rb_c])
    for l in range(length-1):
        temp_o.append(_map[rb_r][rb_c-1-l])
    for l in range(length-2):
        temp_o.append(_map[rb_r-1-l][lt_c])

    temp_t = 0
    temp_o.rotate((length-1))
    for l in range(length):
        _map[lt_r][lt_c + l] = temp_o[temp_t]
        temp_t += 1
    for l in range(length-1):
        _map[lt_r+l+1][rb_c] = temp_o[temp_t]
        temp_t += 1
    for l in range(length-1):
        _map[rb_r][rb_c-1-l] = temp_o[temp_t]
        temp_t += 1
    for l in range(length-2):
        _map[rb_r-1-l][lt_c] = temp_o[temp_t]
        temp_t += 1

total_move = 0
for k in range(K):
    temp_escape = []
    # 참가자 이동
    for l in range(len(location)):
        c_move = True
        p_r, p_c = location[l][0], location[l][1]
        if exit_r > p_r:
            if _map[p_r + 1][p_c] == 0 or _map[p_r + 1][p_c] == "exit":
                location[l][0] = p_r+1
                location[l][1] = p_c
                total_move += 1
                if p_r + 1 == exit_r and p_c == exit_c:
                    temp_escape.append(l)
                c_move = False
        elif exit_r < p_r:
            if _map[p_r-1][p_c] == 0 or _map[p_r-1][p_c] == "exit":
                location[l][0] = p_r-1
                location[l][1] = p_c
                total_move += 1
                if p_r - 1 == exit_r and p_c == exit_c:
                    temp_escape.append(l)
                c_move = False
        if c_move:
            if exit_c > p_c:
                if _map[p_r][p_c+1] == 0 or _map[p_r][p_c+1] == "exit":
                    location[l][0] = p_r
                    location[l][1] = p_c+1
                    total_move += 1
                    if p_r == exit_r and p_c + 1 == exit_c:
                        temp_escape.append(l)
            elif exit_c < p_c:
                if _map[p_r][p_c - 1] == 0 or _map[p_r][p_c - 1] == "exit":
                    location[l][0] = p_r
                    location[l][1] = p_c - 1
                    total_move += 1
                    if p_r == exit_r and p_c - 1 == exit_c:
                        temp_escape.append(l)

    # 도망 완료
    temp_location = []
    if len(temp_escape) > 0:
        for i in range(len(location)):
            if i not in temp_escape:
                temp_location.append(location[i])
        location = deque(temp_location)
    if len(location) == 0:
        break

    # 회전 사각형 구하기
    left_top_r, left_top_c = 0, 0
    right_bottom_r, right_bottom_c = 0, 0
    max_rc = int(max(math.fabs(N-exit_r-1), exit_r, math.fabs(N-exit_c-1), exit_c))

    get_value = False
    for i in range(1, N+1):
        for n_r in range(N-1-i):
            for n_c in range(N-1-i):
                if n_r <= exit_r <= n_r + i and n_c <= exit_c <= n_c + i:
                    for l in location:
                        if n_r <= l[0] <= n_r + i and n_c <= l[1] <= n_c + i:
                            left_top_r = n_r
                            left_top_c = n_c
                            right_bottom_r = n_r + i
                            right_bottom_c = n_c + i
                            get_value = True
                            break
                if get_value:
                    break
            if get_value:
                break
        if get_value:
            break

    # rotation
    # 인간들 -이동 수 -1로 넣기
    for i in range(len(location)):
        _map[location[0][0]][location[0][1]] = "human"
        location.popleft()
    l_length = (right_bottom_r - left_top_r + 1) // 2


    # left_top_r, left_top_c, right_bottom_r, right_bottom_c
    for r in range(left_top_r, right_bottom_r + 1):
        for c in range(left_top_c, right_bottom_c + 1):
            if isinstance(_map[r][c], int) and _map[r][c] > 0:
                _map[r][c] -= 1

    for kk in range(l_length):
        rotation(left_top_r+kk, left_top_c+kk, right_bottom_r-kk, right_bottom_c-kk, (right_bottom_r - left_top_r + 1) - (2 * kk))

    # 인간 + 출구 다시 넣기
    for r in range(N):
        for c in range(N):
            if isinstance(_map[r][c], int) and _map[r][c] < 0:
                location.append([r, c, -_map[r][c] + 1])
                _map[r][c] = 0
            elif isinstance(_map[r][c], str) and _map[r][c] == "exit":
                exit_r = r
                exit_c = c
            elif isinstance(_map[r][c], str) and _map[r][c] == "human":
                location.append([r, c])
                _map[r][c] = 0
    """
    for m in _map:
        print(m)
    print(location)
    print("-------0*************------------------")

    print("-------------------------")
    """
print(total_move)
print(exit_r+1, exit_c+1)