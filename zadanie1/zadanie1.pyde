def setup():
    size(700, 700)
    c = color(255,200,200)
    stroke(c)
    fill(c)
def draw():
    rectMode(CORNER)
    if mousePressed :
        rect (mouseX, mouseY, width, height)
    else:
        clear()
# 2pkt
