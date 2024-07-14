honapok = ['január', 'február','március', 'április']

# lista kiíratása
print(honapok)

# join(): a lista elemeit egy sztringgé fűzi össze
# a megadott elválasztó karakterekkel tagolva
print(', '.join(honapok))

# lista hossza: len( )
print(len(honapok))

# a 0. indexű az első elem
print(honapok[0])

# jelen esetben a 3. indexű az utolsó elem
print(honapok[3])

# túlindexelés, hibát okoz!
# ebben a listában az utolsó elem indexe: 3
# print(honapok[4]) <- HIBÁS!!!

# az 1-es és 2-es indexű elemek kiíratása
print(honapok[1:3])

# az elejétől a 2-es indexű elemmel bezárólag
print(honapok[:3])

# 2-es indexű elemtől a végéig
print(honapok[2:])

# hátulról az első, vagyis az utolsó elem
print(honapok[-1])   

# A sztringek elemeire is így hivatkozhatunk
szo = "almafa"
print(szo[:3])

# üres listát hoz létre
gyumolcsok = []

# kezdőérték nélküli változót hoz létre
gyumolcs = None
while gyumolcs != '':
    gyumolcs = input('Adj meg egy gyümölcsöt! ')
    if gyumolcs != '':
        # hozzáfűzi a listahoz
        gyumolcsok.append(gyumolcs)

print(gyumolcsok)  

# Gyakran szeretnénk egy lista elemeit vesszővel és szóközzel elválasztva megjeleníteni a képernyőn. Ezt így lehet a legegyszerűbben:
lista = [2, 5, 4, 8, 19, 11, 10, 2]

print(lista)
print(*lista, sep=', ')

'''
Tuple
A listához hasonlóan sorba rendezetten tartalmazza az elemeket, amelyek így index-szel rendelkeznek. Lényeges különbség azonban, hogy ezek állandó adatszerkezetek, azaz a benne tárolt érték, azok száma, sorrendje nem változtatható meg. Az elemek itt is vesszővel vannak elválasztva egymástól, de nem [ ], hanem ( ) jelek között.
'''

KEPERNYO_MERET = (1920, 1080)

'''
Set (halmaz)
A halmaz egy nem rendezett adatszerkezet. Az elemek nem rendelkeznek sorszámmal (index-szel). Egy elem csak egyszer szerepelhet benne { } jelek között.
'''

buszjaratok = {'1', '12', '12E'} 

'''
Dictionary
Ezen gyűjtemény kulcs-érték (key-value) párokba rendezetten tárolja az adatokat. Az értékekre az egyedi kulcs alapján lehet hivatkozni.
'''

hallgató = {
    'nev': 'Tamara',
    'kor': 25,
    'varos': 'Sopron'
}

# Lista bejárása

tantargyak = ['matek', 'töri', 'bio', 'kémia', 'info']

for tantargy in tantargyak:
    print(tantargy)

# 0 -> 9
for i in range(10):
    print(i)

# 5 -> 8
for i in range(5,9):
    print(i)

# 3 -> 20-ig 6-osával
for i in range(3,21,6):
    print(i)

# Lista bejárása index-szel I.

honapok = ['január', 'február','március', 'április', 'május', 'június'] 

index = 0
for honap in honapok:
    print(index, honap)
    index = index + 1

# Lista bejárása index-szel II.
honapok = ['január', 'február','március', 'április', 'május', 'június']

for index in range(len(honapok)):
    print(index, honapok[index])

# Lista bejárása index-szel III. <- EZ
   
honapok = ['január', 'február','március', 'április', 'május', 'június']

for index, honapok in enumerate(honapok):
    print(index, honapok)

'''
Nem mindegy, hogyan járod be a listát!
A fentiekben bemutatott három lehetőség közül az I. és III. számú esetben a lista bejárása úgy történik, hogy az egyes elemek - minden egyes cikluslépésben - egy 'honap' nevű átmeneti változóba kerülnek kimásolásra, és ezt használjuk fel a print utasításban. Ha módosítani szeretnéd a listaelemet (pl. nagybetűsre alakítani) akkor hiába tennéd ezt meg a 'honap' nevű változó esetében, ez az eredeti listaelemet NEM módosítaná! Így ez a bejárás csak az adatok olvasására alkalmas!
'''
honapok = ['január', 'február','március', 'április', 'május', 'június']

for honap in honapok:
    # az eredeti listaelem NEM módosul!
    honap = honap.upper()

'''
Ha módosítani szeretnéd a listaelemeket, akkor II. számú esetet kell mintaként venned! Ebben az esetben ugyanis az index segítségével közvetlenül az eredeti listaelemre hivatkozunk, így akár módosíthatjuk is azt!
'''
for index in range(len(honapok)):
    # az eredeti listaelem módosul!
    honapok[index] = honapok[index].upper()
        
# A lista bejárásának megszakítása
szamok = [1,7,8,10,12,9,3]

for szam in szamok:
    if szam % 2 == 0:
        print('Megvan az első páros szám a listában:')
        print(szam)
        break             # megszakítja a lista bejárását
print('Program vége')

# Szövegek (sztringek) összefűzhetőek
print('Jöttem' + ' ' + 'láttam' + ' ' + 'győztem.')

