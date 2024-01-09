n, m = map(int, input().split())

# 0 빈칸, 1 사람, 2 병원

hmap = []
for _ in range(n):
    hmap.append(list(map(int, input().split())))

human_list = []
hospital_list = []

for r in range(n):
    for c in range(n):
        if hmap[r][c] == 1:
            human_list.append((r, c))
        elif hmap[r][c] == 2:
            hospital_list.append((r, c))

hos_num = len(hospital_list)
visited = [False for _ in range(hos_num)]

def find_min():
    total_min = 0
    for hr, hc in human_list:
        min_hh = 1000000000
        for v in range(hos_num):
            if not visited[v]:
                continue
            vr, vc = hospital_list[v]
            current_min = abs(vr-hr) + abs(vc-hc)
            if min_hh > current_min:
                min_hh = current_min
        total_min += min_hh
    return total_min


min_dis = 10000000000
def find_hos(cnt, idx):
    global min_dis
    if cnt == m:
        min_dis = min(find_min(), min_dis)
        return

    for i in range(idx + 1, hos_num):
        visited[i] = True
        find_hos(cnt + 1, i)
        visited[i] = False

find_hos(0, -1)
print(min_dis)