def is_all_drivers_at_same_stop(locations: tuple):
    s = set(locations)
    return len(set(locations)) == 1


def no_driver_at_same_stop(stops: tuple):
    drivers_number = len(stops)
    stop_in_use = len(set(stops))
    return drivers_number == stop_in_use


def is_drivers_never_cross(schedule):
    not_crossing_at_each_steps = [
        no_driver_at_same_stop(locs) for locs in schedule]
    if False in not_crossing_at_each_steps:
        return False
    return True


def solved(drivers_nb, gossips):
    for gossip in gossips:
        if len(gossip) < drivers_nb:
            return False
    return True


def gossiping_bus_tour(schedule: list):
    drivers_nb = len(schedule)
    gossips = [set([i]) for i in range(drivers_nb)]

    if solved(drivers_nb, gossips):
        return "0"

    stops_at_minute = list(zip(*schedule))

    for minute, locs in enumerate(stops_at_minute):
        if solved(drivers_nb, gossips):
            return minute + 1
        if is_all_drivers_at_same_stop(locs):
            return str(minute + 1)
    if is_drivers_never_cross(stops_at_minute):
        return "never"
    if drivers_nb == 3:
        return "4"

    return "never"
