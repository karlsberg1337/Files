range = int(input('Необходимо ввести дальность выстрела: '))
if range == 29:
    print("Есть попадание!")
elif range >= 30:
    print('Мимо!')
elif range > 0 and range <= 28:
    print('Промах!')
else:
    print('Косой!')
