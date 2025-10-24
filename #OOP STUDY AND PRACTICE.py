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
"""
__init__(self)
用途：建構子 (Constructor)。這是物件的「出生證明」。每當你寫 my_shop = InventoryManager() 時，這個方法就會被自動呼叫。
職責：初始化物件的內部狀態。在這裡，它的工作是建立一個空的字典 self.products。這就像給你的商店一個全新的、空白的庫存帳本，準備好記錄商品。
2. add_product(self, ...)
用途：新增商品。這是向庫存帳本中添加一筆新紀錄的方法。
職責：
防衛性檢查：if product_id in self.products: 檢查這個商品 ID 是否已經存在。如果存在，就印出錯誤訊息並用 return 提前結束，防止覆蓋資料。
建立巢狀資料：self.products[product_id] = { ... } 這是最關鍵的一步。它使用傳入的 product_id 變數（例如 "P001"）作為外層字典的鍵，並將商品的其他資訊打包成一個新的內層字典作為值。
3. update_stock(self, ...)
用途：更新庫存。處理商品的賣出（減少庫存）或進貨（增加庫存）。
職責：
存在性檢查：先確認要更新的商品是否存在於庫存中。
庫存充足性檢查：在減少庫存前，必須檢查 if current_stock + quantity_change < 0。這能防止庫存變成負數，確保了資料的正確性。
更新值：如果所有檢查都通過，它會精準地找到 self.products[product_id]["stock"] 這個位置，並更新它的值。
4. get_product_details(self, ...)
用途：安全地查詢商品。
職責：使用字典的 .get() 方法。這個方法非常安全，如果 product_id 存在，它會回傳對應的商品字典；如果不存在，它會回傳 None，而不會像 self.products[product_id] 那樣直接報錯。
5. list_all_products(self)
用途：生成報告。以人類易讀的格式，將整個庫存清單漂亮地印出來。
職責：遍歷 self.products 字典，並使用 f-string 的格式化功能（例如 f"{'ID':<10}"）來對齊文字，產生一個整齊的表格。
6. calculate_total_value(self)
用途：數據分析。計算整個商店庫存的總價值。
職責：遍歷 self.products.values()（所有內層的商品字典），將每個商品的 price * stock 相加，最後回傳總和。
7. __repr__(self)
用途：開發者友善的物件表示。
職責：定義當你直接 print(my_shop_inventory) 時，應該顯示什麼內容。它提供了一個關於物件當前狀態的快速快照，例如有多少種商品、總價值是多少，這在除錯時非常有用。
"""

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

