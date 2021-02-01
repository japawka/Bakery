def ProcessInvoice(netto, brutto):
    if netto > brutto:
        # raise Exception('Netto should be lower or equal to brutto')
        raise ValueError('Netto should be lower or equal to brutto')
    else:
        print(f'Processing invoice netto = {netto}, brutto = {brutto}')


def end_of_month():
    netto = 1800
    brutto = 16000

    try:
        ProcessInvoice(netto, brutto)
    except ValueError as e:  # nqajpierw błedy specyficzne, na końcu ogólne
        print(f"The values of invoice are incorrect: {e}")
        raise ValueError('Error when processing invoice') from e
    except Exception as e:
        print(f"Error processing invoice: {e}")
        raise Exception('General error when processing invoicces')


end_of_month()

################################################# LAB
import datetime as dt


class Trip:
    def __init__(self, symbol, title, start, end):
        self.symbol = symbol
        self.title = title
        self.start = start
        self.end = end

    def check_data(self):
        if len(self.title) == 0:
            raise Exception("Title is empty!")
        if self.start > self.end:
            raise ValueError("Start date is later than end date!")

    @classmethod
    def publish_offer(cls, trips):
        list_of_errors = []
        for trip in trips:
            try:
                trip.check_data()
            except ValueError as e:
                list_of_errors.append(f'{trip.symbol} : {e}')
            except Exception as e:
                list_of_errors.append(f'{trip.symbol} : {e}')
        if list_of_errors:
            raise Exception(f"The list of trips has errors: {list_of_errors}")
        else:
            print("the offer will be published...")


trips = [
    Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
    Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
    Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
]

try:
    print("starting checking trips")
    Trip.publish_offer(trips)
    print('Done')
except Exception as e:
    print("There was fatal error: ", e)
