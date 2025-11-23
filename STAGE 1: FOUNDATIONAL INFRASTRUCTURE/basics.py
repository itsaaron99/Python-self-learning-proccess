#BASIC

#practice 1 
my_age = "30"
print(f"(my age is {my_age} years old)")

#practice 2
my_height = float("64.7")
print(f"(my height is {my_height} kg)")

#practice 3
my_favor_food = "steak"
print(f"(my fav food is {my_favor_food})")

#practice 4
is_student = True
print(f"(is student: {is_student})")

#practice 5 input

"""error
name = "aaron"
input(name)
print(f"(我的名字是: {name} !)")
print(f"name 型態是: {type(name)}")
"""

#revise
your_name = input(str("你的名字是?"))
print(your_name)
print(f"name type: {type(your_name)}")
name_int = int(your_name)   #change to int
result = name_int + 10    #then do calculation
print(result)      #show result



ur_luk_no = input("what's your luk no?")
print(ur_luk_no)
print(f"ur_luk_no type: {type(ur_luk_no)}")


#Operations

#practice 1

num1 = 20000
num2 = 100000000
result = num1 + num2
print(f"my monthly income is {result}")


#practice 2
num3 = float(15555.7)
num4 = float(17.7)
result = num3 / num4
print(result)


#practice 3
num5 = 2**3
print(num5)



#Comparison Operators


#practice 1
x = 10
y = 5

result1 = x == y
print(result1)

result2 = x != y
print(result2)

result3 = x > y
print(result3)

result4 = x < y
print(result4)

result5 = x >= y
print(result5)

result6 = x <= y
print(result6)

#practice 2 

name1 = "apple"
name2 = "banana"
result7 = name1 > name2
result8 = name1 < name2
print(result7)
print(result8)

#practice 3

age = 18
result = age >= 18
print(result)



#Logical Operators

#practice 1

is_sunny = True
is_warm = False
result1 = is_sunny and is_warm
print(result)

#practice 2
result2 = is_sunny or is_warm
print(result2)

#practice 3
"""result3 = is_sunny; not is_warm
print(result3)"""

#practice3 revise
is_sunny = not is_sunny
print(is_sunny)

#practice4
"""user_age = 20
has_licence = True
if user_age >= 18 and has_licence:
    print("user is availible to drive")
else:
    print("user cannot drive")
"""

#practice 4 revise
user_age = 20
can_drive = user_age >=18
has_licence = True
if can_drive and has_licence:
    print("user is availible to drive")
else:
    print("user cannot drive")


#practice 5
is_student = True
is_weekday = True
elder_age = 67
can_take_discount1 = elder_age >= 65 and is_weekday
can_take_discount2 = is_student and is_weekday
if can_take_discount1 or can_take_discount2:
    print("user availible take discount")
else:
    print("user cannot get account")



#practice 6

"""vip_member = True
family_ticket = True
child_age = input("Please enter child age: ")   #wait for user enter age
result = print(int(child_age))      #result must be int
result < 12 = True

priority_access1 = vip_member or sameday_ticket
priority_access2 = result and family_ticket
if priority_access1 and priority_access2:
    print("your same day ticket is availible")
else:
    print("you don't have access to priority Access")
"""

#revise
vip_member = True
family_ticket = True
sameday_ticket = True
child_age = input("Please enter child age: ")   #wait for user enter age
determine_child_age_under_12 = False   #初始化 child_age 是否符合家庭套票優惠的條件

#判斷當輸入年齡格式不正確
try:
    actual_child_age = int(child_age)
    if 0 <= actual_child_age < 12: # 應該比較 actual_child_age，且年齡可以等於0
        determine_child_age_under_12 = True # 如果符合條件，則更新為 True
except ValueError:
    print("Invalid age input. Assuming no qualifying child for family package.")
    
priority_access1 = vip_member or sameday_ticket
priority_access2 = determine_child_age_under_12 and family_ticket
if priority_access1 or priority_access2:
    print("You are available for priority access.") # 修正拼字
