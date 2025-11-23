#OOP STUDY AND PRACTICE
"""students = [

{

'name': 'Alice',

'grades': {'math': 90, 'science': 88, 'history': 92}

}],

def calculate_student_gpa(student):

#Calculates the Grade Point Average (GPA) for a single student.

def find_top_student(student_list):

#Finds the student with the highest GPA in a list of students.

top_student = find_top_student(students)

print(f"The student with the highest GPA is: {top_student}")
"""

class Student:
#define Attibutes, add the name and grades in itself
    def __init__(self, name, grades): #Constructor
        self.name = name
        self.grades = grades
        print(f"student {self.name}'s data has been updated")
# define Methods
# this method belongs to "class Student", which can count it's own GPA        
    def calculate_gpa(self):
        if not self.grades:
            return 0.0
#self.grades will get it's own grade
        total_points = sum(self.grades.values())
        num_subjects = len(self.grades)
        return total_points / num_subjects
#create actual object        
student1 = Student(name='Alice', grades={'math': 90, 'science': 88, 'history': 92})
student2 = Student(name='Bob', grades={'math': 85, 'science': 95, 'history': 80})
students = [student1, student2]

def find_top_student(student_list):
    if not student_list:
        return None
    top_student_object = max(student_list, key=lambda student: student.calculate_gpa())
    return top_student_object

top_student = find_top_student(students)
if top_student:
    print(f"Highest GPA student is: {top_student.name}")
    print(f"Its GPA is {top_student.calculate_gpa():.2f}")

#test
alice_gpa = student1.calculate_gpa()
print(f"{student1.name}'s GPA is {alice_gpa:.2f}")

bob_gpa = student2.calculate_gpa()
print(f"{student2.name}'s GPA is {bob_gpa:.2f}")


#practice guessinggame
""" # 檔案：procedural_course.py

# 用一個字典來代表整門課程的資料
course_data = {
    'course_name': '資料結構',
    'students': []  # 學生名單，裡面會放一個個學生字典
}

# 函式1：在課程中加入一位學生
def add_student(course, student_name, grade):
    將一個學生字典新增到課程的 students 列表中
    course['students'].append({'name': student_name, 'grade': grade})
    print(f"已將 {student_name} 加入 {course['course_name']} 課程。")

# 函式2：計算課程的平均成績
def calculate_average(course):
    計算這門課所有學生的平均成績
    students = course['students']
    if not students:
        return 0.0
    total_grades = sum(student['grade'] for student in students)
    return total_grades / len(students)

# 函式3：找出最高分的學生
def get_top_student(course):
    找出這門課成績最高的學生字典
    students = course['students']
    if not students:
        return None
    # 這裡我們再次用到了 key 和 lambda！
    top_student_dict = max(students, key=lambda s: s['grade'])
    return top_student_dict

# --- 操作流程 ---
print(f"--- 開始管理課程：{course_data['course_name']} ---")
add_student(course_data, '張三', 88)
add_student(course_data, '李四', 92)
add_student(course_data, '王五', 75)

print("\n--- 課程統計 ---")
avg = calculate_average(course_data)
print(f"全班平均分數: {avg:.2f}")

top_student = get_top_student(course_data)
if top_student:
    print(f"最高分的學生是: {top_student['name']} ({top_student['grade']}分)") """


class Course:
    def __init__(self, name, students=None):
        self.name = name
        if students is None:
            self.students = []
        else:
            self.students = students   
        print(f"--- created course: {self.name} ---")

    def add_student(self, students_name: str, grade: float):
        students_data = {'name': students_name, 'grade': grade}
        self.students.append(students_data)
        print(f"added {students_name} into {self.name}")

    def calculate_average(self) -> float:
        if not self.students:
            return 0.0
        total_grades = sum(student['grade'] for student in self.students)
        return total_grades / len(self.students)
    
    def get_top_student(self) -> dict:
        if not self.students:
            return None
        #using lambda due to use one of the key in the dict to compare the highest scores
        top_student_dict = max(self.students, key=lambda s: s['grade'])
        return top_student_dict

    def __repr__(self):
        return f"Course(name='{self.name}', students={len(self.students)})"

