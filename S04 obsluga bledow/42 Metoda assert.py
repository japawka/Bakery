# import datetime
# netto = 100
# brutto = 120
# # Netto should be lower or equal to brutto
# assert netto <= brutto, "Netto should be lower or equal to brutto"
# # jeśli to założenie nie będzie spełnione - wyskoczy błąd
# # zastępuje to if jakby
#
# order_date = datetime.date(2020, 11 ,23)
# delivery_date = datetime.date(2020 ,10, 12)
#
# # order date must be earlier than delivery
#
# assert  order_date <= delivery_date, "order date cannot be later than delivery date"


#####################################   LAB
import datetime as dt

class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        assert len(self.title) != 0, "Title is empty!"
        assert self.start < self.end, "Start date is later than end date!"

    @classmethod
    def publish_offer(cls, trips):

        list_of_errors = []

        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))
            except Exception as e:
                list_of_errors.append("{}: {}".format(trip.symbol, str(e)))

        assert len(list_of_errors) == 0, "The list of trips has errors: {}".format(list_of_errors)
        print('the offer will be published...')


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 6, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 1), dt.date(2023, 5, 12))
]

try:
    print('Publishing trips...')
    Trip.publish_offer(trips)
    print('... done')
except Exception as e:
    print('THERE ARE ERRORS')
    print(e)
    print('THE OFFER CANNOT BE PUBLISHED')