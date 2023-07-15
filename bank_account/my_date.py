from exceptions import DateTypeError, DateValueError


class Date:
    MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    MONTH_NAMES = ['', "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                   "Aug", "Sep", "Oct", "Nov", "Dec"]

    def __init__(self, year, month, day):
        try:
            if type(year) != int:
                raise DateTypeError("year", year)
            elif type(month) != int:
                raise DateTypeError("month", month)
            elif type(day) != int:
                raise DateTypeError("day", day)

            if year < 0:      # Այստեղ կարելի էր ստուգել նաև առանձին ամիսների օրերի ճիշտ քանակը
                raise DateValueError("year", year)
            elif month < 0 or month > 12:
                raise DateValueError("month", month)
            elif day < 0 or day > 31:
                raise DateValueError("day", day)
        except DateTypeError as err:
            print(err)
        except DateValueError as err:
            print(err)
        else:
            self.year = year
            self.month = month
            self.day = day

    def add_year(self, n):  # Այստեղ պետքա ստուգել նաև n-ի 0-ից մեծ լինելը
        self.year += n

    def add_month(self, n):
        self.add_year((self.month + n - 1) // 12)
        self.month = (self.month + n - 1) % 12 + 1

    def add_day(self, n):
        self.add_month((self.day + n - 1) // 30)
        self.day = (self.day + n - 1) % 30 + 1

    def __repr__(self):
        try:
            return "{} {} {}".format(self.day, self.MONTH_NAMES[self.month], self.year)
        except AttributeError:
            return "Object is empty."

