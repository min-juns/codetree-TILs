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
"""
for c in combi:
    temp_list = []
    for i in range(N):
        if not (i+1 in c):
            temp_list.append(i+1)
    if temp_list in combi:
        combi.pop(combi.index(temp_list))
"""
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