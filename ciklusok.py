# while magyarul azt jelenti: amíg  
szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1

# While ciklus III. 
folytatja = True
while folytatja:
    print('Vidd ki a szemetet!')
    valasz = input('Mondjam még egyszer? (i/n)')
    if valasz == 'n':
        folytatja = False
print('>> Program vége! <<')      

# Adatbekérés while-ciklussal (szám bekérése megadott intervallumban) 
szam = int(input('Adj meg egy számot 5 és 10 között! '))

# while szam < 5 or 10 < szam:
while not 5 <= szam <= 10:
    szam = int(input('Helytelen érték! Adj meg egy számot 5 és 10 között! '))
  
print('Rendben!')     

# Adatbekérés while-ciklussal (adatkérés megszakítása ENTER-rel) 
szo = None
while szo != '':
    szo = input('Adj meg szavakat! Ha kilépnél, aszó helyett csak egy ENTER-t üss! ')    
  
print('Program vége!')

# break - A ciklus megszakítása 
szamlalo = 1
while szamlalo < 100:
    print(szamlalo)
    if (szamlalo % 13 == 0):
        break  # megszakítja a ciklust
    szamlalo = szamlalo + 1

# Egymásba ágyazott ciklusok I. 
sor = 1
while sor <= 3:
    oszlop = 1
    while oszlop <= 5:
        print('O ', end='')
        oszlop = oszlop + 1
    print('')
    sor = sor + 1       

# Hány alkalommal írja ki a program a "Hello!" üzenetet? 
n = 1
while n < 3:
    m = n + 1
    while m < 4:
        print('Hello!')
        m += 1
    n += 1  
  