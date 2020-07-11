class OknoWiezienne(object):
    ilosc_wcisniec_wszystkich_krat_wszystkich_obiektow_tej_klasy = 0
    def __init__(self,bok):
        self.bok = bok
        self.wcisniety = False
        
    def rysuj(self, x, y):  
        self.x = x
        self.y = y
        rect(self.x, self.y, self.bok, self.bok)
        
    def zamknij(self, x, y, paski):
         OknoWiezienne.rysuj(self, x, y)
         space = self.bok/paski
         _xLinii_ = 0
         for pasek in range(0, paski):
            line(x+_xLinii_, y, x+_xLinii_, y+self.bok)
            _xLinii_ +=space
            
    def wcisnij(self):
        OknoWiezienne.ilosc_wcisniec_wszystkich_krat_wszystkich_obiektow_tej_klasy +=1
        self.wcisniety = not self.wcisniety
        if self.wcisniety:
            fill(255)
        else:
            fill(220)
def setup():
    size(500,500)
    global moje_okno_wiezienne
    moje_okno_wiezienne = OknoWiezienne(width/2)

def mouseClicked():
    moje_okno_wiezienne.wcisnij()
    
def mouseWheel(event):
    moje_okno_wiezienne.zamknij()
    print(moje_okno_wiezienne.zamkniecie)
    
def draw():
    background(120)
    moje_okno_wiezienne.rysuj(20,50)
    print(OknoWiezienne.ilosc_wcisniec_wszystkich_krat_wszystkich_obiektow_tej_klasy)
    
#0,75pkt
