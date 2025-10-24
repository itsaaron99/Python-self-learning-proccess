class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_check_out = False 

    def __repr__(self) -> str:
        if self.is_check_out == False:
            return f"<Book: {self.title} by {self.author} (Available)>"
        else:
            return f"<Book: {self.title} by {self.author} (Checked Out)>"


class Library:
    def __init__(self, name: str):
        self.name = name #name of library
        self.books = [] #books of library

    def add_book(self, book_object: Book):
        self.books.append(book_object)
        print(f"Added {book_object.title} in library successfully") 


    def check_out_book(self, title: str):
        for book in self.books:
            # match the title first
            if book.title == title: 
                if not book.is_check_out:
                    book.is_check_out = True
                    print(f"Borrowed {title} successfully")
                else:
                    print(f"{title} has been borrowed")
                return
        print(f"{title} doesn't exist")


    def return_book(self, title: str):
        for book in self.books:
            if book.title == title:
                if book.is_check_out:
                    book.is_check_out = False
                    print(f"Return {title} successfully")
                # 使用 else 來確保兩種情況只會發生一種
                else:
                    print(f"{title} hasn't been borrowed, don't need to return")
                return

        print(f"{title} doesn't exist")


    def list_available_books(self):
        avalible_books = []
        for book in self.books:
            if not book.is_check_out:
                avalible_books.append(book)

        if not avalible_books:
            print(f"All books are borrowed")
        else:
            for book in avalible_books:
                print(book)

if __name__ == "__main__":
    city_library = Library("市立圖書館")
    book1 = Book("哈利波特", "J.K. Rowling")
    book2 = Book("沙丘", "Frank Herbert")
    book3 = Book("1984", "George Orwell")

    # --- 測試案例 ---
    print("--- 🧪 開始圖書館系統測試 ---")

    # 1. 將書本加入館藏
    city_library.add_book(book1)
    city_library.add_book(book2)
    city_library.add_book(book3)

    # 2. 列出所有可借閱的書
    city_library.list_available_books()

    # 3. 測試借書流程
    print("\n--- 測試借書 ---")
    city_library.check_out_book("沙丘")      # 成功借出
    city_library.check_out_book("沙丘")      # 借第二次，應顯示已被借出
    city_library.check_out_book("不存在的書") # 應顯示沒有此書

    # 4. 再次列出可借閱的書 (沙丘應該不見了)
    city_library.list_available_books()

    # 5. 測試還書流程
    print("\n--- 測試還書 ---")
    city_library.return_book("沙丘")      # 成功歸還
    city_library.return_book("哈利波特")   # 應顯示已在館內

    # 6. 最終檢查所有可借閱的書 (沙丘應該回來了)
    city_library.list_available_books()

    print("\n--- ✅ 所有測試案例完成 ---")
