from collections import deque

N, k = map(int, input().split())
belt = deque(list(map(int, input().split())))
people = deque([False for _ in range(N * 2)])


count = 0
while True:
    if belt.count(0) >= k:
        break
    count += 1

    # step 1
    belt.rotate(1)
    people.rotate(1)

    if people[N]:
        people[N] = False

    # step 2
    for n in range(N-1, -1, -1):
        if n == N-1:
            if people[n]:
                people[n] = False
        elif people[n]:
            if (not people[n+1]) and belt[n+1] != 0:
                people[n] = False
                people[n+1] = True
                belt[n+1] -= 1

    # step 3
    if not people[0] and belt[0] != 0:
        people[0] = True
        belt[0] -= 1
    
    # step 4
    if belt.count(0) >= k:
        break

print(count)