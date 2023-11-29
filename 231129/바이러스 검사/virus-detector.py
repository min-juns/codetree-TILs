import math

N = int(input())
customer = list(map(int, input().split()))
max_zang, max_won = map(int, input().split())

total_res = 0
for n in range(N):
    current_cu = customer[n]
    total_res += 1
    current_cu -= max_zang
    if current_cu <= 0:
        continue
    else:
        total_res += math.ceil(current_cu / max_won)

print(total_res)