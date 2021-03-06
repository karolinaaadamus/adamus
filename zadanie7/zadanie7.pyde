from abc import ABCMeta, abstractmethod 
class Pet():
    __metaclass__=ABCMeta 
    @abstractmethod 
    def speak(self): 
        super().__init__()
        return 'no sound'
    
class Cat(Pet): 
    def __init__(self, name):
        self.name = name
    def speak(self): 
        text('meow', random(50, width-70), random(50, height-50))
        return 'meow'
    
class Dog(Pet):
    def __init__(self, name):
        self.name = name
    def speak(self):
        text('woof', random(50, width-70), random(50, height-50))
        return 'woof'
    def gimmePaw(self):
        image(loadImage("lapa.png"), random(50, width-70), random(50, height-100))
    def __add__(self, other): 
        return self.name[0]+ ' i ' + other.name[0]
    
class Mouse(Pet):
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        text('pipipi', random(50, width-70), random(50, height-50))
        return 'pipipi')
    
    def obrazek(self):
        image(loadImage("mouse.jpg"),  0, 0, width, height)
    
    def __add__(self, other): 
        return self.name + ' pipipi ' + other.name
        
        
        
def setup():
    size(600, 600)
    textSize(20)
    
    parszywek  = mouse('Parszywek')
    rex = Dog('Rex') 
    skrypcik = Cat('Skrypcik')
    global list_of_pets
    list_of_pets = [parszywek, rex, skrypcik] 
    print(parszywek + rex) 
    
    parszywek.obrazek()


    
def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() 
        
        if isinstance(pet, Dog):
            pet.gimmePaw()


# 1,25pkt
# Praca jest identyczna włącznie z nazwamizwierząt i zakrzyknięciem o chrupki z programem Adriana Mikołajczuka. 