if __name__ == "__main__":
    ds_course = Course(name='data structure')

    ds_course.add_student('Chang', 88)
    ds_course.add_student('Lee', 92)
    ds_course.add_student('Wang', 75)

    avg = ds_course.calculate_average()
    top_student = ds_course.get_top_student()

    print(f"---Report---")
    print(f"course name: {ds_course.name}")
    print(f"class average score: {avg:.2f}")

    if top_student:
        print(f"top student is: {top_student['name']} ({top_student['grade']})")

    print(f"\ninformation of course: {ds_course}")



#practice re-design projects to class
#Practice 20: E-commerce Order Summarizer

"""
# 檔案：/Users/aaron/Desktop/w1/# ------chapter 4: data structures--------.py

def summarize_orders(order_items):
    
    #Groups a list of order items by order_id and calculates a summary for each order.
    
    orders_summary = {}
    for item in order_items:
        order_id = item['order_id']
        # Use setdefault to get or create the summary dict for this order.
        order_summary = orders_summary.setdefault(order_id, {'total_amount': 0, 'items': []})
        
        order_summary['total_amount'] += item['price'] * item['quantity']
        order_summary['items'].append(item['product_name'])
    return orders_summary

# Test data
order_data = [
    {'order_id': 'O-1001', 'product_name': 'Laptop', 'quantity': 1, 'price': 1200},
    {'order_id': 'O-1002', 'product_name': 'Mouse', 'quantity': 2, 'price': 25},
    # ... more items
]

order_summary_report = summarize_orders(order_data)
pprint.pprint(order_summary_report)
"""

class OrderProcessor:
    def __init__(self, order_items):
        self.items = order_items


    def generate_summary(self) -> dict:
        orders_summary = {}
        for item in self.items:
            order_id = item['order_id']
            order_summary = orders_summary.setdefault(order_id, {'total_amount': 0, 'items': []})
            order_summary['total_amount'] += item['price'] * item['quantity']
            order_summary['items'].append(item['product_name'])
        return orders_summary

    def get_order_details(self, order_id) -> dict:
        order_report = self.generate_summary()
        for order in order_report:
            if order.keys(order_id) == order_id:
                return order['order_id']

if __name__ == "__main__":
    order_data = [
        {'order_id': 'O-1001', 'product_name': 'Laptop', 'quantity': 1, 'price': 1200},
        {'order_id': 'O-1002', 'product_name': 'Mouse', 'quantity': 2, 'price': 25},
        {'order_id': 'O-1001', 'product_name': 'Keyboard', 'quantity': 1, 'price': 75},
        {'order_id': 'O-1003', 'product_name': 'Monitor', 'quantity': 1, 'price': 300},
        {'order_id': 'O-1002', 'product_name': 'Webcam', 'quantity': 1, 'price': 50},
    ]

    # 1. 建立一個訂單處理器物件，並傳入原始資料
    processor = OrderProcessor(order_items=order_data)

    # 2. 呼叫方法來產生完整的匯總報告
    full_summary = processor.generate_summary()
    
    print("--- 完整訂單匯總報告 ---")
    pprint.pprint(full_summary)

    # 3. (加分題) 取得特定訂單的詳細資訊
    print("\n--- 查詢特定訂單 O-1001 ---")
    order_1001_details = processor.get_order_details('O-1001')
    if order_1001_details:
        pprint.pprint(order_1001_details)
    

# 檔案：/Users/aaron/Desktop/w1/# ------chapter 4: data structures--------.py
"""
def generate_student_report_cards(roster, scores):
    Merges student roster information with assignment scores to create
    a list of comprehensive report cards.
    # --- Step 1: Group all scores by student ID ---
    scores_by_student = {}
    for record in scores:
        scores_by_student.setdefault(record['student_id'], []).append(record['score'])

    # --- Step 2: Create report cards by merging with the roster ---
    report_cards = []
    for student in roster:
        id_ = student['student_id']
        student_scores = scores_by_student.get(id_, [])
        
        if not student_scores:
            avg_score = 0
        else:
            avg_score = sum(student_scores) / len(student_scores)
            
        status = 'Pass' if avg_score >= 60 else 'Fail'

        report_card = {
            'student_id': id_,
            'name': student['name'],
            'avg_score': avg_score,
            'status': status
        }
        report_cards.append(report_card)
    return report_cards


# --- Test your function ---
student_roster = [
    {'student_id': 's001', 'name': 'Alice'},
    {'student_id': 's002', 'name': 'Bob'},
    {'student_id': 's003', 'name': 'Charlie'}, # A student with no scores
]

assignment_scores = [
    {'student_id': 's001', 'score': 85},
    {'student_id': 's002', 'score': 58},
    {'student_id': 's001', 'score': 92},
    {'student_id': 's002', 'score': 61},
]
"""
import pprint


