import copy
game_map = []
for _ in range(4):
    # p: 죄수 id, d: 방향
    p1, d1, p2, d2, p3, d3, p4, d4 = map(int, input().split())
    game_map.append([(p1, d1-1), (p2, d2-1), (p3, d3-1), (p4, d4-1)])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

# 도둑 이동
def run_first():
    # 도둑 순서대로 정렬
    global game_map

    order_list = [(-1, -1) for _ in range(16)]
    for r in range(4):
        for c in range(4):
            p, d = game_map[r][c]
            # 경찰이면 넘기기
            if p == "P" or p == 0:
                continue
            # 1번 도둑은 0번에..... 16번 도둑은 15번에 저장
            order_list[p-1] = (r, c)
    for i in range(16):
        # 사라진 것은 pass
        if order_list[i] == (-1, -1):
            continue
        c_r, c_c = order_list[i]
        p, d = game_map[c_r][c_c]
        
        # 8방향으로 이동할 수 있는 곳 찾기
        for j in range(8):
            nd = (d + j + 8) % 8
            n_r, n_c = c_r + dr[nd], c_c + dc[nd]
            # 경찰이 있는 곳은 "P"로 표시함
            if n_r < 0 or n_c < 0 or n_r >= 4 or n_c >= 4 or game_map[n_r][n_c][0] == "P":
                continue
            # 비어있는 경우: (game_map이 (0, 0)인 경우)
            if game_map[n_r][n_c] == (0, 0):
                game_map[n_r][n_c] = (p, nd)
                order_list[i] = (n_r, n_c)
                game_map[c_r][c_c] = (0, 0)
            else:
                changed_p, changed_d = game_map[n_r][n_c]
                game_map[n_r][n_c] = (p, nd)
                game_map[c_r][c_c] = (changed_p, changed_d)
                # id-1에 값 저장
                order_list[changed_p-1] = (c_r, c_c)
                order_list[i] = (n_r, n_c)
            break
        #for gm in game_map:
        #    print(gm)
        #print("++++++++++++++++++++++++++++++++++++++")


final_score = 0
def police(score):
    global game_map
    global final_score
    for r in range(4):
        for c in range(4):
            if not isinstance(game_map[r][c], tuple):
                continue
            if game_map[r][c][0] == "P":
                police_d = game_map[r][c][1]
                police_r = r
                police_c = c

    org_game_map = copy.deepcopy(game_map)
    for l in range(3):
        n_r, n_c = police_r + dr[police_d] * (l + 1), police_c + dc[police_d] * (l + 1)
        if n_r < 0 or n_c < 0 or n_r >= 4 or n_c >= 4 or game_map[n_r][n_c] == (0, 0):
            final_score = max(final_score, score)
            continue
        id, d = game_map[n_r][n_c]
        game_map[police_r][police_c] = (0, 0)
        game_map[n_r][n_c] = ("P", d)
        run_first()
        police(score + id)
        game_map = copy.deepcopy(org_game_map)



start_score = game_map[0][0][0]
game_map[0][0] = ("P", game_map[0][0][1])
run_first()
police(start_score)

print(final_score)