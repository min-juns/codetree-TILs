from collections import deque
import copy

game_map = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
game_map_10 = [13, 16, 19]
game_map_20 = [22, 24]
game_map_30 = [28, 27, 26]
# game map의 가장 마지막 index에 값이 있나 없나 체크 해야함
game_map_25 = [25, 30, 35, 40]
next_location = {0: game_map,
                 1: game_map_10,
                 2: game_map_20,
                 3: game_map_30,
                 4: game_map_25}
horse_location = [[0, 0], [0, 0], [0, 0], [0, 0]]
def run_game(horse_id, move):
    global horse_location
    # current_location: 0, 1, 2, 3, 4 idx: 해당 index
    # horse id : 0, 1, 2, 3
    current_location, current_location_idx = horse_location[horse_id]

    if current_location == 5:
        return 0

    if current_location == 0 and current_location_idx == 0:
        move = move + 1

    n_location, next_location_idx = 0, 0

    if current_location == 0 and (current_location_idx % 5 == 0) and current_location_idx != 20:
        n_location = current_location_idx // 5
        next_location_idx = move - 1
        if next_location_idx >= len(next_location[n_location]):
            next_location_idx = next_location_idx - len(next_location[n_location])
            n_location = 4

    elif current_location == 0:
        next_location_idx = current_location_idx + move
        n_location = 0

    elif current_location != 0 and current_location != 4:
        next_location_idx = current_location_idx + move
        n_location = current_location
        if next_location_idx >= len(next_location[current_location]):
            next_location_idx = next_location_idx - len(next_location[current_location])
            n_location = 4

    elif current_location == 4:
        n_location = current_location
        next_location_idx = current_location_idx + move


    if n_location == 0 and next_location_idx == 20:
        if [4, 3] in horse_location:
            return False
    if n_location == 4 and next_location_idx == 3:
        if [0, 20] in horse_location:
            return False

    if n_location == 0 and next_location_idx > 20:
        horse_location[horse_id] = [5, 0]
        return 0
    if n_location == 4 and next_location_idx > 3:
        horse_location[horse_id] = [5, 0]
        return 0

    if [n_location, next_location_idx] not in horse_location:
        horse_location[horse_id] = [n_location, next_location_idx]
        return next_location[n_location][next_location_idx]
    else:
        return False


game_list = deque(list(map(int, input().split())))
best_horse_list = []
total_score = 0
def game_start(game_idx, score, horse_list):
    global total_score
    global horse_location
    global best_horse_list
    if game_idx >= 10:
        if score > total_score:
            total_score = score
            best_horse_list = horse_list
    else:
        temp_horse_location = copy.deepcopy(horse_location)
        for h in range(4):
            c_score = run_game(h, game_list[game_idx])
            if c_score == False:
                horse_location = copy.deepcopy(temp_horse_location)
            else:
                horse_list.append(h)
                game_start(game_idx + 1, score + c_score, horse_list)
                horse_list.pop()
                horse_location = copy.deepcopy(temp_horse_location)

game_start(0, 0, [])
print(total_score)