class ReportCardGenerator:
    def __init__(self, roster, scores):
        self.roster = roster
        self.scores = scores

    def _group_scores(self):
        scores_by_student = {}
        for record in self.scores:
            scores_by_student.setdefault(record['student_id'], []).append(record['score'])
        return scores_by_student

    
    def generate_reports(self):
        scores_by_student = self._group_scores()
        report_cards = []
        for student in self.roster:
            id_ = student['student_id']
            student_scores = scores_by_student.get(id_, [])
            
            if not student_scores:
                avg_score = 0
            else:
                avg_score = sum(student_scores) / len(student_scores)
                
            status = 'Pass' if avg_score >= 60 else 'Fail'

            report_card = {
                'student_id': id_,
                'name': student['name'],
                'avg_score': avg_score,
                'status': status
            }
            report_cards.append(report_card)
        return report_cards




if __name__ == "__main__":
    student_roster = [
        {'student_id': 's001', 'name': 'Alice'},
        {'student_id': 's002', 'name': 'Bob'},
        {'student_id': 's003', 'name': 'Charlie'},
    ]

    assignment_scores = [
        {'student_id': 's001', 'score': 85},
        {'student_id': 's002', 'score': 58},
        {'student_id': 's001', 'score': 92},
        {'student_id': 's002', 'score': 61},
    ]

    report_generator = ReportCardGenerator(roster=student_roster, scores = assignment_scores)
    final_reports = report_generator.generate_reports()
    print("\n--- Student Report Cards (OOP) ---")
    pprint.pprint(final_reports)


# 範例資料結構
#inventory_data = {
    #"P001": {"name": "筆記型電腦", "price": 1200.00, "stock": 10},
    #"P002": {"name": "滑鼠", "price": 25.50, "stock": 50},
    # ... 更多商品
#}

class InventoryManager():
    def __init__(self):
        self.products = {}
    
    def add_product(self, product_id: str, name: str, price: float, initial_stock: int):
        if product_id in self.products:
            print("product already exist")
            return

        self.products[product_id] = {
            'name': name,
            'price': price,
            'stock': initial_stock
        }
        print(f"added product: {name}, ID: {product_id}")

        

    def update_stock(self, product_id: str, quantity_change: int):
        #check if product exists
        if product_id not in self.products:
            print("product: {product_id} not exist")
            return
        current_stock = self.products[product_id]['stock']
        if quantity_change < 0 and current_stock + quantity_change < 0:
            print(f"not enough stock in product: {product_id}")
        self.products[product_id]['stock'] += quantity_change



    def get_product_details(self, product_id: str) -> dict | None:
        return None if not self.products[product_id] else self.products.get(product_id)


    def list_all_products(self):
        if not self.products:
            print("there're no products in stock")
            return
        # 印出表頭
        # 'ID' 靠左佔 10 格, '名稱' 靠左佔 15 格, '價格' 靠右佔 10 格, '庫存' 靠右佔 5 格
        print(f"{'ID':<10} | {'名稱':<15} | {'價格':>10} | {'庫存':>5}")
        print("-" * 45) # 印出一條分隔線
        # 遍歷所有商品並印出內容
        for product_id, details in self.products.items():
            # product_id 靠左佔 10 格
            # details['name'] 靠左佔 15 格
            # details['price'] 靠右佔 9 格，並顯示到小數點後兩位
            # details['stock'] 靠右佔 5 格
            print(f"{product_id:<10} | {details['name']:<15} | ${details['price']:>9.2f} | {details['stock']:>5}")            
            

    def calculate_total_value(self) -> float:
        total_value = 0
        for details in self.products.values():
            total_value += details['price'] * details['stock']
        return total_value


    def __repr__(self) -> str:
        total_value = self.calculate_total_value()
        return f"InventoryManager(products={len(self.products)}, total_value=${total_value:.2f})"


