# ------chapter 2: functions--------

#practice 31

def add_two_numbers(i, j):
    result = i + j
    print(result)

add_two_numbers(5,3)
add_two_numbers(10,20)

#practice 32
def calculate_rectangle_area(width, height):
    result = width * height
    return result

area = calculate_rectangle_area(10, 5)
print(area)

#practice 33 improve

def calculate_rectangle_area(width, height):
    return width * height

area = calculate_rectangle_area(10, 5)
print(area)

#practice 34

"""def calculate_average(score_list):
    if score_list == None:                      #cannot afford [], division will be zero
        return 0
    else:
        return sum(score_list) / len(score_list)
"""        


score_list = [1, 2, 3, 4, 5]
average = calculate_average(score_list)
print(average)

#practice 34 revise

def calculate_average(score_list):
    if not score_list:              #which means score_list = [] empty, none = do not exist
        return 0
    else:
        return sum(score_list) / len(score_list)


score_list = [1, 2, 3, 4, 5]
average = calculate_average(score_list)
print(average)


#practice 35

def calculate_average(scores_list):
    if not scores_list:
        return 0
    else:
        return sum(scores_list) / len(scores_list)

students = [
    {"name": "Alice", "scores": [85, 92, 88]},
    {"name": "Bob", "scores": [78, 81, 86]},
    {"name": "Charlie", "scores": [95, 90, 93, 98]},
    {"name": "David", "scores": [60, 65, 70]},
    {"name": "Eva", "scores": [91, 89, 94]}
]

print("--- 學生平均分數報告 (重構後) ---")
for student in students:
    name = student["name"]
    scores = student["scores"]
    average_score = calculate_average(scores)

    print(f"{name} 的平均分數是: {average_score:.2f}")


#practice 36 todo: finish it

result = {}
vowel_count = 0

def analyze_text(text_input):
    char = text_input.split()
    char_count = len(char)
    word = text_input.split(' ')
    word_count = len(word)
    vowel = ["a", "e", "i", "o", "u"]
    if text_input in vowel:
        vowel_count += 1
    result.append(char_count, word_count, vowel_count)
    return result


#practice 36.1 warm up for def()

def create_greeting(name, hour):
    if hour < 12:
        # 函式應該「回傳」一個值，而不是直接印出
        return f"Good morning, {name}!"
    else:
        return f"Good afternoon, {name}!"

# 函式的「呼叫」應該在定義的外面，而不是裡面
morning_greeting = create_greeting("Bob", 9)
afternoon_greeting = create_greeting("Alice", 14)

# 印出函式回傳並儲存到變數中的結果
print(morning_greeting)
print(afternoon_greeting)



#practice 37


books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genres": ["Science Fiction", "Adventure"], "is_available": True},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "year": 1967, "genres": ["Magic Realism"], "is_available": False},
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "genres": ["Fantasy", "Adventure"], "is_available": True},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genres": ["Science Fiction", "Dystopian"], "is_available": True},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984, "genres": ["Science Fiction", "Cyberpunk"], "is_available": False}
]


#define is_classic(year), if year < 1980, return True
"""
def is_classic(year):
    return year < 1980    

def main():
    amount_is_classic = 0
    latest_book_year = None
    Science_Fiction_available = []


for book in books:
    #find amount of is_classic by using is_classic()
    if is_classic(book["year"]) == True:
        amount_is_classic += 1

    #find is_available == True, append to Science_Fiction_available = []
    if book["is_available"] == True:
        if "Science Fiction" in book["genres"]:
            Science_Fiction_available.append(book["title"])

    #find latest book, print name & year
    if book["year"] > latest_book_year:
        latest_book_year = book["year"]
        latest_year_book_title = book["title"]


print(f"classic books amount: {amount_is_classic}")
print(f"available science fiction books: {Science_Fiction_available}")
print(f"latest books: {latest_year_book_title} ({latest_book_year})")

"""

#practice 37 revise