else:
    print("You are not available for priority access.") # 修正拼字


#conditional statements

#practice 1 "if" condition

number = 5
if number > 0:
    print(f"{number} is a positive number.")


#practice 2 "if-else" condition

"""user_age = input(int("Please enter your age"))
if user_age >= 18:
    print("you are legal adult")
else:
    print("you are not a adult")
"""


#use try-expect
#practice 1
age_input_str = input("please enter your age")
try:
    age_int = int(age_input_str)
    if age_int >= 18:
        print("you are a legal adult")
    else:
        print("you are not a adult")
except ValueError:
    print("that is nat a valid number, please try again")


#practice 2
#加入條件 0~100
"""secret_number = 7
user_input_num = input("Please try a number between 0~100 ")
try:
    user_input_num_int = int(user_input_num)
    0 <= user_input_num_int <= 100
    if user_input_num_int == secret_number:
        print("Congratulations, you guessed it!")
    else:
        print("Sorry, that's not it.")
except ValueError:
    print("Please enter a valid number!")
"""
#revise practice 2 for adding conditions in number 0~100

secret_number = 7
user_input_num = input("Please try a number between 0~100 ")
try:
    user_input_num_int = int(user_input_num)
    if 0 <= user_input_num_int <= 100:
        if user_input_num_int == secret_number:
            print("Congratulations, you guessed it!")
        else:
            print(f"Sorry, that's not it, the secret number is {secret_number}")
    else:
        print("The number you entered is not between 0 and 100.")    
except ValueError:
    print("Please enter a valid number!")
 

 #practice 3 if-elif-else condition

number = 10
if number > 0:
    print("the number is positive")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")

#practice 4 nest conditions
correct_username = "admin"
correct_password = "passsword123"
user_input_username = input("please enter username: ")
if user_input_username == correct_username:
    print("user name exist, please enter your password")
    user_input_password = input("please enter password")
    if user_input_password == correct_password:
        print(f"Login successful, welcome {correct_username} !")
    else:
        print("invalid password, please try again.")
else:
    print(f"user name{user_input_username} not found, please try again.")


#practice 5 nest conditions
#line 296, 297 using invalid def of Y/N, it shouldn't be int(), should be str()
#can transfer y/n through .lower(), for user enter "y" or "yes"
#try-except: if condition is to make sure user entering the right value, should add "ValueERROR" after except
"""user_age = input("please enter your age")
try:
    user_age_int = int(user_age)
    if 0 <= user_age_int < 12:
        print("Ticket price: $5")
    elif 12 <= user_age_int <= 64:
        is_student = input("are you a student? Y/N")  
        is_student_int = int(is_student)
        if is_student_int == "y" or "Y":
            print("Ticket price: $10 (Student Discount)")
        else:
            print("Ticket price: $15 (Adult)")
    else:
        print("Ticket price: $7 (Senior Discount)")
except:
    print("invalid age number, please try again.")            
"""

#revise prctice 5   #using 
user_age_str = input("Please enter your age: ")
try:
    user_age_int = int(user_age_str)
    if 0 <= user_age_int < 12:
        print("Ticket price: $5")
    elif 12 <= user_age_int <= 64:
        is_student_input = input("Are you a student? (yes/no): ")
        # 將輸入轉為小寫並去除前後空格，然後再比較
        if is_student_input.lower().strip() == "yes" or is_student_input.lower().strip() == "y":
            print("Ticket price: $10 (Student Discount)")
        else:
            print("Ticket price: $15 (Adult)")
    else:
        print("Ticket price: $7 (Senior Discount)")
except ValueError:
    print("Invalid age entered. Please enter a number.")

#practice 6

#error 1: strip(), not "stripe()"
#using "in" for if-else condition will be more easy to read

