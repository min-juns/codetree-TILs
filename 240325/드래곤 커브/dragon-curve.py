game_map = [[0 for _ in range(100)] for _ in range(100)]

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
max_r, max_c = 0, 0
def draw_dragon_curve(sr, sc, sd, game_g):
    global game_map
    global max_r, max_c
    game_map[sr][sc] = 1
    draw_list = []
    cr, cc = sr, sc
    cd = sd
    num_game = game_g + 1
    for _ in range(num_game):
        if len(draw_list) == 0:
            cr, cc = cr + dr[sd], cc + dc[sd]
            max_r = max(max_r, cr)
            max_c = max(max_c, cc)
            game_map[cr][cc] = 1
            draw_list.append(cd)
        else:
            num_draw = len(draw_list)
            for i in range(num_draw-1, -1, -1):
                draw_d = (draw_list[i] + 1) % 4
                cr, cc = cr + dr[draw_d], cc + dc[draw_d]
                max_r = max(max_r, cr)
                max_c = max(max_c, cc)
                game_map[cr][cc] = 1
                draw_list.append(draw_d)

n = int(input())
for _ in range(n):
    sr, sc, sd, game_g = map(int, input().split())
    draw_dragon_curve(sr, sc, sd, game_g)

res = 0
for r in range(max_r + 1):
    for c in range(max_c + 1):
        square = True
        for dr in range(2):
            for dc in range(2):
                if game_map[r + dr][c + dc] == 0:
                    square = False
        if square:
            res += 1
print(res)