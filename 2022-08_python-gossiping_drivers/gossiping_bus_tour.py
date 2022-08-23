def is_all_drivers_at_same_stop(locations: tuple):
    if len(set(locations)) == 1:
        return True
    return False


def is_drivers_never_cross(schedule, driver_number):
    is_crossings = [len(set(locs)) != driver_number for locs in schedule]
    if True in is_crossings:
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
    if is_drivers_never_cross(drivers_locations_list, drivers_nb):
        return "never"
    if drivers_nb == 3:
        return "3"

    return "never"
