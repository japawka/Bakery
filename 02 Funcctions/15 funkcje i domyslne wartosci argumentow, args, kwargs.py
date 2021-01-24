def buy_me(prefix='buy me', what='cake', *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)


buy_me(what='a new car', prefix='buy me')
buy_me('buy please', 'new car', "cat", 'dragon', 'star', shop='Rossman', when='tomorrow')
buy_me('buy me please', when='tomorrow')


products = ['milk', 'bread', 'butter', 'salmon', 'rice', 'toilet paper']
params = {'price': 'low', 'time':' now'}

buy_me('plesae buy me honey', 'newspaper', *products,  **params)


###########################  LAB
def calculata_paint(efficency_per_m2, *meters):
    needed_paint = efficency_per_m2 * sum(meters)
    return f'Your appartmen has walls area {sum(meters)}m2, you need {needed_paint} liters of paint'

print(calculata_paint(10, 2,4,6,4))
rooms = [2,4,6,4, 12.5, 124]
print(calculata_paint(10, *rooms))

path = r'D:\Python\Python_kurs_sredniozaawansowany\files\log_it.txt'
def log_it(*args):
    with open(path, 'a') as file:
        for arg in args:
            file.write(arg + ' ')
        file.write('\n')

log_it('milk', 'bread', 'butter', 'salmon', 'rice', 'toilet paper')
log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')