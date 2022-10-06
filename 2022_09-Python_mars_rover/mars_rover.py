moves = {
    'N': lambda position: {**position, 'y': position['y']-1},
    'S': lambda position: {**position, 'y': position['y']+1},
    'W': lambda position: {**position, 'x': position['x']-1},
    'E': lambda position: {**position, 'x': position['x']+1},
}


def navigate(position, instructions, map):

    for instruction in instructions:
        if 'Forward' in instruction:
            position = moves[position['direction']](position)
        else:
            if 'N' in position['direction']:
                position['direction'] = 'E'
            else:
                position['direction'] = 'N'

    return position
