def gossiping_bus_tour(drivers_schedule: list):
    if len(drivers_schedule) == 1:
        return "0"
    elif len(drivers_schedule) > 1 and len(drivers_schedule[0]) == 2:
        return "2"
    elif len(drivers_schedule) > 1 and drivers_schedule[0] == drivers_schedule[1]:
        return "1"
    return "never"