books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genres": ["Science Fiction", "Adventure"], "is_available": True},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "year": 1967, "genres": ["Magic Realism"], "is_available": False},
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "genres": ["Fantasy", "Adventure"], "is_available": True},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genres": ["Science Fiction", "Dystopian"], "is_available": True},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984, "genres": ["Science Fiction", "Cyberpunk"], "is_available": False}
]

def is_classic(year):
    """Checks if a book is a classic (published before 1980)."""
    return year < 1980    

def main():
    """Main function to run the book analysis."""
    # 1. Initialize tracking variables *before* the loop starts.
    classic_count = 0
    available_scifi_titles = []
    newest_book = None # Use None to handle the first book correctly.

    # 2. Loop through the books to perform analysis.
    for book in books:
        # Call the helper function to check for classic books.
        if is_classic(book["year"]):
            classic_count += 1

        # Check for available Science Fiction books.
        # The check should be on the 'genres' list, not the dictionary keys.
        if book['is_available'] and "Science Fiction" in book['genres']:
            # .append() is a function and needs parentheses.
            available_scifi_titles.append(book['title'])

        # Find the newest book using the "king of the hill" algorithm.
        if newest_book is None or book['year'] > newest_book['year']:
            newest_book = book

    # 3. Print the final report *after* the loop is finished.
    print("--- Library Book Analysis Report ---")
    print(f"Number of classic books: {classic_count}")
    print(f"Available Science Fiction titles: {available_scifi_titles}")
    if newest_book:
        print(f"The newest book is: {newest_book['title']} ({newest_book['year']})")

# Standard entry point to run the main function.
if __name__ == "__main__":
    main()




#practice 38

def get_stock_status(stock_count):
    # 為了輸出美觀，將回傳值改為首字母大寫
    if stock_count == 0:
        return "Out of Stock"
    elif 0 < stock_count < 10:
        return "Low Stock"
    else:
        return "In Stock"

def is_on_sale(product):
    """檢查單一產品是否為特價品"""
    # 1. 函式應該接收整個 product 字典，才能取得 category 和 price
    category = product["category"]
    price = product["price"]

    if category == "Electronics" and price > 500:
        return True
    if category == "Books" and price > 50:
        return True
    
    return False

def analyze_inventory(products_list):
    """分析整個產品列表並回傳一份報告字典"""
    # 追蹤變數應在迴圈開始前初始化
    total_value = 0
    sale_items = []
    status_counts = {}

    for product in products_list:
        # 計算總價值
        total_value += product["price"] * product["stock"]

        # 2. 呼叫 is_on_sale 時，應傳入當前的 product 字典
        if is_on_sale(product):
            sale_items.append(product["name"])

        # 取得庫存狀態並更新計數
        status = get_stock_status(product["stock"])
        # .get(status, 0) 的意思是：取得 status 這個鍵的值，如果鍵不存在，就預設為 0
        status_counts[status] = status_counts.get(status, 0) + 1

    # 3. 建立報告和 return 必須在 for 迴圈結束之後
    #    這樣才能回傳包含所有產品分析的完整結果
    report = {
        "total_value": total_value,
        "sale_items": sale_items,
        "status_counts": status_counts
    }
    return report

products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 8},
    {"name": "Python 101", "category": "Books", "price": 45, "stock": 30},
    {"name": "Coffee Mug", "category": "Kitchenware", "price": 15, "stock": 0},
    {"name": "Gaming Mouse", "category": "Electronics", "price": 75, "stock": 25},
    {"name": "The Art of Code", "category": "Books", "price": 60, "stock": 5},
    {"name": "4K Monitor", "category": "Electronics", "price": 700, "stock": 12}
]

def main():
    """主程式進入點"""
    inventory_report = analyze_inventory(products)
    
    print("--- Inventory Analysis Report ---")
    print(f"Total Inventory Value: ${inventory_report['total_value']}")
    print(f"On-Sale Items: {inventory_report['sale_items']}")
    print("Stock Status Counts:")
    # 4. 存取字典的鍵需要用方括號 []
    for status, count in inventory_report['status_counts'].items():
        print(f"  - {status}: {count}")

