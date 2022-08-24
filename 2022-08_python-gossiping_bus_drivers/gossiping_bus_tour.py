def gossiping_bus_tour(schedule: list):
    schedule = [repeat_bus_route(route) for route in schedule]
    drivers_nb = len(schedule)
    gossips = [set([i]) for i in range(drivers_nb)]

    if solved(drivers_nb, gossips):
        return "0"

    stops_at_minute = list(zip(*schedule))

    for minute, stops in enumerate(stops_at_minute):

        drivers_at_stop = get_drivers_at_stop(stops)

        for drivers in drivers_at_stop.values():
            if more_than_one_driver_at_stop(drivers):
                [gossips[driver].update(drivers) for driver in drivers]

        if solved(drivers_nb, gossips):
            return str(minute + 1)

    return "never"


def repeat_bus_route(route: list):
    repeat_times = 10
    for i in range(repeat_times):
        route.extend(route)
    return route


def more_than_one_driver_at_stop(drivers):
    return len(drivers) > 1


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
