from sys import exit
from time import time

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

def firstborn(time_left: int):
    count = 1
    if time_left < 9:
        return count
    time_left -= 9  # After 9 days cycle goes to 6-days and first offspring is born
    count += firstborn(time_left)   # This should calculate all offsprings for the parent
    count += lanternfish_single_parent_family_tree(6, time_left)
    return count

def lanternfish_single_parent_family_tree(lanternfish, days):
    count = 0
    if days < lanternfish+1:
        return count
    time_left = days-(lanternfish+1)
    #count = 1
    count += firstborn(time_left)
    count += lanternfish_single_parent_family_tree(6, time_left)
    return count


def lanternfish_full_family_tree_size(lanternfishes: list[int], days=12):
    count_in_order = []
    for i, parent in enumerate(lanternfishes):
        count = 0
        print(f"Starting parent {i}")
        # Each fish has internal timer, lets calculate beginning of full cycle
        time_left = days-(parent+1)   # parent at day 3 should become 3..2..1..0..6, 4 steps.
        count += firstborn(time_left) # Family tree of the offspring
        print(f"\tParent {i} firstborn family tree counted..")
        count += lanternfish_single_parent_family_tree(6, time_left)
        print(f"parent {i} familytree finished\n")
        count_in_order.append(count)
        #return count
    return count

def run():
    raw_timers = read_file_to_list('data')
    timers = raw_timers[0].split(',')
    timers_int = [str_to_int(x) for x in timers]
    #offsprings = lanternfish_full_family_tree_size([3,4,3,1,2])
    count_of_timers = {}
    for unique_timer in timers_int:
        if unique_timer not in count_of_timers:
            count_of_timers[unique_timer] = 1
        count_of_timers[unique_timer] += 1
    print(count_of_timers)

    new_timers = list(set(timers_int))
    print(new_timers)
    offsprings = lanternfish_full_family_tree_size(new_timers)
    offsprings += len(timers_int)
    print(offsprings)
    

if __name__ == '__main__':
    start = time() * 1000
    run()
    end = time() * 1000
    print(f"Program finished in {end-start}ms")