"""is_member = False
verify_user = input("are you a member? y/n")

try:
    verify_user_str = str(verify_user)
    if verify_user_str.lower().strip() == "yes" or verify_user_str.lower().stripe() == "y": #strip()
        is_member = True
        verify_member = input("please enter your member id")
        verify_member_str = str(verify_member)
        print(f"Welcome back {verify_member_str}!, valued member! You get a 10% off discount.")
    else:
        print("Welcome! Become a member today to enjoy exclusive discounts.")
except ValueError:
    print("Invalid verification entered. please try again")       
"""

#practice 6 revise

is_member = False
user_response = input("are you a member? (y/n): ")
# 使用 .strip() 移除前後可能存在的空白，並用 .lower() 轉換為小寫
# 接著使用 `in` 關鍵字來判斷輸入是否為肯定回覆，這樣寫法更簡潔且易於擴充
if user_response.strip().lower() in ["y", "yes"]:
    is_member = True  # 如果是會員，將 is_member 設為 True
    member_id = input("please enter your member id: ")
    print(f"Welcome back {member_id}!, valued member! You get a 10% off discount.")
else:
    # 如果不是會員，is_member 保持為 False
    print("Welcome! Become a member today to enjoy exclusive discounts.")

#practice 7
#logic error in shipping method
#no break

"""base_cost = input("please enter your package weight(kg):")

#base cost
try:
    base_cost_int = int(base_cost)
    if 0 < base_cost_int < 1:
        base_cost_value = 5
    elif 1 < base_cost_int < 5:
        base_cost_value = 10
    else:
        base_cost_value = 20
except ValueError:
    print("invailid weight entered, please try again") 

#destination surcharge
destination_surcharge = input("please enter the destination: (international / domestic)")
destination_surcharge_str = str(destination_surcharge)
if destination_surcharge_str.lower().strip() == ("international"):
    destination_surcharge_value = 15
else:
    destination_surcharge_value = 0


#Shipping Method 
shipping_methiod = input("please enter your shipping method: (express / standard ")
shipping_methiod_str = str(shipping_methiod)
if shipping_methiod_str.lower().strip() == ("express"):
    shipping_methiod_value = (base_cost_value + destination_surcharge_value)*2
else:
    shipping_methiod_value = 0


final_cost = base_cost_value + destination_surcharge_value + shipping_methiod_value
print(f"the final shipping cost is: ${final_cost}")


"""
         

#practice 7 revise

import sys

# --- 先獲取所有使用者輸入 ---
weight_str = input("請輸入您的包裹重量(kg): ")
destination_input = input("請輸入目的地 (international / domestic): ")
method_input = input("請輸入您的運送方式 (express / standard): ")

# --- 主要計算邏輯 ---
try:
    # 1. 類型轉換必須在 try 區塊內
    weight = float(weight_str)
    if weight <= 0:
        print("輸入的重量無效，必須是正數。請重試。")
        sys.exit() # 結束腳本

    # 2. 計算基礎費用，使用包含邊界的判斷 (<=)
    base_cost = 0
    if weight <= 1:
        base_cost = 5
    elif weight <= 5:
        base_cost = 10
    else:
        base_cost = 20

    # 3. 計算附加費 (忽略大小寫)
    surcharge = 0
    if destination_input.lower().strip() == "international":
        surcharge = 15

    # 4. 計算最終費用，並在 if/else 外部統一輸出
    subtotal = base_cost + surcharge
    final_cost = subtotal * 2 if method_input.lower().strip() == "express" else subtotal
    print(f"最終運費為: ${final_cost}")

except ValueError:
    print("輸入的重量無效，請輸入一個數字。")
    sys.exit() # 結束腳本



# practice 8

"""import sys

weight = input("please enter your weight")
height = input("please enter your height")

try:
    weight_float = float(weight)
    height_float = float(height)
    BMI = (weight_float / height_float) * height_float
    if 0 < BMI < 18.5:
        underweight = BMI
    elif 18.5 <= BMI < 25:
        normalweight =  BMI
    elif 25 <= BMI < 30:
        overweight = BMI
    else:
        obesity = BMI   
except ValueError:
    print("invalid entered, please try again")
    sys.exit()        

if underweight or normalweight:
    print(f"your bmi is {BMI}, You might want to consult a doctor or a nutritionist.")
elif obesity:
    print(f"your bmi is {BMI}, It's highly recommended to consult a doctor for a health plan")
else:
    print(f"your bmi is {BMI}, Great job, keep maintaining a healthy lifestyle!")    
    """


