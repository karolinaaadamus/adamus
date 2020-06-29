def setup():
    global zdjecie
    zdjecie = loadImage("pies.jpg")
    size(800, 800)
    noFill()
def draw():
    try:
        image(zdjecie, height/2, width/2, 199, 199) # tylko tą linijkę sprawdzamy pod kątem błędu i więcej się tu nie powinno znaleźć
    except:
        stroke("#FF0000")
        text("Nie udalo sie wczytac obrazu", 100, 25)
    else:
        stroke("#0000FF")  
    finally:
        rect(height/2-1, width/2-1, 200, 200)
        
# 1,5pkt
