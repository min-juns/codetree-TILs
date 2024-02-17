n, L = map(int, input().split())
road_map = [list(map(int, input().split())) for _ in range(n)]

def check_valid(line):
    temp_slope = [False for _ in range(n)]
    val = line[0]
    for l in range(len(line)):
        if temp_slope[l]:
            continue
        if line[l] == val:
            continue
        else:
            # 보도 블럭 큰 것에서 작은 걸로
            if line[l] - val == -1:
                temp_val = line[l]
                for s in range(L):
                    if l + s >= n:
                        return False
                    if line[l + s] != temp_val:
                        return False
                    else:
                        if temp_slope[l + s]:
                            return False
                        else:
                            temp_slope[l + s] = True
                val = temp_val
            # 보도 블럭 작은 것에서 큰 걸로..
            elif val - line[l] == -1:
                temp_val = val
                for s in range(L):
                    if l - s < 0:
                        return False
                    if line[l - s - 1] != temp_val:
                        return False
                    else:
                        if temp_slope[l - s - 1]:
                            return False
                        else:
                            temp_slope[l - s - 1] = True
                val = line[l]
            else:
                return False

    return True

res = 0
# 가로 방향에 대한 계산
for r in range(n):
    temp_line = road_map[r]
    if check_valid(temp_line):
        res += 1

# 세로 방향에 대한 계산
for c in range(n):
    temp_line = [0 for _ in range(n)]
    for tc in range(n):
        temp_line[tc] = road_map[tc][c]
    if check_valid(temp_line):
        res += 1

print(res)