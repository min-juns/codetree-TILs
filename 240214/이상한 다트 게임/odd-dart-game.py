from collections import deque
import copy
# n: 총 원판의 반지름, m: 원판 하나에 적힌 정수 개수, q: 회전하는 횟수
n, m, q = map(int, input().split())

dart = []
for _ in range(n):
    dart.append(deque(list(map(int, input().split()))))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for t in range(q):
    # x: 원판의 종류, d: 방향(0 시계방향, 1 반시계방향), k: 회전하는 칸 수
    # step 1: 원판 움직이기
    x, d, k = map(int, input().split())
    nx = n // x
    d = d * 2 - 1

    for dx in range(nx):
        temp_plate = dart[x * (dx + 1) - 1]
        temp_plate.rotate(-d * k)
        dart[x * (dx + 1) - 1] = temp_plate

    temp_dart = copy.deepcopy(dart)
    # step 2: 같은 수 지우기
    for r in range(n):
        for c in range(m):
            # r: 반지름 크기, c: 몇번째 숫자인지
            check = False
            current_num = dart[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if nc < 0 or nc >= m:
                    nc = (nc + m) % m
                if nr < 0 or nr >= n:
                    continue
                if dart[nr][nc] == current_num:
                    check = True
                    temp_dart[nr][nc] = 0
            if check:
                temp_dart[r][c] = 0
    dart = temp_dart

res = 0
for r in range(n):
    for c in range(m):
        res += dart[r][c]

print(res)