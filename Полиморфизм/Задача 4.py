class MinStat:
    def __init__(self):
        self.min_value = None

    def add_number(self, number):
        if self.min_value is None or number < self.min_value:
            self.min_value = number

    def result(self):
        return self.min_value


class MaxStat:
    def __init__(self):
        self.max_value = None

    def add_number(self, number):
        if self.max_value is None or number > self.max_value:
            self.max_value = number

    def result(self):
        return self.max_value


class AverageStat:
    def __init__(self):
        self.total_sum = 0
        self.count = 0

    def add_number(self, number):
        self.total_sum += number
        self.count += 1

    def result(self):
        if self.count == 0:
            return None
        return self.total_sum / self.count

values = [1, 0, 0]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
