def calculate_experience_points(level):
    xp = 0
    for i in range(1, level):
        xp += i * 5
    return xp
