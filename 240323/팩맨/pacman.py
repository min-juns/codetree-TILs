import copy
# 한 칸은 4
m, t = map(int, input().split())
pack_r, pack_c = map(int, input().split())
pack_r, pack_c = pack_r - 1, pack_c - 1

monsters = []
for _ in range(m):
    r, c, d = map(int, input().split())
    monsters.append((r-1, c-1, d-1))

# 몬스터 알
eggs = []

def monster_copy():
    global eggs
    eggs = copy.deepcopy(monsters)

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
def move_monster():
    global monsters

    for ml in range(len(monsters)):
        mr, mc, md = monsters[ml]
        moved = False
        for i in range(8):
            d = (md + i) % 8
            nr, nc = mr + dr[d], mc + dc[d]
            # 격자 밖으로 나가면 다시
            if nr < 0 or nc < 0 or nr >= 4 or nc >= 4:
                continue
            # 팩맨이 있으면 다시
            if nr == pack_r and nc == pack_c:
                continue
            for dm in dead_monster[0]:
                if dm == (nr, nc):
                    continue
            for dm in dead_monster[1]:
                if dm == (nr, nc):
                    continue
            moved = True
            next_contents = (nr, nc, d)
            break
        if moved:
            monsters[ml] = next_contents

# 몬스터 사체
dead_monster = [[],[],[]]

dr_pack = [-1, 0, 1, 0]
dc_pack = [0, -1, 0, 1]
best_eat = -1
best_direction = []
def move_pack(direction, pack_pos, eat_count):
    global monsters
    global best_eat
    global best_direction
    if len(direction) >= 3:
        if best_eat < eat_count:
            best_eat = eat_count
            best_direction = direction
    else:
        current_r, current_c = pack_pos
        original_monsters = copy.deepcopy(monsters)
        for i in range(4):
            nr, nc = current_r + dr_pack[i], current_c + dc_pack[i]
            if nr < 0 or nc < 0 or nr >= 4 or nc >= 4:
                continue
            next_eat_count = eat_count
            del_list = []
            for mk in range(len(monsters)):
                if monsters[mk][0] == nr and monsters[mk][1] == nc:
                    next_eat_count += 1
                    del_list.append(monsters[mk])
            if len(del_list) > 0:
                for dl in del_list:
                    monsters.remove(dl)
            next_direction = copy.deepcopy(direction)
            next_direction.append(i)
            move_pack(next_direction, (nr, nc), next_eat_count)

            if len(del_list) > 0:
                monsters = copy.deepcopy(original_monsters)

def remove_monsters():
    global pack_r, pack_c
    global best_direction
    global best_eat
    global monsters
    global dead_monster

    cr, cc = pack_r, pack_c
    for db in best_direction:
        cr, cc = cr + dr_pack[db], cc + dc_pack[db]
        del_list = []
        for mk in range(len(monsters)):
            if monsters[mk][0] == cr and monsters[mk][1] == cc:
                del_list.append(monsters[mk])
        if len(del_list) > 0:
            for dl in del_list:
                dead_monster[2].append((dl[0], dl[1]))
                monsters.remove(dl)
    best_eat = -1
    best_direction = []
    pack_r, pack_c = cr, cc

def manage_dead():
    global dead_monster

    dead_monster[0] = dead_monster[1]
    dead_monster[1] = dead_monster[2]
    dead_monster[2] = []

def done_copy():
    global monsters
    global eggs
    for egg in eggs:
        monsters.append(egg)
    eggs = []

for _ in range(t):
    # 1. 몬스터 복제 시도
    monster_copy()
    #print("1. ", monsters)
    # 2. 몬스터 이동
    move_monster()
    #print("2. ", monsters)
    # 3. 팩맨 이동
    # 팩맨 이동경로 찾기
    move_pack([], (pack_r, pack_c), 0)
    # 팩맨 이동경로에 있는 몬스터 삭제
    remove_monsters()
    #print("3. ", monsters)
    # 4. 몬스터 시체 소멸
    manage_dead()
    # 5. 몬스터 복제 완성
    done_copy()
    #print("4. ", monsters)

print(len(monsters))