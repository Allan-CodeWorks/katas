def is_all_drivers_at_same_stop(locations: tuple):
    return len(set(locations)) == 1


def no_driver_at_same_stop(locations: tuple):
    drivers_number = len(locations)
    stop_in_use = len(set(locations))
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

    drivers_locations_list = list(zip(*drivers_schedule))

    for i, locs in enumerate(drivers_locations_list):
        if is_all_drivers_at_same_stop(locs):
            return str(i + 1)
    if is_drivers_never_cross(drivers_locations_list):
        return "never"
    if drivers_nb == 3:
        return "3"

    return "never"