#practice 8 revise
import sys
weight_str = input("please enter weight(kg)")
height_str = input("please enter height(m)")

try:

    weight = float(weight_str)
    height = float(height_str)
    if weight <= 0 or height <= 0:
        print("invalid entererd, should enter positive number")
        sys.exit()
    height_meter = height / 100
    bmi = weight / (height ** 2)

    if bmi < 18:
        health_category = "under_weight"
    elif bmi < 25:
        health_category = "normal_weight"
    elif bmi < 30:
        health_category = "over_weight"
    else:
        health_category = "obesity"

    print(f"your bmi is {bmi:.2f}")
    print(f"health suggestion: {health_category}")
except ValueError:
    print("invalid entered, please check your enter is number ")
    sys.exit()


#pratice 9

"""import sys
print("---This is our menu: ---")
print("1.latte $4.0")
print("2.espresso $3.0")
print("3.cappuccino $4.5")
print("---------------------------")

latte = 4
espresso = 3
cappuccino = 4.5
latte_float = float(latte)
espresso_float = float(espresso)
cappuccino_float = float(cappuccino)

user_order = input("please enter your order: ")
if user_order == "latte" or user_order == "espresso" or user_order == "cappuccino":
    try:
        amount = input("please enter your amount: ")
        amount_int = int(amount)
        if amount_int <= 0:
            print("invalid number, please try again")
            sys.exit()
        if user_order == "latte":
            final_cost = latte_float * amount_int
            print(f"The price is ${final_cost}, thanks for your order.")
        if user_order == "espresso":
            final_cost = espresso_float * amount_int
            print(f"The price is ${final_cost}, thanks for your order.")
        if user_order == "cappuccino":
            final_cost = cappuccino_float * amount_int
            print(f"The price is ${final_cost}, thanks for your order.")
    except ValueError:
        print("invalid amount number, please try again.")
        sys.exit()
else:
    print("order not exist, please try again.")
    sys.exit()"""


# practice 9 improve
# logic correct
# improve code: to solve the repeat "if", use another varity "base_price" to solve situations in user_order 
    
#run

import sys
print("---This is our menu: ---")
print("1.latte $4.0")
print("2.espresso $3.0")
print("3.cappuccino $4.5")
print("---------------------------")

base_price = 0.0

user_order = input("please enter your order: ").lower().strip()
if user_order == "latte":
    base_price = 4.0
elif user_order == "espresso":
    base_price = 3.0
elif user_order == "cappuccino":
    base_price = 4.5

if base_price > 0:
    try:
        amount = input("please enter your amount: ")
        amount_int = int(amount)
        if amount_int <= 0:
            print("invalid number, please try again")
            sys.exit()
        else:    
            final_cost = base_price * amount_int
            print(f"The price is ${final_cost}")
    except ValueError:
        print("invalid amount number, please try again.")
        sys.exit()
else:
    print("order not exist, please try again.")
    sys.exit()




#practice 11 for-in loop

students = ["Aaron", "Betty", "Chris", "David", "Eva"]
print("--- 開始點名 ---")

for students_name in students:
    print(f"hi, {students_name}!")
print("---點名結束---")


#practice 12

scores = [85, 55, 92, 78, 60, 49, 99, 71]
passing_score = 60

import sys
print("---start to check the score---")

for student_score in scores:
    if student_score > passing_score:
        print(f"hi user, your score is {student_score}, you have pass the test.")
    else:
        print(f"hi user, your score is {student_score}, you do not pass the test")

print("---score checking process done")

#practice 13 

scores = [85, 55, 92, 78, 60, 49, 99, 71]
passing_score = 60
passing_students_count = 0
print("--- start checking scores ---")
for score in scores:
    if score >= passing_score:
        pass_student_amount = passing_students_count + 1
        print(f"hi user, your score is {score}, you have pass the test")

