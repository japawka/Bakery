instructions = ['say hello', 'say how are you',  'say good bye', 'ask for help', 'ask fo money', 'say bye']
instructionApproved = []
for instr in instructions:
    print('adding instruction', instr)
    instructionApproved.append(instr)

    if instr == 'abort':
        print('Terminating!!!')
        instructionApproved.clear()
        break

else:  # wykona siętylko wtedy, kiedy break nie zostało wykonane
    print('following actions will perform', instructionApproved)

instructionApproved.clear()

i = 0
while i < len(instructions):
    print('adding instruction', instructions[i])
    instructionApproved.append(instructions[i])
    #i += 1  # jeśli i zwiększymy w tym miejscu, to dodawanie instrukcji abort sie nie wyświetli
    # i wywali bład przy sprawdzaniu następnej instrukcji, jeśli nie będzie abort

    if instructions[i] == 'abort':
        print('Terminating!!!')
        instructionApproved.clear()
        break
    i += 1
else:  # wykona siętylko wtedy, kiedy break nie zostało wykonane
    print('following actions will perform', instructionApproved)


############################################ LAB
import  os
import urllib.request
data_dir = r'D:\Python\Python_kurs_sredniozaawansowany\files'
pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'https://www.youtube.com/watch?v=4H-9a7nRgJY&ab_channel=DominiqueHeadcharge' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

for page in pages:
    try:
        path = os.path.join(data_dir, page['name'] +".html")
        urllib.request.urlretrieve(page['url'], path)
    except:
        print('something went wrong')
        break
else:
    print("Everything OK")