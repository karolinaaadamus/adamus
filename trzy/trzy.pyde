def setup():
    global tabKolor, wcisnietyKlawisz, zamiana, pierwszyKolor, drugiKolor, wcisnietyKlawisz
    size(600,600)
    pierwszyKolor = 0; drugiKolor = 0; zamiana = False; wcisnietyKlawisz = 0
    tabKolor = ["#C5AAF5", "#79BFA1"]
    textSize(100)
    textAlign(LEFT, TOP)
    noFill()
    rect(200, 200, 170, 120) # kształt miał być niestandardowy, prostokąt raczej nie łapie się w tą definicję
    rect(190, 190, 190, 140)
def draw():
    global pierwszyKolor, drugiKolor
    pierwszyKolor = myszkaNadLitera(200, 200)
    drugiKolor = wcisnietyKlawisz
    if zamiana:
        pierwszyKolor, drugiKolor = drugiKolor, pierwszyKolor
    fill(tabKolor[pierwszyKolor])
    text("K", 200, 200)
    fill(tabKolor[drugiKolor])
    text("A", 300, 200)
    pierwszyKolor = 0; drugiKolor = 0
def keyPressed():
    global wcisnietyKlawisz, zamiana
    if keyCode == LEFT or keyCode == RIGHT:
            zamiana = True
    if str(key).upper() == "A":
            wcisnietyKlawisz = 1
def keyReleased():
    global wcisnietyKlawisz, zamiana
    if keyCode == LEFT or keyCode == RIGHT:
            zamiana = False
    if str(key).upper() == "A":
            wcisnietyKlawisz = 0
def myszkaNadLitera(x, y):
    if mouseX >= x and mouseX <= x + 100 and mouseY >= y and mouseY <= y + 100:
        return 1
    else:
        return 0
# bardzo PRO rozwiązanie... sama na wszystko wpadłaś?
# 1,75p
