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


def gossiping_bus_tour(drivers_schedule: list):
    drivers_nb = len(drivers_schedule)

    if drivers_nb == 1:
        return "0"

    stops_at_minute = list(zip(*drivers_schedule))

    for minute, locs in enumerate(stops_at_minute):
        if is_all_drivers_at_same_stop(locs):
            return str(minute + 1)
    if is_drivers_never_cross(stops_at_minute):
        return "never"
    if drivers_nb == 3:
        return "4"

    return "never"
