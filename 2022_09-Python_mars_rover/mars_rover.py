def navigate(position, instructions, map):
    if instructions:
        if position["direction"] == "N":
            position["y"] -= 1
        else:
            position["x"] += 1
    return position