# Szövegek (sztringek) szorzásjellel megsokszorozhatóak
print('ja' + 'j' * 7)

# Más adattípusok szöveggé (sztringgé) alakíthatóak az str() függvénnyel
print(str(7.53))
  

sztring = 'Ismered ezt a számot?'

# Index-szel hivatkozhatunk egy elemükre
print(sztring[0])      # I
print(sztring[-1])     # ?

# Szeletelhetjük ezeket is 
print(sztring[2:11])
print(sztring[:9])
print(sztring[7:])

# Meghatározhatjuk a hosszukat
print(len(sztring))

# for-ciklussal is bejárhatóak
szamlalo = 0
for betu in sztring:
    if betu == 'e' or betu == 'E':
        szamlalo += 1
print(f'A sztringben {szamlalo} db e/E betű van.')

# Ezeknél is használható az in operátor
if 'e' in sztring:
    print('Van benne e betű.')
else:
    print('Nincs benne e betű.')

# Természetesen csak karaktereket tartalmazhatnak!

# Elemeik (a karakterek) nem módosíthatóak!
# Ez hibát okoz:
sztring = 'Ismered ezt a számot?'
#sztring[0] = 'i'  <- HIBA

sztirng = 'aLmafA' 

# Az első betűt nagybetűvé alakítja,
# de csak a kiírás erejéig, maga a sztring nem változik, 
# hiszen a sztringek elemei nem változtathatóak meg!
print(sztring.capitalize())

# Csupa nagybetűssé alakítja a sztringet
print(sztring.upper())

# Csupa kisbetűssé alakítja a sztringet
print(sztring.lower())

# Megszámolja, hányszor fordul elő a megadott karakter
print(sztring.count('a'))

# Megadja, hányadik indexű helyen fordul elő először a megadott karakter
print(sztring.find('a'))

# True-val tér vissza, ha a sztring minden eleme kisbetű 
print(sztring.islower())

# True-val tér vissza, ha a sztring minden eleme nagybetű 
print(sztring.isupper())

# Listák rendezése
nyelvek = ['Python', 'C', 'C++', 'Java']

# sorbarendezi a listát
nyelvek.sort()

# fordított sorrendbe rendezi a listát
nyelvek.reverse()

# az adott elem első előfordulásának indexe
print(nyelvek.index('C'))

# az adott elem hányszor fordul elő
print(nyelvek.count('Python'))

# NEM listametódus, de így lehet eldönteni, hogy egy elemet tartalmaz-e a lista
print('C++' in nyelvek)

# a lista végére hozzáfűz egy elemet
nyelvek.append('Python')

# a listát másolja
nyelvek_masolat = nyelvek.copy()

# a lista végére hozzáfűz egy másik gyűjteményt (pl. listát)
nyelvek_honlapkesziteshez = ['HTML', 'CSS', 'JavaScript']
nyelvek.extend(nyelvek_honlapkesziteshez)

# adott indexű helyre beszúrja a megadott elemet
nyelvek.insert(1, 'Go')

# eltávolítja a legutolsó elemet, és azzal tér vissza
# itt például a törölt értéket a 'torolt_nyelv' fogja tartalmazni
nyelvek.pop()
torolt_nyelv = nyelvek.pop()

# eltávolítja a megadott indexű elemet,  és azzal tér vissza
nyelvek.pop(1)

# eltávolítja a megadott indexű elemet
del nyelvek[1]

# eltávolítja a megadott elemet az elsőként megtalált pozícióból
nyelvek.remove('Python')

# törli a listát
nyelvek.clear()

# Listák kapcsán használt néhány beépített függvény
nyelvek = ['Python', 'C', 'C++', 'Java']

# METÓDUS: lista.metódus_név()
nyelvek.sort()

# FÜGGVÉNY: függvény_név(lista)
len(nyelvek)


nyelvek = ['Python', 'C', 'C++', 'Java']

# sorted() FÜGGVÉNY: lista elemeinek eredeti sorrendje nem változik, 
# csak rendezetten kerülnek kiírásra
print(sorted(nyelvek))  
print(nyelvek)

# sort() METÓDUS: lista felülírása, az elemek eredeti sorrendje megváltozik,
# rendezett lesz
nyelvek.sort()
print(nyelvek)


szamok = [1, 2, 3, 4, 5]
szavak = ['fal', 'szoba', 'kép', 'villáskulcs']

# megadja, hogy hány elemű a lista
print(len(szamok))

# csak számok esetében használható (különben hibát eredményez)
# összegzi a listában előfroduló számokat
print(sum(szamok))

# a legnagyobb elemet adja eredményül 
# (számnál a legnagyobbat, sztringnél ABC - pontosabban unicode szerinti - rendben az utolsót)
print(max(szavak))

# a legkisebb elemet adja eredményül
# (számnál a legkisebbet, sztringnél ABC - pontosabban unicode szerinti - rendben az elsőt)
print(min(szavak))  


diakok = ['Nóra', 'Gergő', 'Hanna', 'Tamás', 'Ádám']
eletkorok = [17, 16, 18, 18, 15]

print(list(zip(diakok, eletkorok)))

for diak, eletkor in zip(diakok, eletkorok):
    print(f'{diak}: {eletkor}')      
    
  