n = int(input())
val_list = list(map(int, input().split()))
operator_cnt = list(map(int, input().split()))

min_val = 100000000000
max_val = -100000000000

def find_val(ir_res, n_val):
    global min_val, max_val
    if n_val == n:
        min_val = min(ir_res, min_val)
        max_val = max(ir_res, max_val)
        return

    if operator_cnt[0] > 0:
        operator_cnt[0] = operator_cnt[0] - 1
        find_val(ir_res + val_list[n_val], n_val + 1)
        operator_cnt[0] = operator_cnt[0] + 1

    if operator_cnt[1] > 0:
        operator_cnt[1] = operator_cnt[1] - 1
        find_val(ir_res - val_list[n_val], n_val + 1)
        operator_cnt[1] = operator_cnt[1] + 1

    if operator_cnt[2] > 0:
        operator_cnt[2] = operator_cnt[2] - 1
        find_val(ir_res * val_list[n_val], n_val + 1)
        operator_cnt[2] = operator_cnt[2] + 1

find_val(val_list[0], 1)
print(min_val, max_val)