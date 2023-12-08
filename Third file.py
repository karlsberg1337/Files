a = int(input('Необходимо ввести большее число: '))
b = int(input('Необходимо ввести меньшее число: '))

remainder = a % b

if remainder == 0:
    print('The number b is a multiple of a')
else:
    print (f'The number b is not a multiple of a\nremainder - {remainder}')
