n, m, k = map(int, input().split())
atom_list = [list(map(int, input().split())) for _ in range(m)]
# x: 행, y: 열, m: 잘량, s: 속력, d: 방향
direction_r = [-1, -1, 0, 1, 1, 1, 0, -1]
direction_c = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):
    temp_map = [[[] for _ in range(n)] for _ in range(n)]
    # step1: 자신의 속력 만큼 이동
    for i in range(len(atom_list)):
        x, y, m, s, d = atom_list[i]
        x -= 1
        y -= 1
        x += (direction_r[d] * s) + (n * s)
        y += (direction_c[d] * s) + (n * s)
        x = (x % n)
        y = (y % n)
        atom_list[i] = [x, y, m, s, d]
        if temp_map[x][y] == []:
            temp_map[x][y] = [[m, s, d]]
        else:
            temp_map[x][y].append([m, s, d])

    next_map = [[[] for _ in range(n)] for _ in range(n)]
    # step 2: 합성
    for r in range(n):
        for c in range(n):
            if len(temp_map[r][c]) > 1:
                total_m = 0
                total_s = 0
                nd = 0
                first_case = (temp_map[r][c][0][2] % 2)
                num_atom = len(temp_map[r][c])
                for temp_atom in temp_map[r][c]:
                    total_m += temp_atom[0]
                    total_s += temp_atom[1]
                    if (temp_atom[2] % 2) == first_case and nd == 0:
                        nd = 0
                    else:
                        nd = 1
                nm = total_m // 5
                ns = total_s // num_atom
                if nm != 0:
                    for i in range(4):
                        n_r = (r + direction_r[(i*2) + nd] * ns + n) % n
                        n_c = (c + direction_c[(i*2) + nd] * ns + n) % n
                        if next_map[n_r][n_c] == []:
                            next_map[n_r][n_c] = [[nm, ns, nd+i*2]]
                        else:
                            next_map[n_r][n_c].append([nm, ns, nd + i * 2])

            elif len(temp_map[r][c]) == 1:
                temp_atom = temp_map[r][c][0]
                if next_map[r][c] == []:
                    next_map[r][c] = [[temp_atom[0], temp_atom[1], temp_atom[2]]]
                else:
                    next_map[r][c].append([temp_atom[0], temp_atom[1], temp_atom[2]])

    # atom_list에 정렬
    atom_list = []
    for r in range(n):
        for c in range(n):
            if next_map[r][c] != []:
                for atom_info in next_map[r][c]:
                    temp_val = atom_info
                    atom_list.append([r+1, c+1, temp_val[0], temp_val[1], temp_val[2]])


res = 0
for aa in atom_list:
    res += aa[2]
print(res)