N = int(input())
game_map = [[0 for _ in range(N)] for _ in range(N)]
like_list = [[] for _ in range(N ** 2 + 1)]
person_order = []

for _ in range(N * N):
    n0, n1, n2, n3, n4 = map(int, input().split())
    like_list[n0] = [n1, n2, n3, n4]
    person_order.append(n0)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
def select_place(p_id):
    global game_map
    p_like_list = like_list[p_id]
    best_like_friends, best_empty_space = 0, 0
    best_r, best_c = -1, -1

    for r in range(N):
        for c in range(N):
            if game_map[r][c] != 0:
                continue
            like_friends = 0
            empty_space = 0
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                if nr < 0 or nc < 0 or nr >= N or nc >= N:
                    continue
                if game_map[nr][nc] == 0:
                    empty_space += 1
                elif game_map[nr][nc] in p_like_list:
                    like_friends += 1
            if like_friends > best_like_friends:
                best_like_friends = like_friends
                best_empty_space = empty_space
                best_r, best_c = r, c
            elif like_friends == best_like_friends:
                if empty_space > best_empty_space:
                    best_empty_space = empty_space
                    best_r, best_c = r, c

    game_map[best_r][best_c] = p_id


for po in person_order:
    select_place(po)

score = [0, 1, 10, 100, 1000]
total_score = 0
for r in range(N):
    for c in range(N):
        selected_p = game_map[r][c]
        friend_list = like_list[selected_p]
        num_friend = 0
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nc < 0 or nr >= N or nc >= N:
                continue
            if game_map[nr][nc] in friend_list:
                num_friend += 1
        total_score += score[num_friend]
print(total_score)