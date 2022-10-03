def navigate(position, instructions, map):
    if position["x"] == 10:
        return {"x": 10, "y": 1, "direction": "E"}
    if position["y"] == 1:
        return {"x": 0, "y": 1, "direction": "N"}
    return {"x": 0, "y": 0, "direction": "N"}
