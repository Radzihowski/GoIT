class date:
    def __init__(self):

@day.setter
def day(self, days):
    if self.month == 2 and self.year // 4 == 0:
        if 1 <= days <= 29:
            self.days=days
        else:
            raise ValueError("Wrong day value")
    elif self.month==2:
        if 1<=days<=28:
            self.days = days
        else:
            raise ValueError("Wrong day value")
    elif self.month in (1,3,5,7,):
        if 1<=days<=31:
            self.days = days
        else:
            raise ValueError("Wrong day value")
    elif self.month in (4,6,9,11):
        if 1<=days<=30:
            self.days = days
        else:
            raise ValueError("Wrong day value")
    else:
        raise ValueError("Wrong month value")

    def validate(self):
        pass

    def getAsString():
        pass

d = date()


