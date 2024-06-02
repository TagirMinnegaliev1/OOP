class Date:
    def __init__(self, month, day):
        self.month = month
        self.day = day

    def __sub__(self, other):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days = 0

        if self.month == other.month:
            days = abs(self.day - other.day)
        elif self.month > other.month:
            days += (days_in_month[other.month - 1] - other.day)
            for m in range(other.month + 1, self.month):
                days += days_in_month[m - 1]
            days += self.day
        else:
            days += (days_in_month[self.month - 1] - self.day)
            for m in range(self.month + 1, other.month):
                days += days_in_month[m - 1]
            days += other.day

        return days if self.month != other.month else days * (-1 if self.day < other.day else 1)

jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)