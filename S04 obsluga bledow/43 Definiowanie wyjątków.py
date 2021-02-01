class BITException(Exception):
    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return f'{super().__str__()}, area {self.area}'


class BITSecurityException(BITException):  # tylko żeby nazwa i komunikat były inne
    pass


class BITDataFormatException(BITException):
    pass


try:
    # do smth...
    raise BITDataFormatException('file format is incorrect', 'Financial data')

except BITSecurityException as e:
    print(f'Application security error: {e}')

except BITDataFormatException as e:
    print(f'Application data malformed error: {e}')

except BITException as e:
    print(f'Application error: {e}')

except Exception as e:
    print(f'General error: {e}')

################################################# LAB
import datetime as dt


class TripException(Exception):
    def __init__(self, text, desccription):
        super().__init__(text)
        self.description = desccription

    def __str__(self):
        return f'{super().__str__()} description: {self.description}'


class TripNameException(TripException):
    def __init__(self, text):
        super().__init__(text, "Name of the trip is missing")


class TripDateException(TripException):
    def __init__(self, text):
        super().__init__(text, "Date of end of trip is earlier than start date")


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise TripNameException("Name error")
        if self.start > self.end:
            raise TripDateException("Date error")

    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except TripNameException as e:
                list_of_errors.append(f'{trip.symbol} : {e}')
            except TripDateException as e:
                list_of_errors.append(f'{trip.symbol} : {e}')
        if list_of_errors:
            raise TripException("The list of trips has errors:", list_of_errors)
        else:
            print("the offer will be published...")


trips = [
    Trip('IT-VNC', '', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print("starting checking trips")
    Trip.publish_offer(trips)
    print('Done')
except Exception as e:
    print("There was fatal error: ", e)
