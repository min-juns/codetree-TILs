from collections import deque

visited = [False for _ in range(4)]

table = []
for _ in range(4):
    table.append(deque(list(map(int, input()))))

# 1은 시계방향, -1은 반시계방향
def rotate(table_num, direction):
    global table
    global visited
    visited[table_num - 1] = True
    d = direction

    if table_num == 1:
        # table 2를 움직여야 하는지 check
        if (table[0][2] != table[1][6]) and not visited[1]:
            rotate(2, -direction)
        current_table = table[0]
        current_table.rotate(d)
        table[0] = deque(current_table)

    elif table_num == 2 or table_num == 3:
        real_table_num = table_num - 1
        # 왼쪽 움직여야 하는지
        if (table[real_table_num][6] != table[real_table_num - 1][2]) and not visited[real_table_num - 1]:
            rotate(table_num - 1, -direction)
        # 오른쪽 움직여야 하는지
        if (table[real_table_num][2] != table[real_table_num + 1][6]) and not visited[real_table_num + 1]:
            rotate(table_num + 1, -direction)
        current_table = table[real_table_num]
        current_table.rotate(d)
        table[real_table_num] = deque(current_table)
    elif table_num == 4:
        # table 3를 움직여야 하는지 check
        if (table[2][2] != table[3][6]) and not visited[2]:
            rotate(3, -direction)
        current_table = table[3]
        current_table.rotate(d)
        table[3] = deque(current_table)
    else:
        print("error!!!!!!!!!")


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    rotate(a, b)
    visited = [False for _ in range(4)]


def get_result():
    return table[0][0] + table[1][0] * 2 + table[2][0] * 4 + table[3][0] * 8

print(get_result())