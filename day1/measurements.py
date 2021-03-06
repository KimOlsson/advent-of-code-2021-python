from sys import exit, argv

def read_file_to_list(fname: str, encoding='utf-8') -> list[str]:
    data = []
    with open(fname, 'r', encoding=encoding) as file:
        for line in file:
            data.append(line.strip())
    return data

def list_to_int_list(data: list) -> list[int]:
    try:
        return [int(x) for x in data]
    except:
        data_sample = data[:3]
        exit('Unable to convert list to type int.\nData sample {}\nQuitting..'.format(data_sample))

def count_depth_increments(measurements: list[int], depth=1) -> int:
    if depth < 1:
        exit('count_depth_increments() depth was set to less than one.\nQuitting..')
    
    if len(measurements) <= depth:
        exit('not enough data to measure with given depth\nQuitting..')

    depth_increase_count = 0
    for index in range(1, len(measurements)+depth-1):
        previous = sum(measurements[index-1:(index-1+depth)])
        current = sum(measurements[index:(index+depth)])

        if previous < current:
            depth_increase_count += 1
    return depth_increase_count

def get_depth():
    depth = 1
    try:
        if len(argv) > 1:
            depth = int(argv[1])
    except ValueError:
        exit('Unable to convert given parameter to type int\nQuitting..')
    return depth

def simple_tests():
    sample_input = [199,200,208,210,200,207,240,269,260,263]
    assert(count_depth_increments(sample_input, depth=1) == 7)
    assert(count_depth_increments(sample_input, depth=3) == 5)

def run():
    simple_tests()
    depth = get_depth()
    raw_measurements = read_file_to_list('measurements')
    measurements = list_to_int_list(raw_measurements)
    depth_increase_count = count_depth_increments(measurements, depth=depth)
    print("Depth increase count was {} at given depth of {}".format(depth_increase_count, depth))

if __name__ == '__main__':
    run()