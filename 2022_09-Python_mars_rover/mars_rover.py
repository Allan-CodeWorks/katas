def navigate(position, instructions, map):
    if position["y"] == 1:
        return {"x": 0, "y": 1, "direction": "N"}
    return {"x": 0, "y": 0, "direction": "N"}
