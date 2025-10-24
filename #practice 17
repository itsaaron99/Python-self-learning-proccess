#practice 17
scores = [2, 1, 3, 0, 4, 2]

if scores:
    highest_score = scores[0]
    for score in scores:
        if score > highest_score:
            highest_score = score
    print(f"highest score is: {highest_score}")
else:
    print("the score list is empty.")    


#practice 18 add user search for price interval
"""
import sys
names = ["蘋果", "香蕉", "櫻桃", "橘子"]
prices = [5, 3, 10, 4]
quantities = [20, 40, 4, 35]

highest_price = 0
lowest_price = 0
result_items_info = []

try:
    lowest_price = input("please enter the minimum price of research:")
    highest_price = input("please enter the maximum price of research:")
    lowest_price_int = int(lowest_price)
    highest_price_int = int(highest_price)
    for i in prices:
        if lowest_price_int <= prices[i] <= highest_price_int:
            result_items_info.append((names(i), prices(i), quantities(i)))
except:
    print("invalid entered, please try again")
    sys.exit()

if result_items_info:
    for name, price, quantity in result_items_info:
        print(f"item: {name}, price: {price}, quantity: {quantity}")
else:
    print("item not exist, please try again.")
"""

#pracice 18 revise
#revise for i in range(len(prices)): 索引
# revice result_items_info.append((names[i], prices[i], quantities[i]))
import sys
names = ["蘋果", "香蕉", "櫻桃", "橘子"]
prices = [5, 3, 10, 4]
quantities = [20, 40, 4, 35]

highest_price = 0
lowest_price = 0
result_items_info = []

try:
    lowest_price = input("please enter the minimum price of research:")
    highest_price = input("please enter the maximum price of research:")
    lowest_price_int = int(lowest_price)
    highest_price_int = int(highest_price)
    for i in range(len(prices)):
        if lowest_price_int <= prices[i] <= highest_price_int:
            result_items_info.append((names[i], prices[i], quantities[i]))
except:
    print("invalid entered, please try again")
    sys.exit()

if result_items_info:
    for name, price, quantity in result_items_info:
        print(f"item: {name}, price: {price}, quantity: {quantity}")
else:
    print("item not exist, please try again.")


#practice 19
students = ["Aaron", "Betty", "Chris", "David", "Eva"]

#solution 1
for i, name in enumerate(students):
    print(f"{i+1}. {name}")

#solution 2
for i, name in enumerate(students, start=1):
    print(f"{i}, {name}")



#practice 20 
todo_list = ["寫報告", "買牛奶", "去運動"]
print(f"初始待辦事項: {todo_list}")
todo_list.remove("買牛奶")
todo_list.append("回復郵件")
print(f"{todo_list}")


#practice 21
"""
gradebook = [
    ["Alice", 85, 92, 88],
    ["Bob", 78, 81, 86],
    ["Charlie", 95, 90, 93],
    ["David", 60, 65, 70],
    ["Eva", 91, 89, 94]
]

highest_avg_score = 0.00
honor_student = []
top_student_name = ""
avg_score = 0

for student_data in gradebook:
    name = student_data[0]
    scores = student_data[1:]
    avg_score = sum(scores) / len(score)
    if avg_score > highest_avg_score:
        highest_avg_score = avg_score
        top_student_name = name
        if highest_avg_score >= 90:
            honor_student_name = name
            honor_student.append(honor_student_name)
print(f"{name}'s avarage score is: {avg_score}")
print(f"highest score student is {top_student_name}, average score is {highest_avg_score}")
print(f"honor students list: {honor_student}")

"""

#practice 21 revise

gradebook = [
    ["Alice", 85, 92, 88],
    ["Bob", 78, 81, 86],
    ["Charlie", 95, 90, 93],
    ["David", 60, 65, 70],
    ["Eva", 91, 89, 94]
]

highest_avg_score = 0.00
honor_student = []
top_student_name = ""
avg_score = 0

for student_data in gradebook:
    name = student_data[0]
    scores = student_data[1:]
    current_avg = sum(scores) / len(scores)
    print(f"{name}'s avarage score is: {current_avg}")

    if current_avg > highest_avg_score:
        highest_avg_score = current_avg
        top_student_name = name
    if current_avg >= 90:
        honor_student_name = name
        honor_student.append(name)
print("------------------------")        
print(f"highest score student is {top_student_name}, average score is {highest_avg_score}")
print("------------------------")        
print(f"honor students list: {honor_student}")




#pratice 22 
orders = [
    ["A001", 2500, True, "TW"],
    ["A002", 150, False, "USA"],
    ["A003", 4500, True, "TW"],
    ["A004", 800, True, "JP"],
    ["A005", 6200, False, "TW"]
]

total_revenue = 0
vip_order_count = 0
oversea_orders = []
highest_order = 0

