# Ez egy egysoros komment.

'''
    Többsoros kommentet írhatunk
    3 aposztróf vagy 3 idézőjel közé írva.
    Így szoktuk megadni általában a program vagy programrészlet leírását.
'''
print('alma')  # Kiírunk egy sort

'''
A print függvény a megadott szöveg kiírása után sort emel, 
vagyis a következő print függvény már egy újabb sorba ír.
Az alapértelmezett viselkedés azonban felülírható a "t" paraméterrel.
'''
# a kiírást követően a kurzor egy tabulátornyit ugrik
print('Teszt', end='\t')

# a kiírást követően a kurzor a kiírás végén marad
print('Teszt', end='')   

# int típus egész szám tárolására
szam = 5
print(type(szam))

# float típus tizedes tört tárolására
tizedes_tort = 0.25
print(type(tizedes_tort))

# str típus (string) karaktersorozat tárolására
szoveg = 'alma'
print(type(szoveg))

# bool típus (boolean) két értéket vehet fel: True vagy False
oszthato = True
print(type(oszthato))

# sztring -> szám
szam = int('17')

# sztring -> tizedes tört
tizedes_tort = float('0.5')

# szám -> sztring
szoveg = str(17)

'''
snake_case
A változó nevét alkotó szavakat aláhúzásjellel kötjük össze: megadott_szam. Így használjuk a Python, C nyelv, SQL nyelv esetében is.

camelCase
Az alkotó szavakat egybeírjuk, de a másodiktól kezdődően nagy kezdőbetűvel: megadottSzamReciproka. Ezt az írásmódot használja pédául a Java, JavaScript.

kebab-case
Az alkotó szavakat kötőjellel választjuk el: megadott-szam. Ezt az írásmódot használja a CSS nyelv. 
'''

# Mivel az input függvény mindig sztringet ad vissza,
# ha számot kérsz be, ne feledkezz meg a típusátalakításról!
adat = input('Adj meg egy számot! ')
szam = int(adat)

# rövidebben:
szam = int(input('Adj meg egy számot! '))

x = 7
y = 3

# összeadás
print(x + y)

# kivonás
print(x - y)

# szorzás
print(x * y)

# osztás
print(x / y)

# maradékos osztás, az osztás maradékát adja eredményül
print(x % y)

szo1 = 'alma'
szo2 = 'fa'
print(szo1 + szo2)

szoveg1 = 'Adj meg '
szoveg2 = 'egy szamot!'
print(szoveg1, szoveg2)

x = 9
y = 2
print('9 % 2 = ', x % y)

# Az input függvénnyel ez azonban nem lehetséges, hibát eredményez!
# input(szo1, szoveg2) # HIBÁS!!!

# x = x + 3 helyett:
x += 3

# x = x - 3 helyett:
x -= 3

# x = x * 3 helyett:
x *= 3

# x = x / 3 helyett:
x /= 3

# x = x % 3 helyett:
x %= 3

x = 5
x = x ** 3  # x = 125
