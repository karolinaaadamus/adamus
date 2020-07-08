import unittest

class Library(): 
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook): 
        if requestedBook in self.availableBooks: 
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self): 
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook):
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")
 
class Customer(): 
    book = "" 
    haveBook = False
    def requestBook(self, book): # klient może zapytać o książę
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook = True
        return self.book
    def returnBook(self): # albo zwrócić jeśli posiada
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False
 
def setup():
    size(220,100)
    if __name__ == '__main__':
        unittest.main()
   
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) # do wypożyczania
    rect(100,40,100,20) # do zwracania
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)
 
def mouseClicked(): 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Madzia.requestBook("Naocznosc")) 
        if mouseY >40 and mouseY <60:
            library.addBook(Madzia.returnBook())
 
class tests(unittest.TestCase):
    def test1(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        self.assertEqual(library.availableBooks, ["Naocznosc", "Sens Sztuki", "Harry Potter"])
    def test2(self):
        Madzia = Customer()
        self.assertTrue(isinstance(Madzia, Customer)) # zamiast używać pól prywatnych, lepiej użyć metody do teg oprzeznaczonej, któa zresztą wystąpiłą w przykłądowym zadaniu 7 ode mnie
    def test3(self):
        books = ["Naocznosc", "Sens Sztuki", "Harry Potter"]
        library = Library(books)
        self.assertFalse(library.availableBooks == [])
        
if __name__ == '__main__':
    unittest.main()
    
#1,25pkt
