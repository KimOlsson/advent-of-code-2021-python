from sys import exit

FORWARD, DOWN, UP = "forward down up".split()

def read_file_to_list(fname: str, encoding='utf-8') -> list[str]:
    data = []
    with open(fname, 'r', encoding=encoding) as file:
        for line in file:
            data.append(line.strip())
    return data

def str_to_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        exit('You attempted to convert value {} to int\nQuitting..'.format(value))

def process_movement_commands(movements: list[str]) -> tuple[int, int]:
    position, depth, aim = 0, 0, 0
    for command in movements:
        direction, raw_value = command.split(" ", 1)
        value = str_to_int(raw_value)
        if direction == FORWARD:
            position += value
            depth += aim * value
        elif direction in [UP, DOWN]:
            aim = (aim-value) if direction == UP else (aim+value)
        else:
            exit('Unknown direction {} given\nQuitting..'.format(direction))
    return position, depth

def run():
    data = read_file_to_list('movement')
    position, depth = process_movement_commands(data)
    print('You ended up in position {} and depth of {}'.format(position, depth))
    print('Multiplying these together yields {}'.format(position*depth))

if __name__ == '__main__':
    run()
