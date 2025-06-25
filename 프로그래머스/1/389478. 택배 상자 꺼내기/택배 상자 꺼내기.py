def solution(n, w, num):
    total_floors = (n - 1) // w + 1
    target_floor = (num - 1) // w + 1
    last_floor_dir = (total_floors - 1) % 2  # 0: L→R, 1: R→L

    def col(nth, floor_dir):
        rem = (nth - 1) % w + 1
        return rem if floor_dir == 0 else (w - rem + 1)

    col_last = col(n, last_floor_dir)
    col_target = col(num, (target_floor - 1) % 2)

    answer = total_floors - target_floor
    if last_floor_dir == 0:
        if col_target <= col_last:
            answer += 1
    else:
        if col_target >= col_last:
            answer += 1

    return answer
