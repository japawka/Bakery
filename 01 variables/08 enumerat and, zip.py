workDays = [19, 20, 21, 20, 22, 21]
print(workDays)
workDict = {a: b for a, b in zip(range(1, len(workDays) + 1), workDays)}
print(workDict)

enumeratedWorkDays = list(enumerate(workDays))  # bez utworzenia  listy zwróci tylko 'enumerate object',
# a tsk listę krotek
print(enumeratedWorkDays)
for a, b in enumeratedWorkDays:
    print(f'possition - {a}, value - {b}')

months = ['I', 'II', "III", "IV", 'V', 'VI']
zipDays = list(zip(months, workDays))
print(zipDays)

for a, b in zipDays:
    print(f'month - {a}, value - {b}')

 # enumerate mozemy połączyć z zip

for pos, (m, d) in enumerate(zip(months, workDays), 1):
    print(f'position {pos} month {m} days {d}')


##########################################################
projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
for project, name in zip(projects, leaders):
    print(f'The leader of "{project}" is {name}')

dates = ['2016-06-23', '2016-08-29', '1994-01-01']

for project, date,  name in zip(projects, dates,  leaders):
    print(f'The leader of "{project}" started {date} is {name}')

for pos, (project, date,  name) in enumerate(zip(projects, dates,  leaders), 1):
    print(f'{pos} - The leader of "{project}" started {date} is {name}')