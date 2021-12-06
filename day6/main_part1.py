# Second part requires really heavy simulations, sadly can't treat
# these fishes as individuals :sad: However, I'll leave this solution
# as is. Takes roughly 2.3 seconds to get to day 80, after that
# 10% increase in days increases the runtime by roughly 2x, if you
# try to run this simulation with custom time period, 
# watch out that you won't run out of RAM. :)

from sys import exit
from lanternfish import LanternFish
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

def create_lanternfishes(timers: list[str]) -> list[list[LanternFish]]:
    lanternfishes = []
    for timer in timers:
        lanternfishes.append(LanternFish(timer=timer))
    return lanternfishes

def handle_day_passing(lanternfishes: list[LanternFish]):
    if not lanternfishes:   return None
    for lanternfish in lanternfishes:
        if lanternfish is None: continue
        handle_day_passing(lanternfish.offsprings)
        lanternfish.create_offspring_if_ready()

def handle_time_period(lanternfishes: list[list[LanternFish]], days: int):
    for i in range(days):
        print(f"Day {i+1} - {count_all_fishes(lanternfishes)}")
        handle_day_passing(lanternfishes)
    print(f"Time period of {days} days has passed!")

def count_all_fishes(lanternfishes: list[LanternFish]):
    count = 0
    if not lanternfishes: return 0
    for lanternfish in lanternfishes:
        if lanternfish is None: continue
        count += count_all_fishes(lanternfish.offsprings)
        count += 1
    return count

def run():
    raw_timers = read_file_to_list('data')
    timers = raw_timers[0].split(',')
    lanternfishes = create_lanternfishes(timers)
    #print(lanternfishes)
    handle_time_period(lanternfishes, 80)
    #print(lanternfish_generations)
    #print(lanternfish_kin)
    print(count_all_fishes(lanternfishes))
    

if __name__ == '__main__':
    start = time() * 1000
    run()
    end = time() * 1000
    print(f"Program finished in {end-start}ms")