print(f"total pass amount is {pass_student_amount}")
print("--- checking complete ---")

#practice 13

scores = [85, 55, 92, 78, 60, 49, 99, 71]
total_score = 0
print("--- starting counting total score ---")
for score in scores:
    total_score += score

student_number = len(scores)
average_score = total_score / student_number

print(f"total score: {total_score}")
print(f"average score is: {average_score:.2f}")
print("--- counting ended ---")

#practice 14

"""scores = [85, 55, 92, 78, 60, 49, 99, 71]

if scores:
    max_value = scores[0]

print("--- 開始尋找最高分 ---")
for score in scores:
    if score > max_value:
        max_value = score
print(f"maximum value is {max_value}")        
"""
#practice 14 improve

if scores:
    max_value = scores[0]

print("--- 開始尋找最高分 ---")
for score in scores[1:]:   #slicing, start the calculation from the second number
    if score > max_value:
        max_value = score
    print(f"maximum value is {max_value}")
else:
    print("the score list is empty")   



#practice 15 combination
"""scores = [85, 55, 92, 78, 60, 49, 99, 71, 100, 23]
print("--- score report ---")

#total student amount
total_amount = len(scores)
print(f"total student amount is {total_amount}")

#total_score
total_score = 0
if scores:
    for score in scores:
        total_score += score
    print(f"total score: {total_score}")
else:
    print("list does not exist")

#avg score
total_amount = len(scores)
total_score = 0
if scores:
    for score in scores:
        total_score += score
    avg_score = total_score / total_amount    
    print(f"average score: {avg_score}")
else:
    print("list does not exist")

#find the minimum & maximum score

max_score = scores[0]
min_score = scores[0]
if scores:    #scores, not score, to check the list exist or not
    for score in scores[1:]:
        if score > max_score:
            max_score = score
    print(f"the highest score is {max_score}")

    for score in scores[1:]:
        if score < min_score:
            min_score = score
    print(f"the lowest score is {min_score}")
else:
    print("the list does not exit")

#total amount of students pass score

pass_test_count = 0
pass_score = 60
pass_score_int = int(pass_score)
if scores:
    for score in scores:
        if score >= 60:
            pass_test_count += 1
    print(f"{pass_test_count} students pass the test")
else:
    print("the list does not exit")

#pass rating
#pass amount / total amount of student

pass_rate = pass_test_count / total_amount
percentage = pass_rate * 100
print(f"pass rate is {percentage:.2f}%")


#user funtion

print("--- adding new score funtion ---")
import sys
user_add_score = input("adding new score? y/n")

if user_add_score.lower().strip() in ["y" or "yes"]:
    add_score = input("please enter score(0 <= score <= 100): ")
    try:
        add_score_int = int(add_score)
        if 0 <= add_score_int <= 100:
            scores.append(add_score_int)
            
        else:
            print("invalid entered, please try again.")
            sys.exit()
    except ValueError:
        print("please enter a number, try again later")
        sys.exit()

        """

#practice 15 improve
scores = [85, 55, 92, 78, 60, 49, 99, 71, 100, 23]
if not scores:
    print("list is empty, cannot output score report")
else:
    total_score = 0
    pass_test_count = 0
    max_score = scores[0]
    min_score = scores[0]

    for score in scores:
        total_score += score
        if score >= 60:
            pass_test_count += 1
        if score > max_score:
            max_score = score
        if score < min_score:
            min_score = score
#report
total_amount = len(scores)
avg_score = total_score / total_amount
pass_rate = pass_test_count / total_amount
percentage_pass_rate = pass_rate * 100
print(f"total student amount: {total_amount}")
print(f"total score: {total_score}")
print(f"average score: {avg_score}")
print(f"highest score: {max_score}")
print(f"lowest score: {min_score}")
print(f"{pass_test_count} students pass the score")
print(f"past rate: {percentage_pass_rate:.2f}%")


