def gossiping_bus_tour(drivers_schedule: list):
    if len(drivers_schedule) == 1:
        return "0"
    elif len(drivers_schedule) >= 1:
        return "1"
    return "never"