if __name__ == "__main__":
    main()


#38 small practice 

# ------chapter 2: functions--------

#practice 31

def add_two_numbers(i, j):
    result = i + j
    print(result)

add_two_numbers(5,3)
add_two_numbers(10,20)

#practice 32
def calculate_rectangle_area(width, height):
    result = width * height
    return result

area = calculate_rectangle_area(10, 5)
print(area)

#practice 33 improve

def calculate_rectangle_area(width, height):
    return width * height

area = calculate_rectangle_area(10, 5)
print(area)

#practice 34

"""def calculate_average(score_list):
    if score_list == None:                      #cannot afford [], division will be zero
        return 0
    else:
        return sum(score_list) / len(score_list)
"""        


score_list = [1, 2, 3, 4, 5]
average = calculate_average(score_list)
print(average)

#practice 34 revise

def calculate_average(score_list):
    if not score_list:              #which means score_list = [] empty, none = do not exist
        return 0
    else:
        return sum(score_list) / len(score_list)


score_list = [1, 2, 3, 4, 5]
average = calculate_average(score_list)
print(average)


#practice 35

def calculate_average(scores_list):
    if not scores_list:
        return 0
    else:
        return sum(scores_list) / len(scores_list)

students = [
    {"name": "Alice", "scores": [85, 92, 88]},
    {"name": "Bob", "scores": [78, 81, 86]},
    {"name": "Charlie", "scores": [95, 90, 93, 98]},
    {"name": "David", "scores": [60, 65, 70]},
    {"name": "Eva", "scores": [91, 89, 94]}
]

print("--- 學生平均分數報告 (重構後) ---")
for student in students:
    name = student["name"]
    scores = student["scores"]
    average_score = calculate_average(scores)

    print(f"{name} 的平均分數是: {average_score:.2f}")


#practice 36 todo: finish it

result = {}
vowel_count = 0

def analyze_text(text_input):
    char = text_input.split()
    char_count = len(char)
    word = text_input.split(' ')
    word_count = len(word)
    vowel = ["a", "e", "i", "o", "u"]
    if text_input in vowel:
        vowel_count += 1
    result.append(char_count, word_count, vowel_count)
    return result


#practice 36.1 warm up for def()

def create_greeting(name, hour):
    if hour < 12:
        # 函式應該「回傳」一個值，而不是直接印出
        return f"Good morning, {name}!"
    else:
        return f"Good afternoon, {name}!"

# 函式的「呼叫」應該在定義的外面，而不是裡面
morning_greeting = create_greeting("Bob", 9)
afternoon_greeting = create_greeting("Alice", 14)

# 印出函式回傳並儲存到變數中的結果
print(morning_greeting)
print(afternoon_greeting)



#practice 37


books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genres": ["Science Fiction", "Adventure"], "is_available": True},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "year": 1967, "genres": ["Magic Realism"], "is_available": False},
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "genres": ["Fantasy", "Adventure"], "is_available": True},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genres": ["Science Fiction", "Dystopian"], "is_available": True},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984, "genres": ["Science Fiction", "Cyberpunk"], "is_available": False}
]


#define is_classic(year), if year < 1980, return True
"""
def is_classic(year):
    return year < 1980    

def main():
    amount_is_classic = 0
    latest_book_year = None
    Science_Fiction_available = []


for book in books:
    #find amount of is_classic by using is_classic()
    if is_classic(book["year"]) == True:
        amount_is_classic += 1

    #find is_available == True, append to Science_Fiction_available = []
    if book["is_available"] == True:
        if "Science Fiction" in book["genres"]:
            Science_Fiction_available.append(book["title"])

    #find latest book, print name & year
    if book["year"] > latest_book_year:
        latest_book_year = book["year"]
        latest_year_book_title = book["title"]


print(f"classic books amount: {amount_is_classic}")
print(f"available science fiction books: {Science_Fiction_available}")
print(f"latest books: {latest_year_book_title} ({latest_book_year})")

"""

