from datetime import datetime


# реализация объекта, с перегруженными операторами
class Train:

    def __init__(self, date, dep_time, trav_time, num, type):
        self.date = datetime.strptime(date, '%m/%d/%Y')
        self.dep_time = dep_time
        self.trav_time = trav_time
        self.num = num
        self.type = type

    def __lt__(self, other):
        if self.date != other.date:
            return self.date < other.date
        if self.dep_time != other.dep_time:
            return self.dep_time < other.dep_time
        if self.num != other.num:
            return self.num < other.num
        return self.trav_time < other.trav_time

    def __le__(self, other):
        if self.date != other.date:
            return self.date <= other.date
        if self.dep_time != other.dep_time:
            return self.dep_time <= other.dep_time
        if self.num != other.num:
            return self.num <= other.num
        return self.trav_time <= other.trav_time

    def __gt__(self, other):
        if self.date != other.date:
            return self.date > other.date
        if self.dep_time != other.dep_time:
            return self.dep_time > other.dep_time
        if self.num != other.num:
            return self.num > other.num
        return self.trav_time > other.trav_time

    def __ge__(self, other):
        if self.date != other.date:
            return self.date <= other.date
        if self.dep_time != other.dep_time:
            return self.dep_time >= other.dep_time
        if self.num != other.num:
            return self.num >= other.num
        return self.trav_time >= other.trav_time
