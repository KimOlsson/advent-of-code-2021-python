class LanternFish:
    def __init__(self, timer=8):
        self.timer = int(timer)
        self.offsprings = []
        self.offspring_count = 0

    def handle_day_passing(self):
        if self.timer == 0:
            self.timer = 6
            return 1
        self.timer -= 1
        return 0

    def double_offspring_table_size(self):
        self.offsprings.extend([None]*len(self.offsprings))

    def handle_offspring_addition(self, timer=8):
        self.offsprings.append(LanternFish(timer=timer))
        
    def create_offspring_if_ready(self, timer=8):
        should_create_offspring = self.handle_day_passing()
        if should_create_offspring:
            self.handle_offspring_addition(timer)

    def __repr__(self):
        result = str(self.timer) + ", " + str(len(self.offsprings))
        return result