#practice 37 revise



books = [
    {"title": "Dune", "author": "Frank Herbert", "year": 1965, "genres": ["Science Fiction", "Adventure"], "is_available": True},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "year": 1967, "genres": ["Magic Realism"], "is_available": False},
    {"title": "Harry Potter", "author": "J.K. Rowling", "year": 1997, "genres": ["Fantasy", "Adventure"], "is_available": True},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genres": ["Science Fiction", "Dystopian"], "is_available": True},
    {"title": "Neuromancer", "author": "William Gibson", "year": 1984, "genres": ["Science Fiction", "Cyberpunk"], "is_available": False}
]

def is_classic(year):
    """Checks if a book is a classic (published before 1980)."""
    return year < 1980    

def main():
    """Main function to run the book analysis."""
    # 1. Initialize tracking variables *before* the loop starts.
    classic_count = 0
    available_scifi_titles = []
    newest_book = None # Use None to handle the first book correctly.

    # 2. Loop through the books to perform analysis.
    for book in books:
        # Call the helper function to check for classic books.
        if is_classic(book["year"]):
            classic_count += 1

        # Check for available Science Fiction books.
        # The check should be on the 'genres' list, not the dictionary keys.
        if book['is_available'] and "Science Fiction" in book['genres']:
            # .append() is a function and needs parentheses.
            available_scifi_titles.append(book['title'])

        # Find the newest book using the "king of the hill" algorithm.
        if newest_book is None or book['year'] > newest_book['year']:
            newest_book = book

    # 3. Print the final report *after* the loop is finished.
    print("--- Library Book Analysis Report ---")
    print(f"Number of classic books: {classic_count}")
    print(f"Available Science Fiction titles: {available_scifi_titles}")
    if newest_book:
        print(f"The newest book is: {newest_book['title']} ({newest_book['year']})")

# Standard entry point to run the main function.
"""if __name__ == "__main__":
    main()"""




#practice 38

def get_stock_status(stock_count):
    # 為了輸出美觀，將回傳值改為首字母大寫
    if stock_count == 0:
        return "Out of Stock"
    elif 0 < stock_count < 10:
        return "Low Stock"
    else:
        return "In Stock"

def is_on_sale(product):
    """檢查單一產品是否為特價品"""
    # 1. 函式應該接收整個 product 字典，才能取得 category 和 price
    category = product["category"]
    price = product["price"]

    if category == "Electronics" and price > 500:
        return True
    if category == "Books" and price > 50:
        return True
    
    return False

def analyze_inventory(products_list):
    """分析整個產品列表並回傳一份報告字典"""
    # 追蹤變數應在迴圈開始前初始化
    total_value = 0
    sale_items = []
    status_counts = {}

    for product in products_list:
        # 計算總價值
        total_value += product["price"] * product["stock"]

        # 2. 呼叫 is_on_sale 時，應傳入當前的 product 字典
        if is_on_sale(product):
            sale_items.append(product["name"])

        # 取得庫存狀態並更新計數
        status = get_stock_status(product["stock"])
        # .get(status, 0) 的意思是：取得 status 這個鍵的值，如果鍵不存在，就預設為 0
        status_counts[status] = status_counts.get(status, 0) + 1

    # 3. 建立報告和 return 必須在 for 迴圈結束之後
    #    這樣才能回傳包含所有產品分析的完整結果
    report = {
        "total_value": total_value,
        "sale_items": sale_items,
        "status_counts": status_counts
    }
    return report

products = [
    {"name": "Laptop", "category": "Electronics", "price": 1200, "stock": 8},
    {"name": "Python 101", "category": "Books", "price": 45, "stock": 30},
    {"name": "Coffee Mug", "category": "Kitchenware", "price": 15, "stock": 0},
    {"name": "Gaming Mouse", "category": "Electronics", "price": 75, "stock": 25},
    {"name": "The Art of Code", "category": "Books", "price": 60, "stock": 5},
    {"name": "4K Monitor", "category": "Electronics", "price": 700, "stock": 12}
]

