

def gossiping_bus_tour(drivers_schedule: list):
    routes_nb = len(drivers_schedule)
    drivers_schedule

    if routes_nb == 1:
        return "0"
    elif routes_nb > 1 and drivers_schedule[0] == drivers_schedule[1]:
        return "1"

    drivers_locations_list = list(zip(*drivers_schedule))

    for i, locs in enumerate(drivers_locations_list):
        if len(set(locs)) == 1:
            return str(i + 1)

    return "never"
