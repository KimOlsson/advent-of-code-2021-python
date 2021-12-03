from sys import exit

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

def bit_counts_in_column(binaries: list[str], column: int) -> tuple[int, int]:
    zero_count, one_count = 0, 0
    for binary in binaries:
        binary_target = str_to_int(binary[column])
        if binary_target in [0, 1]:
            zero_count += 1 if binary_target == 0 else 0
            one_count += 1 if binary_target == 1 else 0
    return zero_count, one_count

def bit_counts(binaries: list[str]) -> list[tuple[int, int]]:
    binary_length = len(binaries[0])
    bit_counts_list = []
    for column in range(0, binary_length):
        zero_count, one_count = bit_counts_in_column(binaries, column)
        bit_counts_list.append((zero_count, one_count))
    return bit_counts_list

def most_common_bits_per_column(binaries: list[str]) -> list[int]:
    bit_counts_tuple = bit_counts(binaries)
    most_common_bits = []
    for tuple in bit_counts_tuple:
        zeros, ones = tuple
        more_common_bit = 1 if ones > zeros else 0
        most_common_bits.append(more_common_bit)
    return most_common_bits

def remove_binaries_not_matching_bit_in_position(binaries: list[str], bit: int, position: int) -> list[str]:
    return [x for x in binaries if str_to_int(x[position]) == str_to_int(bit)]

def oxygen_generator_rating(binaries: list[str]) -> list[str]:
    binaries_left = binaries[:]
    for column in range(len(binaries[0])):
        zeros, ones = bit_counts_in_column(binaries_left, column)
        most_common_bit = 1 if ones >= zeros else 0
        binaries_left = remove_binaries_not_matching_bit_in_position(binaries_left, most_common_bit, column)

        found_the_target = len(binaries_left) == 1
        if found_the_target:
            return binaries_left     
    return None

def co2_scrubber_rating(binaries: list[str]) -> list[str]:
    binaries_left = binaries[:]
    for column in range(len(binaries[0])):
        zeros, ones = bit_counts_in_column(binaries_left, column)
        most_common_bit = 1 if ones >= zeros else 0
        least_common_bit = 0 if most_common_bit == 1 else 1
        binaries_left = remove_binaries_not_matching_bit_in_position(binaries_left, least_common_bit, column)
        
        found_the_target = len(binaries_left) == 1
        if found_the_target:
            return binaries_left
    return None


def bin_int_list_to_int(binary: list[int]) -> int:
    return int(''.join(str(x) for x in binary), 2)

def bin_to_gamma(binary: list[int]) -> int:
    return bin_int_list_to_int(binary)

def bin_to_epsilon(binary: list[int]) -> int:
    flipped_bin = []
    for bin in binary:
        new_bin = 0 if bin == 1 else 1
        flipped_bin.append(new_bin)
    return bin_int_list_to_int(flipped_bin)

def simple_tests():
    binaries = "00100 11110 10110 10111 10101 01111 00111 11100 10000 11001 00010 01010".split()
    most_common_bits = most_common_bits_per_column(binaries)
    assert(most_common_bits == [1,0,1,1,0])
    assert(bin_to_gamma(most_common_bits) == 22)
    assert(bin_to_epsilon(most_common_bits) == 9)
    assert(oxygen_generator_rating(binaries) == ['10111'])
    assert(co2_scrubber_rating(binaries) == ['01010'])

def run():
    simple_tests()

    raw_binaries = read_file_to_list('diagnostic_report')
    most_common_bits = most_common_bits_per_column(raw_binaries)
    gamma = bin_to_gamma(most_common_bits)
    epsilon = bin_to_epsilon(most_common_bits)
    print(f'Most common bits: {most_common_bits}')
    print(f'Gamma value was {gamma}')
    print(f'Epsilon value was {epsilon}')

    oxygen_results = oxygen_generator_rating(raw_binaries)
    oxygen_rating = bin_int_list_to_int(oxygen_results)
    co2_results = co2_scrubber_rating(raw_binaries)
    co2_rating = bin_int_list_to_int(co2_results)
    print(f'Power consumption was {gamma*epsilon}')
    print(f'Oxygen rating was {oxygen_rating}')
    print(f'CO2 rating was {co2_rating}')
    print(f'Life support rating was {oxygen_rating*co2_rating}')

if __name__ == '__main__':
    run()