def main():
    """主程式進入點"""
    inventory_report = analyze_inventory(products)
    
    print("--- Inventory Analysis Report ---")
    print(f"Total Inventory Value: ${inventory_report['total_value']}")
    print(f"On-Sale Items: {inventory_report['sale_items']}")
    print("Stock Status Counts:")
    # 4. 存取字典的鍵需要用方括號 []
    for status, count in inventory_report['status_counts'].items():
        print(f"  - {status}: {count}")

if __name__ == "__main__":
    main()


# --- 字典計數小挑戰 ---

def count_characters(input_text):
    """計算字串中每個字元的出現次數（忽略大小寫和空格）。"""
    # 步驟 1: 準備一個空的「計分板」字典
    char_counts = {}

    # 步驟 2: 一個字一個字地檢查輸入的文字
    for original_char in input_text:
        # 步驟 3.1: 統一格式，將字元轉成小寫
        char = original_char.lower()

        # 步驟 3.2: 過濾雜訊，如果字元不是空格，才繼續
        if char != ' ':
            # 步驟 3.3: 核心！更新計分板
            # TODO: 在這裡寫下「看、算、寫」的那行關鍵程式碼
            #       char_counts[?] = char_counts.get(?, ?) + ?
            char_counts[char] = char_counts.get(char, 0) + 1
    # 步驟 4: 交出最終的計分板
    return char_counts

# --- 測試您的函式 ---
test_string = "Practice makes perfect"
frequency_report = count_characters(test_string)
print(f"\n--- Character Count Report for '{test_string}' ---")
print(frequency_report)



#practice 40

def count_fruits(basket):
    """計算一個列表中每種水果的出現次數。"""
    fruit_counts = {}
    for fruit in basket:
        fruit_counts[fruit] = fruit_counts.get(fruit, 0) + 1
    return fruit_counts

# --- 測試您的函式 ---
fruit_basket = [
    'apple', 'orange', 'apple', 'banana',
    'apple', 'grape', 'orange'
]
final_counts = count_fruits(fruit_basket)
print("\n--- Fruit Count Report ---")
print(final_counts)


# --- practice 41: System Log Analyzer ---

# --- Part 1: Helper Functions (Each works on a SINGLE log entry) ---

def is_critical(log_entry):
    """Checks if a single log entry has a level of 'ERROR'."""
    return log_entry['level'] == 'ERROR'

def categorize_log(log_entry):
    """Categorizes a single log entry based on its message content."""
    message = log_entry['message']
    if "login" in message or "Password" in message or "locked" in message:
        return "Security"
    elif "Payment" in message or "Credit card" in message:
        return "Billing"
    else:
        return "General"

# --- Part 2: Main Analysis Function ---

def analyze_logs(log_list):
    """Analyzes a list of logs and returns a summary report."""
    # 1. Initialize tracking variables before the loop
    level_counts = {}
    critical_messages = []
    category_counts = {}

    # 2. Loop through each log in the list
    for log in log_list:
        # Update level counts
        level = log['level']
        level_counts[level] = level_counts.get(level, 0) + 1

        # Check for critical errors and collect messages
        if is_critical(log):
            critical_messages.append(log['message'])

        # Categorize the log and update category counts
        category = categorize_log(log)
        category_counts[category] = category_counts.get(category, 0) + 1

    # 3. AFTER the loop, create and return the final report
    report = {
        "level_counts": level_counts,
        "critical_messages": critical_messages,
        "category_counts": category_counts
    }
    return report

# --- Main Execution Block ---

