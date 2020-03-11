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
def draw():
    global natezenie
    natezenie = natezenie + 1
    if natezenie == 225:
        natezenie=0
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
        
    if index==3:
        index=0
    rect(szerokosc,dlugosc,100,100)
    slownik={"czerwony":(225,0,0), "niebieski":(0,0,225), "zielony":(0,225,0)}
    print(slownik["zielony"])
    stroke(*slownik["zielony"])
    lista=[]
    global index
    print(dlugosc, szerokosc)
    for nazwa, wartosc in slownik.items():
        lista.append(wartosc)
    index += 1
    if index==3:
        index=0

    stroke(*lista[index])
def mousePressed():
    exit()