# --- 這是你完成 Class 後，期望的執行效果 ---

if __name__ == "__main__":
    # 1. 建立一個庫存管理系統物件
    my_shop_inventory = InventoryManager()

    # 2. 新增商品
    my_shop_inventory.add_product("P001", "筆記型電腦", 1200.00, 10)
    my_shop_inventory.add_product("P002", "滑鼠", 25.50, 50)
    my_shop_inventory.add_product("P003", "鍵盤", 75.00, 20)
    my_shop_inventory.add_product("P001", "重複的筆電", 100.00, 5) # 測試重複新增

    # 3. 查詢商品
    print("\n--- 查詢商品 P002 ---")
    mouse_details = my_shop_inventory.get_product_details("P002")
    if mouse_details:
        print(f"商品名稱: {mouse_details['name']}, 價格: {mouse_details['price']}, 庫存: {mouse_details['stock']}")
    else:
        print("商品 P002 不存在。")

    # 4. 更新庫存
    print("\n--- 更新庫存 ---")
    my_shop_inventory.update_stock("P001", -2) # 賣出2台筆電
    my_shop_inventory.update_stock("P003", 5)  # 鍵盤入庫5個
    my_shop_inventory.update_stock("P004", 10) # 測試不存在的商品
    my_shop_inventory.update_stock("P002", -60) # 測試庫存不足

    # 5. 列出所有商品
    print("\n--- 目前所有商品庫存 ---")
    my_shop_inventory.list_all_products()

    # 6. 計算總價值
    total_value = my_shop_inventory.calculate_total_value()
    print(f"\n--- 總庫存價值: ${total_value:.2f} ---")

    # 7. (加分題) 看看 __repr__ 的效果
    print(f"\n庫存管理系統物件資訊: {my_shop_inventory}")



"""
class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.initial_balance = initial_balance
        self.transactions = []
        print(f'Welocome {user}! your account has been added.')

    def deposit(self, amount: float):
        if amount < 0:
            print("Invalid amount of deposit, please try again.")
            return None

        self.initial_balance += amount

        current_record_deposit = {}
        current_record_deposit[type] = 'deposit'
        current_record_deposit[amount] = self.initial_balance

        self.transactions.append(current_record_deposit)
        print(f"{current_record_deposit[type]} ${amount} successfully executed. Initial balance: ${self.initial_balance}")


    def withdraw(self, amount: float):
        if amount < 0:
            print("Invalid amount of deposit, please try again.")
            return None

        if amount > self.initial_balance:
            print(f"Not enough amount to execute the withdraw, please try again")
            return None

        self.initial_balance -= amount
        
        current_record_withdraw = {}
        current_record_withdraw[type] = 'withdraw'
        current_record_withdraw[amount] = self.initial_balance

        self.transactions.append(current_record_withdraw)
        print(f"{current_record_withdraw[type]} ${amount} successfully executed. Initial balance: ${self.initial_balance}")



    def get_balance(self) -> float:
        return self.initial_balance

    def get_transaction_history(self):
        if not self.transactions:
            print("No recored exists")
        for record in self.transactions:
            return record

    def __repr__(self) -> str:
        return f"BankAccount(holder='{self.account_holder}', balance=${self.balance:.2f})"
"""