logs = [
    {"timestamp": "2023-10-27T10:00:00Z", "level": "ERROR", "service": "auth-service", "message": "Failed login attempt for user 'test'"},
    {"timestamp": "2023-10-27T10:01:15Z", "level": "INFO", "service": "payment-service", "message": "Payment successful for user_123"},
    {"timestamp": "2023-10-27T10:02:30Z", "level": "WARNING", "service": "auth-service", "message": "Password for user 'admin' nearing expiration"},
    {"timestamp": "2023-10-27T10:03:00Z", "level": "ERROR", "service": "payment-service", "message": "Credit card payment failed for user_456"},
    {"timestamp": "2023-10-27T10:05:00Z", "level": "ERROR", "service": "auth-service", "message": "User account 'test' has been locked"},
    {"timestamp": "2023-10-27T10:06:45Z", "level": "DEBUG", "service": "recommendation-engine", "message": "Fetching recommendations for user_789"}
]

def main_log_analyzer():
    """Main function to run the log analysis and print the report."""
    report = analyze_logs(logs)

    print("--- System Log Analysis Report ---")
    print("Log Level Counts:")
    for level, count in report['level_counts'].items():
        print(f"  - {level}: {count}")

    print("Critical Error Messages:")
    for msg in report['critical_messages']:
        print(f"  - {msg}")

    print("Log Category Counts:")
    for category, count in report['category_counts'].items():
        print(f"  - {category}: {count}")

# Standard entry point to run the main function
if __name__ == "__main__":
    # We call our new main function to avoid conflicts with previous ones
    main_log_analyzer()


# --- practice 42: Advanced Student Performance Report ---

# --- Part 1: Helper Functions ---

def calculate_average(scores):
    """Calculates the average of a list of scores."""
    # TODO: Handle the case of an empty list to avoid ZeroDivisionError.
    pass

def get_grade(average_score):
    """Returns a letter grade for a given average score."""
    # TODO: Use if/elif/else to return 'A', 'B', 'C', or 'F'.
    pass

def check_attendance_award(attendance_percentage):
    """Checks if a student deserves an attendance award."""
    # TODO: Return True if percentage is 100, otherwise False.
    pass

# --- Part 2: Main Analysis Function ---

def generate_performance_reports(student_data_list):
    """Analyzes student data and generates a list of report cards and class statistics."""
    # TODO: Initialize a list for report_cards and variables for class statistics.
    report_cards = []
    total_scores_sum = 0
    students_with_scores_count = 0
    perfect_attendance_count = 0

    # TODO: Loop through each student in student_data_list
        # TODO: Call helper functions to get average, grade, and award status.
        # TODO: Create a new 'report_card' dictionary for the student.
        # TODO: Append the new report_card to the report_cards list.
        # TODO: Update class statistics variables.

    # TODO: After the loop, calculate the final class average.

    # TODO: Create and return the final report dictionary with two main keys.
    final_report = {
        # "student_reports": ...,
        # "class_statistics": ...
    }
    return final_report

# --- Main Execution Block ---

student_data = [
    {"name": "Alice", "scores": [92, 88, 95], "attendance_percentage": 100},
    {"name": "Bob", "scores": [78, 81, 86], "attendance_percentage": 95},
    {"name": "Charlie", "scores": [100, 95, 98], "attendance_percentage": 100},
    {"name": "David", "scores": [65, 70, 72], "attendance_percentage": 88},
    {"name": "Eva", "scores": [], "attendance_percentage": 98}
]

def main_student_analyzer():
    """Main function to run the student analysis and print the report."""
    # TODO: Call generate_performance_reports and get the final_report.
    # TODO: Print the report in a user-friendly format.
    pass

if __name__ == "__main__":
    main_student_analyzer()


# --- practice 43: Interactive Shopping Cart ---


#original

