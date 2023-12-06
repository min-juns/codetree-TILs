"""
코드트리 조삼모사: 조합으로 풀려다가 시간 복잡도로 인해 실패
N = int(input())

work = []
for _ in range(N):
    work.append(list(map(int, input().split())))

def P(a, b):
    res = 0
    res += work[a - 1][b - 1]
    res += work[b - 1][a - 1]
    return res

def comb(comb_list, pick_num):
    res = []
    if pick_num == 0:
        return [[]]

    for i in range(len(comb_list)):
        val = comb_list[i]
        for C in comb(comb_list[i+1:], pick_num-1):
            res.append([val] + C)
    return res


poss_list = [n+1 for n in range(N)]
combi = comb(poss_list, N/2)

non_CC = []

min_val = 10000000
for CC in combi:
    not_CC = []
    for i in range(N):
        if not (i+1 in CC):
            not_CC.append(i+1)
    non_CC.append(not_CC)
    if CC in non_CC:
        continue

    pos_CC = comb(CC, 2)
    no_pos_CC = comb(not_CC, 2)

    val1 = 0
    for pos_cc in pos_CC:
        val1 += P(pos_cc[0], pos_cc[1])
    val2 = 0
    for no_pos_cc in no_pos_CC:
        val2 += P(no_pos_cc[0], no_pos_cc[1])

    if min_val > abs(val1 - val2):
        min_val = abs(val1 - val2)

print(min_val)

"""

N = int(input())
work_m = [list(map(int, input().split())) for _ in range(N)]
evening = [False for _ in range(N)]

def cal_diff():
    morning_sum = [work_m[i][j]
        for i in range(N)
        for j in range(N)
        if evening[i] == False and evening[j] == False]

    evening_sum = [work_m[i][j]
               for i in range(N)
               for j in range(N)
               if evening[i] == True and evening[j] == True]

    return abs(sum(morning_sum) - sum(evening_sum))


min_val = 10000000
def cal_c(c_idx, selected_num):
    global min_val
    if selected_num == N/2:
        min_val = min(min_val, cal_diff())
        return

    if c_idx == N:
        return

    cal_c(c_idx+1, selected_num)
    evening[c_idx] = True
    cal_c(c_idx + 1, selected_num+1)
    evening[c_idx] = False

cal_c(0, 0)
print(min_val)