class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []
        print(f'Welcome {self.account_holder}! your account has been added.')

    def deposit(self, amount: float):
        if amount <= 0:
            print("Invalid amount of deposit, please try again.")
            return

        self.balance += amount

        transaction_record = {'type': 'deposit', 'amount': amount}
        self.transactions.append(transaction_record)
        print(f"Deposit of ${amount:.2f} successful. New balance: ${self.balance:.2f}")


    def withdraw(self, amount: float):
        if amount <= 0:
            print("Invalid amount of deposit, please try again.")
            return 

        if amount > self.balance:
            print(f"Insufficient funds. Current balance is ${self.balance:.2f}.")
            return

        self.balance -= amount
        
        transaction_record = {'type': 'withdraw', 'amount': amount}
        self.transactions.append(transaction_record)
        print(f"Withdrawal of ${amount:.2f} successful. New balance: ${self.balance:.2f}")



    def get_balance(self) -> float:
        return self.balance

    def get_transaction_history(self):
        if not self.transactions:
            print("No transaction records exist.")
            return
        
        print(f"\n--- Transaction History for {self.account_holder} ---")
        # 修正：應該遍歷並印出每一筆紀錄，而不是只回傳第一筆
        for record in self.transactions:
            print(f"- Type: {record['type']:<8} | Amount: ${record['amount']:.2f}")

    def __repr__(self) -> str:
        return f"BankAccount(holder='{self.account_holder}', balance=${self.balance:.2f})"

if __name__ == "__main__":
    print("--- 🧪 Starting BankAccount Test Cases ---")

    # 1. 建立一個新帳戶
    print("\n[Test 1: Account Creation]")
    my_account = BankAccount("Aaron", 100.0)
    print(f"Account created: {my_account}")
    print(f"Initial balance check: ${my_account.get_balance():.2f}")
    print("-" * 20)

    # 2. 測試有效的存款
    print("\n[Test 2: Valid Deposit]")
    my_account.deposit(50.0)
    print("-" * 20)

    # 3. 測試有效的提款
    print("\n[Test 3: Valid Withdrawal]")
    my_account.withdraw(30.0)
    print("-" * 20)

    # 4. 測試無效的存款 (負數)
    print("\n[Test 4: Invalid Deposit (Negative Amount)]")
    my_account.deposit(-20.0)
    print(f"Balance after invalid deposit: ${my_account.get_balance():.2f}")
    print("-" * 20)

    # 5. 測試餘額不足的提款
    print("\n[Test 5: Insufficient Funds Withdrawal]")
    my_account.withdraw(200.0) # 目前餘額應為 100 + 50 - 30 = 120
    print(f"Balance after failed withdrawal: ${my_account.get_balance():.2f}")
    print("-" * 20)

    # 6. 顯示最終的交易紀錄
    my_account.get_transaction_history()

    print("\n--- ✅ All Test Cases Completed ---")



"""
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
        self.name = name
        self.books = []

    def add_book(self, book_object: Book):
        print(f"Added {self.name} in library successfully")
        return self.book.append(book_object)


    def check_out_book(self, title: str):
        if title not in self.title:
            return f"Sorry, {title} doesn't exist"
        for books in self.books:
            if books == title and self.is_check_out == False:
                print(f"Successfully borrowed {self.title}.")
                self.is_check_out = True
            else:
                print(f"Sorry, {self.title} has been borrowed")

    def return_book(self, title: str):
        if title in self.books and self.is_check_out == False:
            return f"{title} is already exist in library, don't need to return"
        for books in self.books:
            if books == title:
                print(f"{title} has been returned")
                self.is_check_out = False


    def list_available_books(self):
        for books in self.books:
            if books.is_check_out == False:
                print(f"{books.title}")

"""


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


