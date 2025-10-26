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
    fruit_count = {}
    for fruit in basket:
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
    return fruit_count

final_counts = count_fruits(fruit_basket)
print(final_counts)



#practice 41

"""
#define log status
def is_critical(log_entry):
    for log in log_entry:
        if log["level"] == "ERROR":
            return True
        else:
            return False

#define categorize type
def categorize_log(log_entry):
    for log in log_entry:
        if "login" or "Password" or "locked" in log_entry["message"]:
            return "Security"
        elif "Payment" or "Credit card" in log_entry["message"]:
            return "Billing"
        else:
            return "General"

#main log analyze
def analyze_logs(log_list):
    #create level analyze
    level_count = {}
    error_message = []
    category_type_count = {}
    #log error count
    for logs in log_list:
        level_count[logs("level")] = level_count.get(logs("level"), 0) + 1
        return level_count
        #error message list
        if is_critical(log_list) == True:
            error_message.append("message")
        return error_message
        #log category type count dict
        if categorize_log(log_list):
            category_type_count[log_list] = category_type_count.get(logs, 0) + 1
        return category_type_count


logs = [
    {"timestamp": "2023-10-27T10:00:00Z", "level": "ERROR", "service": "auth-service", "message": "Failed login attempt for user 'test'"},
    {"timestamp": "2023-10-27T10:01:15Z", "level": "INFO", "service": "payment-service", "message": "Payment successful for user_123"},
    {"timestamp": "2023-10-27T10:02:30Z", "level": "WARNING", "service": "auth-service", "message": "Password for user 'admin' nearing expiration"},
    {"timestamp": "2023-10-27T10:03:00Z", "level": "ERROR", "service": "payment-service", "message": "Credit card payment failed for user_456"},
    {"timestamp": "2023-10-27T10:05:00Z", "level": "ERROR", "service": "auth-service", "message": "User account 'test' has been locked"},
    {"timestamp": "2023-10-27T10:06:45Z", "level": "DEBUG", "service": "recommendation-engine", "message": "Fetching recommendations for user_789"}
]

final_analyze = (logs)
print(final_analyze)
"""



#practice 40 revise
#helper function
def is_critical(log_entry):
    return log_entry['level'] == "ERROR"

def categorize_log(log_entry):
    message = log_entry['message']
    if "login" in message or "Password" in message or "locked" in message:
        return "Security"
    elif "Payment" in message or "Credit card" in message:
        return "Billing"
    else:
        return "General"

#main analyze funtion
def analyze_logs(log_entry):
    level_counts = {}
    critical_messages = []
    category_counts = {}    
    # level 
    for log in log_entry:
        level = log_entry['level']
        level_counts[level] = level_counts.get(level, 0) + 1
    #error message
        if is_critical(log):
            error_message.append(log['message'])
    #log type count
        category = categorize_log(log)
        category_counts[category] = category_counts.get(category, 0) + 1

    #report
    report = {
        "level_counts": level_counts,
        "critical_messages": critical_messages,
        "category_counts": category_counts
    }
    return report   



logs = [
    {"timestamp": "2023-10-27T10:00:00Z", "level": "ERROR", "service": "auth-service", "message": "Failed login attempt for user 'test'"},
    {"timestamp": "2023-10-27T10:01:15Z", "level": "INFO", "service": "payment-service", "message": "Payment successful for user_123"},
    {"timestamp": "2023-10-27T10:02:30Z", "level": "WARNING", "service": "auth-service", "message": "Password for user 'admin' nearing expiration"},
    {"timestamp": "2023-10-27T10:03:00Z", "level": "ERROR", "service": "payment-service", "message": "Credit card payment failed for user_456"},
    {"timestamp": "2023-10-27T10:05:00Z", "level": "ERROR", "service": "auth-service", "message": "User account 'test' has been locked"},
    {"timestamp": "2023-10-27T10:06:45Z", "level": "DEBUG", "service": "recommendation-engine", "message": "Fetching recommendations for user_789"}
]

def main_log_analyzer():
    report = analyze_logs(log)

    print("log level counts:")
    for level, count in report['level_counts']:
        print(f"    - {level}: {count}")
    for msg in reprot['critical_messages']:
        print(f"    - {msg}")
    for catagory, counts in report['category_counts']:
        print(f"    -{catagory}: {counts}")

if __name__ == "__main__":
    main_log_analyzer()

#practice 41


def calculate_average(scores):
    if not scores:
        return 0
    else:
        return avg_scores

def get_grade(average_score):
    if average_score >= 90:
        return 'A' 
    elif average_score >= 80:
        return 'B'
    elif average_score >= 70:
        return 'C'
    else:
        return 'F'

def check_attendance_award(attendance_percentage):
    if attendance_percentage == 100:
        return True
    else:
        return False

def generate_performance_reports(student_data_list):
    report_cards = []
    report_card = {}
    class_statistics = {}
    sum_score = 0
    perfect_attendance_count = 0
    for data in student_data_list:
        #avg score
        if calculate_average(data):
            sum_score = sum(data['scores'])
            avg_score = sum_score / len(data['scores'])
        #get grade
        grade_data = get_grade(avg_score)
        #attendance
        attend = check_attendance_award(data['attendance_percentage'])
        #report card dict
        report_card = {
            'name': data["name"], 
            'grade': grade_data, 
            'has_attendance_award': attend,
        }
        #append to report_cards = []
        if report_card:
            report_cards.append[report_card]
        
        