"""
#test run
def find_item_in_cart(cart, item_name):
    """Finds an item in the cart by its name and returns it, or None if not found."""
    if not item_name in cart:
        return None
    else:
        return item_name


# --- Part 2: Main Feature Functions ---

def add_to_cart(cart, item_to_add):
    """Adds an item to the cart. If it exists, updates quantity; otherwise, adds the new item."""
    if find_item_in_cart(cart, item_to_add):
        cart.get("quantity", 0) + 1
    else:
        cart.get(item_to_add, 0) + 1

def calculate_total(cart):
    """Calculates the total cost of all items in the cart."""
    total_price = 0
    for value in cart:
        total_price += cart["quantity"] * cart["price"]
    return total_price

def main_shopping_cart():
    my_cart = []
    product1 = {"name": "Laptop", "price": 1200, "quantity": 1}
    product2 = {"name": "Coffee Mug", "price": 15, "quantity": 2}
    product3 = {"name": "Python 101", "price": 45, "quantity": 1}
    # Simulate adding items to the cart
    my_cart.append(add_to_cart(product1, "quantity"))
    my_cart.append(add_to_cart(product2, "quantity"))
    my_cart.append(add_to_cart(product1, "quantity"))
    #  Calculate the total and print the report
    calculate_total(my_cart)
    #  Print the final state of my_cart and the total cost.
    print("--- Shopping Cart State ---/n")
    print("Current Cart:")
    print(product1)
    print(product2)

if __name__ == "__main__":
    main_shopping_cart()



"""
#revise
# --- Part 1: Helper Function ---

def find_item_in_cart(cart, item_name):
    """Finds an item in the cart by its name and returns it, or None if not found."""
    # We must loop through the list of dictionaries.
    for item in cart:
        # Check the 'name' key inside each dictionary.
        if item['name'] == item_name:
            return item  # Return the entire dictionary if found.
    # If the loop completes without finding the item, return None.
    return None

# --- Part 2: Main Feature Functions ---

def add_to_cart(cart, item_to_add):
    """Adds an item to the cart. If it exists, updates quantity; otherwise, adds the new item."""
    # Call the helper function to see if an item with the same name is already in the cart.
    existing_item = find_item_in_cart(cart, item_to_add['name'])

    if existing_item:
        # If the item exists, just update its quantity.
        existing_item['quantity'] += item_to_add['quantity']
    else:
        # If it does not exist, add a *copy* of the new item to the list.
        # .copy() is important to avoid modifying the original product dictionary.
        cart.append(item_to_add.copy())

def calculate_total(cart):
    """Calculates the total cost of all items in the cart."""
    total_cost = 0
    # 'item' here is each dictionary in the cart list.
    for item in cart:
        # Access keys on the 'item' dictionary, not the 'cart' list.
        total_cost += item['price'] * item['quantity']
    return total_cost

# --- Part 3: Main Execution Block ---

def main_shopping_cart():
    """Main function to simulate shopping cart interactions."""
    my_cart = []

    product1 = {"name": "Laptop", "price": 1200, "quantity": 1}
    product2 = {"name": "Coffee Mug", "price": 15, "quantity": 2}

    # Simulate adding items. The function modifies my_cart directly.
    add_to_cart(my_cart, product1)
    add_to_cart(my_cart, product2)
    add_to_cart(my_cart, product1) # Add the same product again to test quantity update

    # Calculate the total and store the returned value.
    total = calculate_total(my_cart)

    print("--- Shopping Cart State ---")
    print("Current Cart:")
    for item in my_cart:
        print(f"- {item}")

    print(f"\nTotal Cost: ${total}")

if __name__ == "__main__":
    main_shopping_cart()


# --- Micro-Practice: Strengthening Core Function Skills ---

def find_book_author_by_title(book_list, title_to_find):
    """
    Finds a book in a list by its title and returns the author's name.
    """
    #  Loop through each 'book' (which is a dictionary) in the 'book_list'.
    #  Inside the loop, check if the current book's 'title' matches 'title_to_find'.
    #  If it matches, return the current book's 'author'.
    #  If the loop finishes and nothing was found, return the string "Not Found".
    for book in books:
        if book['title'] == title_to_find:
            return book['author']
    # This return statement is outside the loop. It only runs if the loop finishes without finding a match.
    return "Not Found"