class Product:
    """ 
    Represents a single product with its details.

    Attributes:
        name (str): The name of the product.
        product_id (str): The unique identifier for the product.
        price (float): The price of the product.
        stock (int): The available quantity in stock.
    """
    def __init__(self, name: str, product_id: str, price: float, stock: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.stock = stock

    def __repr__(self) -> str:
        if self.stock > 0:
            return f"<Product: {self.name} (ID: {self.product_id}), Price: ${self.price}, Stock: {self.stock}>"
        else:
            return f"<Product: {self.name} (ID: {self.product_id}), Price: ${self.price} (Out of Stock)>"

class ShoppingCart:
    """     
    Attribute:
        Set "product_list" as a dict.
        example: product_list = {'P001': {'product': <Product Object>, 'quantity': 2}}

    Funtions of ShoppingCart:
        1. Add product
        2. Calculate total prices
        3. Remove and add products (if adding same products, should update its amount,
        instead of adding another product in list)
    """

    def __init__(self):
        self.product_list = {}

    def add_product(self, product: Product, quantity: int = 1) -> None:
        p_id = product.product_id

        if p_id in self.product_list:
            self.product_list[p_id]['quantity'] += quantity
            print(f"updated {product.name} quantity to {self.product_list[p_id]['quantity']}")
        else:
            self.product_list[p_id] = {'product': product, 'quantity': quantity}
            print(f"Added {quantity} {product.name}s into shopping cart successfully.")

    def remove_product(self, product_id: str, quantity: int = 1) -> None:
        if product_id in self.product_list:
            self.product_list.pop(product_id)
            print(f"{product_id} has been removed from shopping cart")
        else:
            print(f"{product_id} does not exist in the shopping cart")

    def calculate_total(self) -> float:
        total_price = 0
        for products in self.product_list.values():
            total_price += products['product'].price * products['quantity']
        return total_price

    def __repr__(self):
        num_items = sum(item_data['quantity'] for item_data in self.product_list.values())
        num_unique_products = len(self.product_list)
        total_value = self.calculate_total()
        return f"<ShoppingCart: {num_unique_products} unique products, {num_items} total items, Total: ${total_value:.2f}>"

if __name__ == "__main__":
    laptop = Product("laptop", "P001", 1200.00, 10)
    mouse = Product("mouse", "P002", 25.50, 50)
    keyboard = Product("keyboard", "P003", 75.00, 20)


    my_cart = ShoppingCart()

    print("--- 🧪 測試 add_product 方法 ---")
    my_cart.add_product(laptop, 1)
    my_cart.add_product(mouse, 2)
    my_cart.add_product(laptop, 1) # 再次加入筆電，應該更新數量
    my_cart.add_product(keyboard, 3)
    my_cart.add_product(mouse, 1) # 再次加入滑鼠，應該更新數量

    print(f"\n目前購物車狀態: {my_cart}")
    print(f"購物車總金額: ${my_cart.calculate_total():.2f}")

    print("\n--- 測試移除商品 ---")
    my_cart.remove_product("P001", 1)
    print(f"\n移除商品後購物車狀態: {my_cart}")
    print(f"移除商品後總金額: ${my_cart.calculate_total():.2f}")

    class Coffee:

        def __init__(self, name: str, size: str, price: float):
            self.name = name
            self.size = size
            self.price = price

        def __repr__(self) -> str:
            return f"<Coffee: {self.size} {self.name}, ${self.price}>"


class CoffeeShop:
    """ 
    represent a coffee shop, with shop name and coffee menu
    """
    def __init__(self, name):
        self.name = name
        self.menu = []
    
    def add_to_menu(self, coffee: Coffee) -> None:
        self.menu.append(coffee)

    def display_menu(self) -> None:
        print(f"--- Welcome to {self.name}! ---")
        print("--- Menu ---")
        if not self.menu:
            print("Sorry, the menu is empty right now.")
            return
        for item in self.menu:
            print(f"- {item.size} {item.name}: ${item.price:.2f}")
        print("------------")

    def take_order(self, coffee_name: str, quantity: int) -> None:
        for order in self.menu:
            if order.name == coffee_name:
                total_price = order.price * quantity
                print(f"Order confirmed: {quantity} x {order.name}. Total is ${total_price:.2f}")
                return
        print(f"Sorry, we don't have '{coffee_name}' on our menu.")

if __name__ == "__main__":
    #add objects of coffee
    latte_m = Coffee("Latte", "Medium", 4.50)
    latte_l = Coffee("Latte", "Large", 5.50)
    americano = Coffee("Americano", "Medium", 3.75)

    #create a coffee shop
    my_shop = CoffeeShop("Gemini's Cafe")

    #adding coffe into menu
    my_shop.add_to_menu(latte_m)
    my_shop.add_to_menu(latte_l)
    my_shop.add_to_menu(americano)

    #test methods
    my_shop.display_menu()

    print("\n--- Taking Orders ---")
    my_shop.take_order("Latte", 2)       # should success
    my_shop.take_order("Mocha", 1)       # should fail
    my_shop.take_order("Americano", 3)   # should success

