# EXERCISE 6 - LIBRARY MANAGEMENT SYSTEM
# Problem Statement: Write a Library class with no_of_books and books as two instance variables. Write a program to create a library from this Library class and show how you can print all books, add a book and get the number of books using different methods. Show that your program doesn't persist the books after the program is stopped!



from time import sleep

class Library:
  def __init__(self):
    self.books = ["Motivation beyond", "Success of life", "Nation matters", "Exactly coffee"]
    self.no_of_books = len(self.books)

  
  def printBooks(self):
    if len(self.books)<1:
      print("\nThere is no book in the library")
    else:
      print("\nAll the books in the library are :")
      i = 1
      for items in self.books:
        print(f"{i}) {items}")
        i = i + 1

  
  def addBooks(self, new_book):
    self.books.append(new_book)
    self.no_of_books += 1
    print(f"\nYou have added a book '{new_book}' in the library\n")

  
  def checkBooks(self):
    print("\nThe total number of books in the library are :", self.no_of_books, "\n")
    # print(self.no_of_books)

  
  def equalBooks(self):
    if len(self.books)==self.no_of_books:
      print("equal\n")

  
  def libraryInfo(self):
    print("Call the following methods/functions for the following tasks :\n1) printBooks() to print all the books in the library\n2) addBooks(new_book) to add a book in the library\n3) checkBooks() to check total number of books in the library\n")
    sleep(2)


reader = Library()
reader.libraryInfo()
# reader.printBooks()
# reader.checkBooks()
# reader.addBooks("Real beauty")
# reader.addBooks("The last life")
# reader.checkBooks()
# reader.printBooks()
# reader.equalBooks()