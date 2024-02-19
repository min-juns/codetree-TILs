# n: 고객의 수, m: 메모리 유실 선의 개수, h: 취약 지점의 개수
n, m, h = map(int, input().split())
connection = [[0 for _ in range(n)] for _ in range(h)]

for _ in range(m):
    r, c = map(int, input().split())
    connection[r-1][c] = 1

def detect(num):
    current_num = num
    for r in range(h):
        next_num = 0
        if current_num == 1:
            if connection[r][current_num] == 1:
                next_num = current_num + 1
            else:
                next_num = current_num
        elif current_num == n:
            if connection[r][current_num - 1] == 1:
                next_num = current_num - 1
            else:
                next_num = current_num
        else:
            if connection[r][current_num] == 1:
                next_num = current_num + 1
            elif connection[r][current_num-1] == 1:
                next_num = current_num - 1
            else:
                next_num = current_num
        current_num = next_num
    return current_num

def check_connection():
    for check_num in range(n):
        if detect(check_num) != check_num:
            return False
    return True

# case 1: 수정 없이 돌아가는 경우
check_first = check_connection()
if check_first:
    print(0)

# case 2: 하나만 추가했을 때 돌아가는 경우
check_second = False
if not check_first:
    for r in range(h):
        for c in range(n-1):
            add_r, add_c = r, c + 1
            if c + 1 == n - 1:
                if connection[add_r][add_c - 1] == 0 and connection[add_r][add_c] ==0:
                    connection[add_r][add_c] = 1
                    check_second = check_connection()
                    connection[add_r][add_c] = 0
            else:
                if connection[add_r][add_c - 1] == 0 and connection[add_r][add_c + 1] == 0 and connection[add_r][add_c] == 0:
                    connection[add_r][add_c] = 1
                    check_second = check_connection()
                    connection[add_r][add_c] = 0
            if check_second:
                break
        if check_second:
            break
if check_second:
    print(1)

# case 3: 하나만 추가했을 때 돌아가는 경우
check_third = False
def add_and_check(num):
    global check_third
    if check_third:
        return True
    if num >= 2:
        check_third = check_connection()
    else:
        for r in range(h):
            for c in range(n - 1):
                add_r, add_c = r, c + 1
                if c + 1 == n - 1:
                    if connection[add_r][add_c - 1] == 0 and connection[add_r][add_c] == 0:
                        connection[add_r][add_c] = 1
                        add_and_check(num+1)
                        connection[add_r][add_c] = 0
                else:
                    if connection[add_r][add_c - 1] == 0 and connection[add_r][add_c + 1] == 0 and connection[add_r][add_c] == 0:
                        connection[add_r][add_c] = 1
                        add_and_check(num+1)
                        connection[add_r][add_c] = 0
    return check_third

if not check_first:
    if not check_second:
        add_and_check(0)
        if check_third:
            print(2)

if not check_first:
    if not check_second:
        if not check_third:
            print(-1)