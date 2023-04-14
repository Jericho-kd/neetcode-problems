# 70. Climbing Stairs (easy)
def climb_stairs(n: int):
    prev_step, next_step = 1, 1

    for _ in range(n-1):
        tmp = prev_step
        prev_step = prev_step + next_step
        next_step = tmp

    return prev_step