#user add new score
user_add_score = input("adding new score in list? y/n")

if user_add_score.strip().lower() in ["y", "yes"]:
    add_score = input("please enter new score (0-100)")
    try:
        add_score_int = int(add_score) 
        if 0 <= add_score_int <= 100:
            scores.append(add_score_int)
            print(f"score has been added in list")
            print(f"updated list: {scores}")
        else:
            print("please enter a valid number")
    except ValueError:
        print("invalid entered, please try again")

print("--- function complete ---")


#practice 16

"""names = ["蘋果", "香蕉", "櫻桃", "橘子"]
prices = [5, 3, 10, 4]
quantities = [20, 40, 4, 35]

total_value = 0
highest_price_item = None
low_stock_items = []
highest_price = prices[0]
highest_price_item = names[0]

for i in range(len(names)):
    item_value = prices[i] * quantities[i]
    total_value += item_value
    if prices[i] > highest_price:
        highest_price = prices[i]
        names[i] == prices[i]
    if quantities[i] < 10:
        names[i] == quantities[i]
        low_stock_items.append(names[i])


print(f"total items value: {total_value}")
print(f"highest price item: {names[i]}")
print(f"low stock item: {low_stock_items}")
"""



#practice 16 revise

names = ["蘋果", "香蕉", "櫻桃", "橘子"]
prices = [5, 3, 10, 4]
quantities = [20, 40, 4, 35]

total_value = 0
highest_price_item = None
low_stock_items = []
highest_price = prices[0]
highest_price_item = names[0]

for i in range(len(names)):
    item_value = prices[i] * quantities[i]
    total_value += item_value
    if prices[i] > highest_price:
        highest_price = prices[i]
        highest_price_item = names[i]
    if quantities[i] < 10:
        low_stock_items.append(names[i])

print(f"total items value: {total_value}")
print(f"highest price item: {highest_price_item}")
print(f"low stock item: {low_stock_items}")


#practice 16 adding search fuction
"""
import sys
names = ["蘋果", "香蕉", "櫻桃", "橘子"]
prices = [5, 3, 10, 4]
quantities = [20, 40, 4, 35]
search_results = []
user_search_max = 0
user_search_min = 0

try:
    user_enter_min = input("please enter the item minimum price for search ($min ~ $max)")
    user_enter_max = input("please enter the item maximum price for search ($min ~ $max)")
    user_enter_min_int = int(user_enter_min)
    user_enter_max_int = int(user_enter_max)

    if user_enter_min_int > user_enter_max_int:
        print("invalid value, please try again.")
        sys.exit()
    for i in prices:
        if user_enter_min_int < i < user_enter_max_int:
            names[i] = prices[i]
            search_results.append(names[i])
        else:
            print("there is no item in your request")
except ValueError:
    print("please enter a valid number")

if search_results:
    print(f"item: {names[i]}, price: {prices[i]}")
else:
    print("item not exist, please try again")    
"""     

#practice 16 adding search fuction revise

#practice 16 adding search fuction
import sys
names = ["蘋果", "香蕉", "櫻桃", "橘子"]
prices = [5, 3, 10, 4]
quantities = [20, 40, 4, 35]
search_results = []
user_search_max = 0
user_search_min = 0

try:
    user_enter_min = input("please enter the item minimum price for search ($min ~ $max)")
    user_enter_max = input("please enter the item maximum price for search ($min ~ $max)")
    user_enter_min_int = int(user_enter_min)
    user_enter_max_int = int(user_enter_max)

    if user_enter_min_int > user_enter_max_int:
        print("invalid value, please try again.")
        sys.exit()
    for i in range(len(prices)):
        if user_enter_min_int <= prices[i] <= user_enter_max_int:
            search_results.append((names[i], prices[i], quantities[i]))
        else:
            print("there is no item in your request")
except ValueError:
    print("please enter a valid number")

if search_results:
    for name, price, quantity in search_results:
        print(f"item: {name}, price: {price}, quantity: {quantity}")
else:
    print("item not exist, please try again")    