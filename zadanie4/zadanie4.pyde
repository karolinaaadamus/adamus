add_library('pdf')

def setup():
    global img, moustache, hat
    size(425,520)
    img = loadImage("dowod.jpg")
    imageMode(CORNER)
    beginRecord(PDF, "dowodpdf.pdf")
    moustache = loadImage("moustache.png")
    hat = loadImage("hat.png")
    background(0)
def draw():
    global img, moustache, hat
    image(img,20,20,400,500)
    if key == "d":
        image(moustache,150,280,150 ,200)
        
    elif key == "a":
        image(hat,0,40,450,200)
        

def mousePressed():
    endRecord() # umieszczenie tego po kliknięciu sprawia, że co klatkę dorysowują sie kolejne warstwy obrazów.. można to sprawdzić po tym ,że im dłuzęj trwa program, tym cięższy będzie plik wynikowy.
    exit()
    
# 2 pkt
