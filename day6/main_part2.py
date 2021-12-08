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

def lanternfish_start_new_family_tree_simulation(parent: int, days: int) -> tuple[int, int]:
    count = 0
    print(f"Starting calculating family tree size for timer {parent}")
    # Each fish has internal timer, lets calculate beginning of full cycle
    time_left = days-(parent+1)   # parent at day 3 should become 6 in ..2..1..0..6, 4 steps.
    count += firstborn(time_left) # Family tree of the firsborn offspring
    count += lanternfish_single_parent_family_tree(6, time_left)
    print(f"\tFamily tree size after {days} for timer {parent} was {count}")
    return count


def lanternfish_full_family_tree_size(lanternfishes: list[int], days=80) -> list[tuple[int, int]]:
    count_in_order = []
    for parent in lanternfishes:
        count = lanternfish_start_new_family_tree_simulation(parent, days)
        count_in_order.append((parent, count))
    return count_in_order

def timer_counts(timers: list[int]) -> dict[int: int]:
    count_of_timers = {}
    for unique_timer in timers:
        if unique_timer not in count_of_timers:
            count_of_timers[unique_timer] = 1
        else:
            count_of_timers[unique_timer] += 1
    return count_of_timers

def count_total_of_offsprings(result_for_each_unique_timer: tuple[int, int], count_of_timers: dict[int: int]):
    total = 0
    for timer in result_for_each_unique_timer:
        parent, count = timer
        total += count_of_timers[parent] * (count if count else 1)
    return total

def run(days):
    raw_timers = read_file_to_list('data')
    timers = raw_timers[0].split(',')
    timers_int = [str_to_int(x) for x in timers]
    count_of_timers = timer_counts(timers_int)

    unique_timers = sorted(list(set(timers_int)))
    print(f"Unique timers in input: {unique_timers}")
    amount_of_parents = len(timers_int)
    result_for_each_unique_timer = lanternfish_full_family_tree_size(unique_timers, days)
    total = count_total_of_offsprings(result_for_each_unique_timer, count_of_timers)
    total += amount_of_parents
    print(total)
    

if __name__ == '__main__':
    start = time() * 1000
    day_amount = 160
    run(day_amount)
    end = time() * 1000
    print(f"Program finished simulating {day_amount} days in {end-start}ms")