for order_data in orders:
    order_number = order_data[0]
    order_amount = order_data[1]
    total_revenue += order_amount
    is_vip = order_data[2]
    country = order_data[3]
    #vip amount
    if is_vip == True:
        vip_order_count += 1
    #oversea orders
    if country != "TW":
        oversea_orders.append(order_number)
    #highest order
    if order_amount > highest_order:
        highest_order = order_amount
         
print(f"Total revenue: {total_revenue}")
print(f"vip member amount: {vip_order_count}")
print(f"oversea orders: {oversea_orders}")
print(f"highest order amount: {highest_order}")



#practice 23
"""
employees = [
    ["E01", "ENG", 12, 4.5],
    ["E02", "MKT", 8, 3.5],
    ["E03", "ENG", 5, 4.8],
    ["E04", "ADM", 15, 3.0],
    ["E05", "MKT", 2, 4.0],
    ["E06", "ENG", 10, 5.0]
]

department_data = 0
eng_count = 0
total_serve_years = 0
senior_emp = []
lowest_peform = 5.1

for emp in employees:
    #avg serve years
    emp_id = emp[0]
    department = emp[1]
    serve_year = emp[2]
    perform_score = emp[3]
    total_serve_years += serve_year
    avg_serve_years = total_serve_years / len(emp)
    #senior emp count
    if serve_year >= 10:
        senior_emp.append(emp_id)
    #departmant eng count
    if department == "ENG":
        eng_count += 1
    if perform_score < lowest_peform:
        lowest_peform = perform_score
        lowest_emp_id = emp[0]

print(f"ENG deparment amount: {eng_count}")
print(f"average employee serve years: {avg_serve_years}")
print(f"senior employees: {senior_emp}")
print(f"lowest performance employee: {lowest_emp_id}, score: {lowest_peform}")
"""


#practice 23 revise

#avg years revise, should be calculated outside the for()

    
employees = [
    ["E01", "ENG", 12, 4.5],
    ["E02", "MKT", 8, 3.5],
    ["E03", "ENG", 5, 4.8],
    ["E04", "ADM", 15, 3.0],
    ["E05", "MKT", 2, 4.0],
    ["E06", "ENG", 10, 5.0]
]

department_data = 0
eng_count = 0
total_serve_years = 0
senior_emp = []
lowest_score = employees[0][3]
lowest_performer_id = employees[0][0]

for emp in employees:
    #avg serve years
    emp_id = emp[0]
    department = emp[1]
    serve_year = emp[2]
    perform_score = emp[3]
    #sum of serve years for all emp
    total_serve_years += serve_year
    #senior emp count
    if serve_year >= 10:
        senior_emp.append(emp_id)
    #departmant eng count
    if department == "ENG":
        eng_count += 1
    if perform_score < lowest_score:
        lowest_score = perform_score
        lowest_performer_id = emp_id

avg_serve_years = total_serve_years / len(employees)   #range should be all employees


print(f"ENG deparment amount: {eng_count}")
print(f"average employee serve years: {avg_serve_years}")
print(f"senior employees: {senior_emp}")
print(f"lowest performance employee: {lowest_performer_id}, score: {lowest_score}")



#practice 24
"""
product = {

    "name": "蘋果",
    "price": 15,
    "in_stock": True,
}

if product["in_stock"] == True:
    print(f"product name: {product["name"]}, price: ${product["price"]}")
    print(f"product is in stocked")
else:
    print(f"product name: {product["name"]}, price: ${product["price"]}")
    print("product sold out")   
"""     

#practice 24 revise
product = {

    "name": "蘋果",
    "price": 15,
    "in_stock": True,
}

print(f"product name: {product["name"]}, price: ${product["price"]}")
if product["in_stock"]:
    print("product is in_stock")
else:
    print("product sold out")

#practice 25

product = {
    "name": "蘋果",
    "price": 15,
    "in_stock": True,
}

product["price"] = 20
product["origin"] = "Taiwan"
print(f"{product}")

#practice 26

shopping_cart = {
    "蘋果": 5,
    "香蕉": 3,
    "牛奶": 1
}

for product, amount in shopping_cart.items():
    print(f"product: {product}, amount: {amount}")



#practice 27

products = [
    {"name": "蘋果", "price": 20, "quantity": 50},
    {"name": "香蕉", "price": 10, "quantity": 100},
    {"name": "牛奶", "price": 80, "quantity": 20},
    {"name": "麵包", "price": 35, "quantity": 30}
]

max_value = 0
max_value_product = 0
total_products_value = 0
for products_data in products:
    products_value = products_data["price"] * products_data["quantity"]
    total_products_value += products_value
    if products_value > max_value_product:
        max_value_product = products_value
        max_value_product_name = products_data["name"]

print(f"total stock value: {total_products_value}")
print(f"highest value item: {max_value_product_name}") 


#practice 28