# --- Test your micro-practice function ---

library = [
    {'title': 'Dune', 'author': 'Frank Herbert'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'Harry Potter', 'author': 'J.K. Rowling'}
]
  
author1 = find_book_author_by_title(library, '1984')
author2 = find_book_author_by_title(library, 'Neuromancer')


print(f"\nThe author of '1984' is: {author1}") # Expected: George Orwell
print(f"The author of 'Neuromancer' is: {author2}") # Expected: Not Found


# --- Micro-Practice 2: The Counter Pattern ---

def count_available_items(item_list):
    """Counts how many items in a list are marked as available."""
    # TODO: 1. Initialize a counter variable to 0.
    # TODO: 2. Loop through each 'item' in the 'item_list'.
    # TODO: 3. Inside the loop, check if item['is_available'] is True.
    # TODO: 4. If it is, increment the counter.
    # TODO: 5. After the loop finishes, return the final count.
    available_count = 0
    for item in item_list:
        if item['is_available'] == True
            available_count += 1
    return available_count


# --- Test your new micro-practice function ---

inventory = [
    {'name': 'Laptop', 'is_available': True},
    {'name': 'Coffee Mug', 'is_available': False},
    {'name': 'Mouse', 'is_available': True},
    {'name': 'Keyboard', 'is_available': True}
]
available_count = count_available_items(inventory)
print(f"\nNumber of available items: {available_count}") # Expected: 3


# --- Micro-Practice 3: The Collector Pattern ---

def get_available_item_names(item_list):
    available_names = []

    for item in item_list:

        if item['is_available']:

            available_names.append(item['name'])
    # 5. Return the final collected list
    return available_names

# --- Test your collector function ---

product_catalog = [
    {'name': 'Laptop', 'is_available': True},
    {'name': 'Coffee Mug', 'is_available': False},
    {'name': 'Mouse', 'is_available': True}
]
available_names_list = get_available_item_names(product_catalog)
print(f"\nNames of available items: {available_names_list}") # Expected: ['Laptop', 'Mouse']


# --- Micro-Practice 3.5: The Collector Pattern with List Comprehension ---

def get_available_item_names_comprehension(item_list):
    """Collects the names of all available items using a list comprehension."""
    # This single line does the same job as the 4-line loop in the previous exercise.
    # Syntax: [expression_to_collect for item in iterable if condition]
    return [item['name'] for item in item_list if item['is_available']]

# --- Test your comprehension function ---
available_names_comp = get_available_item_names_comprehension(product_catalog)
print(f"\nNames of available items (using comprehension): {available_names_comp}") # Expected: ['Laptop', 'Mouse']


# --- Micro-Practice 4: Function Collaboration Pattern ---

def is_eligible_for_bonus(employee):
    """Checks if a single employee is eligible for a bonus."""
    # A more robust and Pythonic way is to directly return the result of the boolean expression.
    # This ensures the function always returns either True or False.
    return employee['years'] > 5 and employee['rating'] >= 4

def get_bonus_recipients(employee_list):
    """Collects the names of all employees eligible for a bonus."""
    # Using a list comprehension is the most elegant way to solve this.
    # It reads like a sentence: "Collect the employee's name for each employee in the list
    # if that employee is eligible for a bonus."
    return [employee['name'] for employee in employee_list if is_eligible_for_bonus(employee)]

# --- Test your collaborating functions ---

employees = [
    {'name': 'Alice', 'years': 7, 'rating': 5}, # Eligible
    {'name': 'Bob', 'years': 4, 'rating': 5},   # Not eligible (years)
    {'name': 'Charlie', 'years': 6, 'rating': 3}, # Not eligible (rating)
    {'name': 'David', 'years': 8, 'rating': 4}  # Eligible
]
bonus_winners = get_bonus_recipients(employees)
print(f"\nBonus recipients: {bonus_winners}") # Expected: ['Alice', 'David']






