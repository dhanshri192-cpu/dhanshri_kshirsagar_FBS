from book import Book

class Bookstore:
    def __init__(self, filename="books.txt"):
        self.filename = filename

    def add_book(self):
        book_id = input("Enter Book ID: ")
        name = input("Enter Book Name: ")
        author = input("Enter Author: ")
        price = input("Enter Price: ")

        book = Book(book_id, name, author, price)

        with open(self.filename, "a") as file:
            file.write(str(book) + "\n")

        print("Book Added Successfully")





    def view_books(self):
        try:
            with open(self.filename, "r") as file:
                print("\n--- Book List ---")
                for line in file:
                    bid, name, author, price = line.strip().split(",")
                    print(bid, name, author, price)
        except FileNotFoundError:
            print("No books found")




    def search_book(self):
        try:
            with open(self.filename, "r") as file:
                books = file.readlines()
        except FileNotFoundError:
            print("No books available")
            return

        attempts = 0

        while attempts < 2:
            book_id = input("Enter Book ID: ")
            found = False

            for line in books:
                bid, name, author, price = line.strip().split(",")
                if bid == book_id:
                    print("Book Found:", bid, name, author, price)
                    found = True
                    break

            if found:
                return

            attempts += 1
            print("Book ID not found!")

        print("No more attempts left.")

    

    



    def update_book(self):
        book_id = input("Enter Book ID to Update: ")
        updated = False

        with open(self.filename, "r") as file:
            books = file.readlines()

        with open(self.filename, "w") as file:
            for line in books:
                bid, name, author, price = line.strip().split(",")
                if bid == book_id:
                    name = input("New Name: ")
                    author = input("New Author: ")
                    price = input("New Price: ")
                    file.write(f"{bid},{name},{author},{price}\n")
                    updated = True
                else:
                    file.write(line)

        if updated:
            print("Book Updated")
        else:
            print("Book ID Not Found")


            

    def delete_book(self):
        book_id = input("Enter Book ID to Delete: ")
        deleted = False

        with open(self.filename, "r") as file:
            books = file.readlines()

        with open(self.filename, "w") as file:
            for line in books:
                bid = line.split(",")[0]
                if bid != book_id:
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print("Book Deleted")
        else:
            print("Book ID Not Found")
 
 
 
 
 
    