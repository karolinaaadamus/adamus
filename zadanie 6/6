class Kwadrat(object):
    def __init__(self, bok):
        self.bok = bok
    def sketch(self, x, y):
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
       
class PasiastyKwadrat(Kwadrat):
    def sketchPasiasty(self, x, y, paski):
        Kwadrat.sketch(self, x, y)
        space = self.bok/paski
        _xLinii_ = 0
        for pasek in range(0, paski):
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
           
class NiebieskiKwadrat(Kwadrat):
    def sketch(self, x, y):
        fill(255)
        super(NiebieskiKwadrat, self).sketch(x, y)
        stroke("#0000ff")
        ySpace = self.bok / 7
        while y + ySpace < y + self.bok:
            line(x, y + ySpace, x + self.bok, y + ySpace)
            ySpace += self.bok / 7
           
def setup():
    size(500, 500)
    niebieski1 = NiebieskiKwadrat(25.0)
    niebieski1.sketch(250, 250)
   
    niebieski2 = NiebieskiKwadrat(100.0)
    niebieski2.sketch(375, 375)
