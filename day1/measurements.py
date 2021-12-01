from sys import exit

def read_file_to_list(fname: str, encoding='utf') -> list[str]:
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
    def list_to_buckets(data: list, bucket_size: int) -> list:
        for i in range(0, len(data)):
            bucket = data[i:i+bucket_size]
            if len(bucket) == bucket_size:
                yield sum(bucket)
    
    if depth < 1:
        exit('count_depth_increments() depth was set to less than one.\nQuitting..')
    
    measurement_buckets = []
    if depth == 1:
        measurement_buckets = measurements
    else:
        measurement_buckets = list(list_to_buckets(measurements, depth))

    if len(measurement_buckets) < 2:
        exit('Measurement buckets length is too short, try lowering the depth parameter value..\nQuitting..')
    
    depth_increase_count = 0
    for index in range(1, len(measurement_buckets)):
        previous = measurement_buckets[index-1]
        current = measurement_buckets[index]

        if previous < current:
            depth_increase_count += 1
    return depth_increase_count

def simple_tests():
    sample_input = [199,200,208,210,200,207,240,269,260,263]
    assert(count_depth_increments(sample_input, depth=1) == 7)
    assert(count_depth_increments(sample_input, depth=3) == 5)

def run():
    simple_tests()
    raw_measurements = read_file_to_list('measurements')
    measurements = list_to_int_list(raw_measurements)
    depth_increase_count = count_depth_increments(measurements, depth=3)
    print("Depth increase count was {}".format(depth_increase_count))

if __name__ == '__main__':
    run()