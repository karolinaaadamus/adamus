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
    
class Parrot(Pet):
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        text('chrrrupki!', random(50, width-70), random(50, height-50))
        return 'chrrrupki!'
    
    def obrazek(self):
        image(loadImage("parrot.jpg"),  0, 0, width, height)
    
    def __add__(self, other): 
        return self.name + ' i ' + other.name
        
        
        
def setup():
    size(600, 600)
    textSize(20)
    
    zielonka = Parrot('Zielonka')
    rex = Dog('Rex') 
    skrypcik = Cat('Skrypcik')
    global list_of_pets
    list_of_pets = [zielonka, rex, skrypcik] 
    print(zielonka + rex) 
    
    zielonka.obrazek()


    
def draw():
    pass
    
def mouseClicked():
    for pet in list_of_pets:
        pet.speak() 
        
        if isinstance(pet, Dog):
            pet.gimmePaw()
        
