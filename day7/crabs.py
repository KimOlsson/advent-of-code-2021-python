# This is a brute force solution

from sys import exit, maxsize

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

def distance_from(numbers: list[int], target: int):
    total_distance = 0
    for num in numbers:
        distance = abs(num-target)
        distance_cost = sum(range(int(distance)+1))
        total_distance += distance_cost
    return total_distance

def find_best_spot(numbers: list[int]):
    sorted_numbers = sorted(numbers)
    least_distance = maxsize
    for i in range(len(sorted_numbers)):
        distance = distance_from(numbers, i)
        least_distance = distance if distance < least_distance else least_distance
    return least_distance


def run():
    crabs_raw = read_file_to_list('data')
    crabs = crabs_raw[0].split(',')
    crabs_int = [str_to_int(x) for x in crabs]
    shortest_distance = find_best_spot(crabs_int)
    print("The shortest amount of gas: ", shortest_distance)


if __name__ == '__main__':
    run()