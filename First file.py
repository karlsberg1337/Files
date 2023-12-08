a = int(input('Необходимо ввести первое число: '))
b = int(input('Необходимо ввести второе число: '))
c = int(input('Необходимо ввести третье число: '))
max_n = a
min_n = a
if b > a and b > c:
    max_n = x2
elif c > a and c > b:
    max_n = x3

if b < a and b < c:
    min_n = b
elif c < a and c < b:
    min_n = c
print (f'max number - {max_n}\nmin number - {min_n}')
