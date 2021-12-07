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

def offspring_offsprings(offsprings, time_left):
    if time_left < 10:
        print("\t\tNo more offsprings")
        return 0
    time_left -= 10
    offsprings += 1
    print("\toffspring made offspring! +1 offspring time left", time_left)
    for time_left_for_offspring in range(time_left, 0, -8):

        offsprings += offspring_offsprings(0, time_left_for_offspring)
    return offsprings

def amount_of_offsprings(timers, days=18):
    #fishes = 1
    offsprings_total = 0
    for i, timer in enumerate(timers):
        print("\n###Start parent", i+1)
        offsprings = 0
        time_left = days
        time_left -= timer+1
        #print("\tParent made offspring +1")
        #offsprings += 1
        for time_left_for_offspring in range(time_left, 0, -8):
            print("Parent time left", time_left_for_offspring)
            if time_left_for_offspring >= 8:
                print("\tParent made offspring +1")
                offsprings += 1
            offsprings += offspring_offsprings(0, time_left_for_offspring)
        print(f"Finished parent {i+1}/{len(timers)} - {offsprings}+1")
        offsprings_total += offsprings + 1
        if i == 2: break
    return offsprings_total

def run():
    raw_timers = read_file_to_list('data')
    timers = raw_timers[0].split(',')
    timers_int = [str_to_int(x) for x in timers]
    offsprings = amount_of_offsprings([3,4,3,1,2])
    print(offsprings)
    

if __name__ == '__main__':
    start = time() * 1000
    run()
    end = time() * 1000
    print(f"Program finished in {end-start}ms")