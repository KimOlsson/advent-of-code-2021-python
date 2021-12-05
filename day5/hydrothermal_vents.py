from sys import exit
#from pprint import pprint  # pprint seems to crash if list dimensions are too large (1000x1000)?

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

def parse_coordinates(raw_coordinates: list[str]):
    coordinates_arrowless = [x.split(' -> ') for x in raw_coordinates]

    coordinates = []
    for line in coordinates_arrowless:
        x1, y1 = line[0].split(',', 1)
        x2, y2 = line[1].split(',', 1)
        start = (str_to_int(x1), str_to_int(y1))
        end = (str_to_int(x2), str_to_int(y2))
        coordinates.append([start, end])
    return coordinates

def find_largest_coordinates(coordinates: list[list[tuple[int, int]]]) -> tuple[int, int]:
    max_x = 0
    max_y = 0
    for line in coordinates:
        start, end = line
        if start[0] > max_x: max_x = start[0]
        if start[1] > max_y: max_y = start[1]
        if end[0] > max_x: max_x = end[0]
        if end[1] > max_y: max_y = end[1]
    return max_x, max_y

def coordinates_overlap(start: tuple[int, int], end: tuple[int, int]) -> bool:
    return start[0] == end[0] or start[1] == end[1]

def fill_diagram_vertical_line(diagram: list[list[int]], line: tuple[int, int], x: int):
    start, end = line
    for y in range(start, end+1):
        diagram[y][x] += 1

def fill_diagram_horizontal_line(diagram: list[list[int]], line: tuple[int, int], y: int):
    start, end = line
    for x in range(start, end+1):
        diagram[y][x] += 1

def fill_diagram_diagonal_line(diagram: list[list[int]], start: tuple[int, int], end: tuple[int, int]):
    x1, y1 = start
    x2, y2 = end
    line_length = abs(x1 - x2)
    smaller_x, _ = tuple_of_two_ints_in_ascending_order(x1, x2) # 5, 8
    smaller_y, _ = tuple_of_two_ints_in_ascending_order(y1, y2) # 2, 5
    for i in range(line_length+1):
        movement_x = x1+i if x1 == smaller_x else x1-i
        movement_y = y1+i if y1 == smaller_y else y1-i
        diagram[movement_y][movement_x] += 1

def tuple_of_two_ints_in_ascending_order(num1: int, num2: int) -> tuple[int, int]:
    return (num1, num2) if num1 <= num2 else (num2, num1)

def fill_diagram(diagram: list[list[int]], coordinates: list[list[tuple[int, int]]]):
    for line in coordinates:
        start, end = line
        if coordinates_overlap(start, end):
            start_x, end_x = tuple_of_two_ints_in_ascending_order(start[0], end[0])
            start_y, end_y = tuple_of_two_ints_in_ascending_order(start[1], end[1])

            if start_x == end_x: fill_diagram_vertical_line(diagram, (start_y, end_y), start_x)
            elif start_y == end_y: fill_diagram_horizontal_line(diagram, (start_x, end_x), start_y)
        else:
            x_abs_difference = abs(start[0]-end[0])
            y_abs_difference = abs(start[1]-end[1])
            if x_abs_difference == y_abs_difference:
                fill_diagram_diagonal_line(diagram, start, end)

def overlap_count(diagram: list[list[int]], height=2) -> int:
    overlaps = 0
    for row in diagram:
        for col in row:
            if col >= height:
                overlaps += 1
    return overlaps

def simple_tests():
    raw_coordinates = read_file_to_list('sample_data')
    coordinates = parse_coordinates(raw_coordinates)
    max_x, max_y = find_largest_coordinates(coordinates)
    diagram = [[0]*(max_x+1) for _ in range(max_y+1)]
    fill_diagram(diagram, coordinates)

    assert(overlap_count(diagram, height=2) == 12)

def run():
    simple_tests()
    raw_coordinates = read_file_to_list('hydrothermal_vents')
    coordinates = parse_coordinates(raw_coordinates)
    max_x, max_y = find_largest_coordinates(coordinates)
    diagram = [[0]*(max_x+1) for _ in range(max_y+1)]
    fill_diagram(diagram, coordinates)

    overlaps_2_or_more = overlap_count(diagram, height=2)

    print("Overlaps:", overlaps_2_or_more)

if __name__ == '__main__':
    run()