def setup():
    zdjecie = loadImage("pies.jpg")
    global zdjecie
    size(800, 800)
def draw():
    rect(height/2-1, width/2-1, 200, 200)
    try:
        stroke("#0000FF")
        image(zdjecie, height/2, width/2, 199, 199)
        
    except:
        stroke("#FF0000")
        text("Nie udalo sie wczytac obrazu", 100, 25)
