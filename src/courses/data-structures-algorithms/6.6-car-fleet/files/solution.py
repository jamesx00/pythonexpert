def car_fleet(target, positions, speeds):
    cars = sorted(zip(positions, speeds), reverse=True)
    fleets = 0
    max_time = 0
    for pos, speed in cars:
        time = (target - pos) / speed
        if time > max_time:
            fleets += 1
            max_time = time
    return fleets
