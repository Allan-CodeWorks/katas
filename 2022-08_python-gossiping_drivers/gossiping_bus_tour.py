def gossiping_bus_tour(drivers_schedule: list):
    routes_nb = len(drivers_schedule)
    drivers_schedule
    if routes_nb == 1:
        return "0"
    elif routes_nb > 1 and drivers_schedule[0] == drivers_schedule[1]:
        return "1"
    elif routes_nb > 1 and len(drivers_schedule[0]) > 1:
        return str(len(drivers_schedule[0]))
    return "never"
