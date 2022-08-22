def gossiping_bus_tour(drivers_schedule: list):
    routes_nb = len(drivers_schedule)
    if routes_nb == 1:
        return "0"
    elif routes_nb > 1 and len(drivers_schedule[0]) == 2:
        return "2"
    elif routes_nb > 1 and len(drivers_schedule[0]) == 3:
        return "3"
    elif routes_nb > 1 and drivers_schedule[0] == drivers_schedule[1]:
        return "1"
    return "never"
