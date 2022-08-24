def gossiping_bus_tour(schedule: list):
    drivers_nb = len(schedule)
    gossips = [set([i]) for i in range(drivers_nb)]

    if solved(drivers_nb, gossips):
        return "0"

    stops_at_minute = list(zip(*schedule))

    for minute, stops in enumerate(stops_at_minute):

        drivers_at_stop = get_drivers_at_stop(stops)

        for drivers in drivers_at_stop.values():
            if len(drivers) > 1:
                for driver in drivers:
                    gossips[driver] = gossips[driver].union(drivers)

        if solved(drivers_nb, gossips):
            return str(minute + 1)

    if is_drivers_never_cross(stops_at_minute):
        return "never"

    return "never"


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


def get_drivers_at_stop(stops: tuple):
    drivers_at_stop = dict([(stop, set()) for stop in stops])
    for driver in range(len(stops)):
        stop = stops[driver]
        drivers_at_stop[stop].add(driver)
    return drivers_at_stop
