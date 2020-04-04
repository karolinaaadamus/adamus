def setup():
    size(600,800)
    stroke(255,0,0)
    strokeWeight(3)
    global natezenie
    natezenie=0
    global index
    index=0
    frameRate(30)
    global szerokosc
    szerokosc=0
    global dlugosc
    dlugosc=0
    global zmienna
    zmienna=1
    global kierunek_zmiany
    kierunek_zmiany = 1
def draw():
    global natezenie
    global kierunek_zmiany
    natezenie = natezenie + kierunek_zmiany
    if natezenie == 225 or natezenie == 0:
        kierunek_zmiany *= -1 # dzięki temu zmiana natężenia będzie gładsza, dwustronna, bez skoku - jako ćwiczenie możesz to przeanalizować :)
#    line(mouseX,mouseY,width/3, height/3)
    fill(0,0,natezenie,120)
#    rect(20,30,120,140)
    fill(0,natezenie,0,120)
    global szerokosc
    global dlugosc
    global zmienna
    
    if dlugosc == 0 and szerokosc == 0:
        zmienna = 0
    if dlugosc == 250 and szerokosc == 0:
        zmienna = 2
    if dlugosc == 0 and szerokosc == 125:
        zmienna = 1
    if dlugosc == 500 and szerokosc == 500:
        zmienna = 3
    if dlugosc == 500 and szerokosc == 375:
        zmienna = 4
    if dlugosc == 240 and szerokosc == 505:
        zmienna = 5
    if dlugosc == 0 and szerokosc == 25:
        zmienna = 6
        
    if zmienna == 1:
        dlugosc +=10
        szerokosc +=5
    if zmienna == 2:
        dlugosc -=10
        szerokosc +=5
    if zmienna == 0:
        dlugosc +=10
        szerokosc +=10
    if zmienna == 3:
        dlugosc -=5
        szerokosc -=10
    if zmienna == 4:
        dlugosc -=20
        szerokosc +=10
    if zmienna == 5:
        dlugosc -=5
        szerokosc -=10
    if zmienna == 6:
        dlugosc =0
        szerokosc =0
# ciekawie napisane, ale ot nie do końca ta ścieżka, którą miał pokonywać obiekt ;)
    if index==3:
        index=0
    rect(szerokosc,dlugosc,100,100)
    slownik={"czerwony":(225,0,0), "niebieski":(0,0,225), "zielony":(0,225,0)} # mogłabyś zmienić kolory, byłoby ciekawiej i bardziej indywidualnie
    print(slownik["zielony"])
    stroke(*slownik["zielony"])
    lista=[]
    global index
    print(dlugosc, szerokosc)
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    # od definicji słownika dotąd lepiej byłoby wykonać raz w draw i udostępnić przez specyfikator global
    index += 1
    if index==3:
        index=0

    stroke(*lista[index])
    
def mousePressed():
    exit()
    
# 1,75 pkt
# dziwnym zbiegiem okoliczności u koleżanki Siehej program wygląda identycznie znaczek w znaczek...
