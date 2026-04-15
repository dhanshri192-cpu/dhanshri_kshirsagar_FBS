from bookstore import Bookstore

class Admin:
    def __init__(self):
        self.store = Bookstore()
        self.menu()

    def menu(self):
        while True:
            print("\n--- Book Management System ---")
            print("1. Add Book")
            print("2. View Books")
            print("3. Search Book")
            print("4. Update Book")
            print("5. Delete Book")
            print("6. Exit")

            choice = input("Enter Choice: ")

            if choice == "1":
                self.store.add_book()
            elif choice == "2":
                self.store.view_books()
            elif choice == "3":
                self.store.search_book()
            elif choice == "4":
                self.store.update_book()
            elif choice == "5":
                self.store.delete_book()
            elif choice == "6":
                print("Exiting Admin Panel...")
                break
            else:
                print("Thank you!")
               
