def navigate(position, instructions, map):
    if instructions:
        if position["direction"] == "N":
            position["y"] -= 1
        elif position["direction"] == "S":
            position["y"] += 1
        elif position["direction"] == "W":
            position["x"] -= 1
        else:
            position["x"] += 1
    return position