students = [
    {"name": "Alice", "scores": [85, 92, 88]},
    {"name": "Bob", "scores": [78, 81, 86]},
    {"name": "Charlie", "scores": [95, 90, 93, 98]},
    {"name": "David", "scores": [60, 65, 70]},
    {"name": "Eva", "scores": [91, 89, 94]}
]
#outputs
highest_score = 0
highest_score_student = ""
std_best_students = []

for student_data in students:

#avg scores for each students
    score_list = student_data["scores"]
    name_list = student_data["name"]
    avg_score_each = sum(score_list) / len(score_list)
    print(f"{name_list} average score is {avg_score_each}")
# find highest score and student
    student_max_score = max(score_list)
    if student_max_score > highest_score:
        highest_score = student_max_score
        highest_score_student = name_list
# append std high score studnts into "std_best_students = []"
    if min(score_list) >= 85:
        std_best_students.append(name_list)

print("-----------------------")
print(f"highest score student: {highest_score_student}, score is {highest_score}")
print(f"best students list: {std_best_students}")



#pracrice 29

menu = [
    {"name": "牛肉麵", "price": 150, "category": "主食", "ingredients": ["麵條", "牛肉", "青菜"]},
    {"name": "滷肉飯", "price": 50, "category": "主食", "ingredients": ["米飯", "豬肉", "醬油"]},
    {"name": "燙青菜", "price": 40, "category": "小菜", "ingredients": ["青菜", "醬油"]},
    {"name": "蛋花湯", "price": 30, "category": "湯品", "ingredients": ["雞蛋", "青蔥", "水"]},
    {"name": "親子丼", "price": 180, "category": "主食", "ingredients": ["米飯", "雞肉", "雞蛋", "洋蔥"]}
]

#todo: 
#find how many main dish in category
#calculate all avg meal price
#create a [], which store meals with any ingredients of eggs in it
#find the most expensive meal on menu

main_dish_count = 0
total_price = 0
avg_price = 0
egg_ingredients_meals = []
most_expensive_meal = 0

for dish in menu:
    menu_names = dish["name"]
    meal_price = dish["price"]
    category_data = dish["category"]
    ingredients_data = dish["ingredients"]
    #average meal price
    total_price += meal_price
    avg_price = total_price / len(menu)   #除以總菜單長度 非dish
    #main dish amount
    if "主食" in category_data:
        main_dish_count += 1
    #find meals with eggs in it   
    if "雞蛋" in ingredients_data:
        egg_ingredients_meals.append(menu_names)
    # find most expensive meal
    if meal_price > most_expensive_meal:
        most_expensive_meal = meal_price
        most_expensive_meal_name = menu_names
print("-----reprot-----")
print(f"main dish amount: {main_dish_count}")
print(f"avarage meal price: ${avg_price}")
print(f"meals with egg: {egg_ingredients_meals}")
print(f"most expensive meal: {most_expensive_meal_name}, price: ${most_expensive_meal}")


#practice 30

posts = [
    {"post_id": 1, "author": "Alice", "content": "Learning Python is fun!", "likes": 150, "tags": ["#python", "#coding"]},
    {"post_id": 2, "author": "Bob", "content": "Just had a great coffee.", "likes": 50, "tags": ["#coffee", "#lifestyle"]},
    {"post_id": 3, "author": "Alice", "content": "Dictionaries are so useful.", "likes": 250, "tags": ["#python", "#datastructures"]},
    {"post_id": 4, "author": "Charlie", "content": "My new project is live!", "likes": 300, "tags": ["#dev", "#project"]},
    {"post_id": 5, "author": "Alice", "content": "What's everyone's favorite food?", "likes": 80, "tags": ["#food", "#question"]}
]

#todo
#find tags amount of #python
#calculate total "likes"
#find most likes post, print its "content", "author", "likes"
#find "author" == "Alice" and likes > 100, append to a new list

python_tags_amount = 0
total_likes = 0
most_like = 0
alice_popular_post = []

for post in posts:
    id_data = post["post_id"]
    author_data = post["author"]
    content_data = post["content"]
    likes_data = post["likes"]
    tags_data = post["tags"]
    #find tags amount of #python
    if "#python" in tags_data:
        python_tags_amount += 1
    #calculate total "likes"
    total_likes += likes_data
    #find most likes post, print its "content", "author", "likes"
    if likes_data > most_like:
        most_like = likes_data
        viral_post = post   #storevthe whole dict
    #   most_like_content = content_data
    #   most_like_author = author_data
    #find "author" == "Alice" and likes > 100, append to a new list
    if author_data == "Alice" and likes_data > 100:
        alice_popular_post.append(content_data)
print("-------------report----------------")        
print(f"amount of python tag: {python_tags_amount}")
print(f"total likes of the post: {total_likes}")
print(f"most popular post content: '{most_like_content}' (author: {most_like_author}), likes: {most_like}")
print(f"alice's popular posts (likes over 100): {alice_popular_post}")
        



