N = int(input())

task = [[]]
for _ in range(N):
    task.append(list(map(int, input().split())))

money = [0 for _ in range(N+1)]

for n in range(1, N+1):
    t = task[n][0]
    p = task[n][1]

    if n+t-1 > N:
        continue
    if money[n+t-1] < money[n-1] + p:
        money[n+t-1] = money[n-1] + p

print(max(money))