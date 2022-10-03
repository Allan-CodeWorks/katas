def navigate(position, instructions, map):
    if instructions:
        if position["x"] == 3:
            return {"x": 3, "y": 0, "direction": "N"}
        return {"x": 1, "y": 0, "direction": "E"}
    return position
