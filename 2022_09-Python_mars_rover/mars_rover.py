moves = {
    "N": lambda position: {**position, "y": position["y"]-1},
    "S": lambda position: {**position, "y": position["y"]+1},
    "W": lambda position: {**position, "x": position["x"]-1},
    "E": lambda position: {**position, "x": position["x"]+1},
}


def navigate(position, instructions, map):
    if instructions:
        position = moves[position["direction"]](position)
    return position
