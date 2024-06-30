# if-elif-else szerkezet 
szam = int(input('Adj meg egy számot! '))
if szam < 0:
    print('A megadott szám negatív.')
elif szam == 0:
    print('A megadott szám nulla.')
else:
    print('A megadott szám pozitív.')
print('>> A program vége! <<')

# Match ... case szerkezet
import random
a = random.randint(0, 10)
b = random.randint(0, 10)
print(f'Itt van két szám {a} és {b}, milyen műveletet végezzek velük? ')
valasz = input(f'Add meg a műveleti jelet! ')

match valasz:
    case '+':
        print(f'{a} {valasz} {b} = {a+b}')
    case '-':
        print(f'{a} {valasz} {b} = {a-b}')
    case '*':
        print(f'{a} {valasz} {b} = {a*b}')
    case '/' if b != 0:
        print(f'{a} {valasz} {b} = {a * b}')
    case '**' | '%':
        print('Ezt a műveletet még nem ismerem!')
    case other:
        # case _:
        print('?!')

# ...
x = 5
y = -3

if x < 0 and y < 0:
    print('mindkettő negatív')

if x < 0 or y < 0:
    print('van köztük negatív')

if not x <= 0:
    print('x pozitív')

# ord és chr

# Az ord() függvény
# az adott betű Unicode értékével tér vissza
print(ord('a'))  # 97

# A chr() függvény
# az adott Unicode értéknek megfelelő betűvel tér vissza
print(chr(97))  # a 
        