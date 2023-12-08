a = int(input('Необходимо ввести первое число: '))
b = int(input('Необходимо ввести второе число: '))
c = int(input('Необходимо ввести третье число: '))

middle_n = a
if a == b or b == c or a == c:
    middle_n = 'Error'
else:
    if (b > a and b < c) or (b < a and b > c):
        middle_n = b
    elif (c > a and c < b) or (c < a and c > b):
        middle_n = c

print(f'Middle number - {middle_n}')
