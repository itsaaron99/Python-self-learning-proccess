# ------chapter 4: data structures--------

# --- Practice 5: Working with Nested Dictionaries ---

# In this exercise, we'll work with a list of students. Each student is a
# dictionary, and their 'grades' are stored in another nested dictionary.

def calculate_student_gpa(student):
    """Calculates the Grade Point Average (GPA) for a single student."""
    grades = student['grades']
    if not grades:
        return 0
    scores = grades.values()
    return sum(scores) / len(scores)
        

def find_top_student(student_list):
    """Finds the student with the highest GPA in a list of students."""
    top_student_name = None
    highest_gpa = -1 
    for student in student_list:
        current_gpa = calculate_student_gpa(student)
        if current_gpa > highest_gpa:
            highest_gpa = current_gpa
            top_student_name = student['name']
    return top_student_name
# --- Test your functions ---

students = [
    {
        'name': 'Alice',
        'grades': {'math': 90, 'science': 88, 'history': 92} 
    },
    {
        'name': 'Bob',
        'grades': {'math': 78, 'science': 82, 'history': 80} 
    },
    {
        'name': 'Charlie',
        'grades': {} 
    },
    {
        'name': 'Diana',
        'grades': {'math': 95, 'science': 98, 'history': 99} 
    }
]

top_student = find_top_student(students)
print(f"--- Top Student Report ---")
print(f"The student with the highest GPA is: {top_student}") # Expected: Diana


# --- Practice 6: File I/O - Making Data Persistent ---

import json # Import the json module to work with JSON files.

def save_list_to_file(todo_list, filename):
    """Saves the to-do list to a file using JSON."""
    # 'w' stands for 'write' mode. It will create the file if it doesn't exist,
    # or overwrite it if it does.
    # 'with open' ensures the file is automatically closed.
    with open(filename, 'w') as f:
        # json.dump takes the Python object (todo_list) and writes it
        # into the file object (f) in JSON format.
        json.dump(todo_list, f, indent=4)

def load_list_from_file(filename):
    """Loads the to-do list from a file. Returns an empty list if the file doesn't exist."""
    # We use a try-except block to handle the first run when the file is not yet created.
    try:
        # 'r' stands for 'read' mode.
        with open(filename, 'r') as f:
            # json.load reads from the file object (f) and converts
            # the JSON text back into a Python object (a list in this case).
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, this block runs instead of crashing.
        # We return an empty list to start fresh.
        return []

def main_persistent_todo_app():
    """A to-do app that saves and loads its data."""
    FILE_NAME = "my_todo_list.json" # Define the filename as a constant.

    # At the start, load the list from the file.
    todo_items = load_list_from_file(FILE_NAME)

    print("\n--- Persistent To-Do List Application ---")

    while True:
        # We can reuse the functions from the previous chapter's exercise.
        # For simplicity, we'll just put the logic here.
        print("\nMenu: 1: Add, 2: View, q: Save & Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("What to add? ")
            todo_items.append(item)
            print(f"Added: {item}")
        elif choice == '2':
            print("\n--- Your List ---")
            for i, item in enumerate(todo_items, 1):
                print(f"{i}. {item}")
        elif choice == 'q':
            # Before quitting, save the current list to the file.
            save_list_to_file(todo_items, FILE_NAME)
            print("List saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# --- Run the application ---
# The file I/O practice is paused for now.
# main_persistent_todo_app()


def group_sales_by_date(sales_list):
    """Groups a list of sales records by date."""
    group_result = {}
    for sale in sales_list:
        date = sale['date']
        # setdefault 會回傳該 date 對應的字典。如果 date 是新的，它會先建立一個空字典。
        date_summary = group_result.setdefault(date, {'total_sale': 0, 'product_sold': []})
        date_summary['total_sale'] += sale['amount']
        date_summary['product_sold'].append(sale['product'])
    return group_result
# --- Test your function ---
sales_data = [
    {'date': '2023-10-01', 'product': 'Laptop', 'amount': 1200},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 25},
    {'date': '2023-10-02', 'product': 'Laptop', 'amount': 1250},
    {'date': '2023-10-02', 'product': 'Keyboard', 'amount': 75},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 30},
]

grouped_report = group_sales_by_date(sales_data)
print("\n--- Sales Report Grouped by Date ---")
# We use pprint (pretty-print) to make the nested dictionary output easier to read.
import pprint
pprint.pprint(grouped_report)
# Expected output (order of products in list might vary):
# {'2023-10-01': {'products_sold': ['Laptop', 'Mouse', 'Mouse'], 'total_sales': 1255},
#  '2023-10-02': {'products_sold': ['Laptop', 'Keyboard'], 'total_sales': 1325}}


# --- Practice 8: Data Transformation - Flattening Data ---

# This is the reverse of grouping. We take a structured dictionary and
# flatten it into a single list, often adding information along the way.

import pprint

def flatten_employee_data(grouped_employees):
    """
    Takes a dictionary of employees grouped by department and returns a single
    list of all employees, with their department added to their record.
    """
    flat_list = []
    for department_name, employee_list in grouped_employees.items():
        for emp in employee_list:
            new_employee_list = emp.copy()
            new_employee_list['department'] = department_name
            flat_list.append(new_employee_list)
    return flat_list

# --- Test your function ---
employees_by_department = {
    'Sales': [
        {'name': 'Alice', 'employee_id': 'S001'},
        {'name': 'Bob', 'employee_id': 'S002'}
    ],
    'Engineering': [
        {'name': 'Charlie', 'employee_id': 'E001'},
        {'name': 'Diana', 'employee_id': 'E002'}
    ]
}

flat_employee_list = flatten_employee_data(employees_by_department)
print("\n--- Flattened Employee List ---")
pprint.pprint(flat_employee_list)


# --- Practice 9: Data Transformation - inverted_index ---

import pprint

def create_inverted_index(documents):
    """Creates an inverted index from a list of documents."""
    inverted_index = {}
    for index, doc in enumerate(documents):
        # Using set to handle multiple occurrences of the same word in one document
        unique_words = set(doc.lower().split())
        for word in unique_words:
            inverted_index.setdefault(word, []).append(index)
    return inverted_index            


documents = [
    "the quick brown fox jumps over the lazy dog",
    "the dog is lazy",
    "the fox is quick"
]

inverted_index_result = create_inverted_index(documents)
pprint.pprint(inverted_index_result)



# --- Practice 10: Merging and Summarizing Data ---

# This is a very common real-world task: combining data from multiple sources
# based on a shared key and creating a summary.

import pprint

def create_product_summary(sales, products):
    """
    Merges product information with sales data to create a summary report.
    """
    sales_summary = {}
    
    # Step 1: Summarize sales data by product_id
    for sale in sales:
        product_id = sale['product_id']
        summary = sales_summary.setdefault(product_id, {'total_quantity': 0, 'transaction_count': 0})
        summary['total_quantity'] += sale['quantity_sold']
        summary['transaction_count'] += 1

    # Step 2: Build the final report using the product list as the base
    summary_report =[]
    for product in products:
        product_id = product.get('product_id')
        default_sales_data = {'total_quantity': 0, 'transaction_count': 0}
        # FIX: Use the current product's ID (product_id) to get sales data, not a lingering variable from a previous loop.
        product_sales_data = sales_summary.get(product_id, default_sales_data)
        
        current_summary = {
            'product_id': product_id,
            'name': product.get('name'),
            'total_quantity_sold': product_sales_data['total_quantity'],
            'number_of_transactions': product_sales_data['transaction_count']
        }
        summary_report.append(current_summary)
    return summary_report  




# --- Test your function ---
product_list = [
    {'product_id': 'p001', 'name': 'Laptop'},
    {'product_id': 'p002', 'name': 'Mouse'},
    {'product_id': 'p003', 'name': 'Keyboard'},
    {'product_id': 'p004', 'name': 'Monitor'}
]

sales_list = [
    {'product_id': 'p001', 'quantity_sold': 2},
    {'product_id': 'p002', 'quantity_sold': 5},
    {'product_id': 'p001', 'quantity_sold': 3},
    {'product_id': 'p003', 'quantity_sold': 1},
    {'product_id': 'p002', 'quantity_sold': 10}
]


result = create_product_summary(sales_list, product_list)
pprint.pprint(result)
              


import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

def generate_student_report_cards(roster, scores):
    """
    Merges student roster information with assignment scores to create
    a list of comprehensive report cards.
    """
    # --- Step 1: Group all scores by student ID ---
    # TODO: Create an empty dictionary `scores_by_student`.
    # TODO: Loop through each `record` in the `scores` list.
        # TODO: Get the student_id and score.
        # TODO: If the student_id is new, initialize its value in `scores_by_student` as an empty list [].
        # TODO: Append the current score to the list for that student_id.
    scores_by_student = {}
    for record in scores:
        # Using setdefault makes this step more concise.
        scores_by_student.setdefault(record['student_id'], []).append(record['score'])


    # --- Step 2: Create report cards by merging with the roster ---
    # TODO: Create an empty list `report_cards`.
    # TODO: Loop through each `student` in the `roster` list.
        # TODO: Get the student's id and name.
        # TODO: Use .get(student_id, []) to get the list of scores.
        # TODO: Calculate the average score. (Handle the case of an empty list!)
        # TODO: Determine the 'status' ('Pass' or 'Fail').
        # TODO: Create a new dictionary for the report card.
        # TODO: Append the new report card to the `report_cards` list.
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

student_reports = generate_student_report_cards(student_roster, assignment_scores)
print("\n--- Student Report Cards ---")
pprint.pprint(student_reports)


# ------chapter 4: data structures--------

# --- Practice 5: Working with Nested Dictionaries ---

# In this exercise, we'll work with a list of students. Each student is a
# dictionary, and their 'grades' are stored in another nested dictionary.

def calculate_student_gpa(student):
    """Calculates the Grade Point Average (GPA) for a single student."""
    grades = student['grades']
    if not grades:
        return 0
    scores = grades.values()
    return sum(scores) / len(scores)
        

def find_top_student(student_list):
    """Finds the student with the highest GPA in a list of students."""
    top_student_name = None
    highest_gpa = -1 
    for student in student_list:
        current_gpa = calculate_student_gpa(student)
        if current_gpa > highest_gpa:
            highest_gpa = current_gpa
            top_student_name = student['name']
    return top_student_name
# --- Test your functions ---

students = [
    {
        'name': 'Alice',
        'grades': {'math': 90, 'science': 88, 'history': 92} 
    },
    {
        'name': 'Bob',
        'grades': {'math': 78, 'science': 82, 'history': 80} 
    },
    {
        'name': 'Charlie',
        'grades': {} 
    },
    {
        'name': 'Diana',
        'grades': {'math': 95, 'science': 98, 'history': 99} 
    }
]

top_student = find_top_student(students)
print(f"--- Top Student Report ---")
print(f"The student with the highest GPA is: {top_student}") # Expected: Diana


# --- Practice 6: File I/O - Making Data Persistent ---

import json # Import the json module to work with JSON files.

def save_list_to_file(todo_list, filename):
    """Saves the to-do list to a file using JSON."""
    # 'w' stands for 'write' mode. It will create the file if it doesn't exist,
    # or overwrite it if it does.
    # 'with open' ensures the file is automatically closed.
    with open(filename, 'w') as f:
        # json.dump takes the Python object (todo_list) and writes it
        # into the file object (f) in JSON format.
        json.dump(todo_list, f, indent=4)

def load_list_from_file(filename):
    """Loads the to-do list from a file. Returns an empty list if the file doesn't exist."""
    # We use a try-except block to handle the first run when the file is not yet created.
    try:
        # 'r' stands for 'read' mode.
        with open(filename, 'r') as f:
            # json.load reads from the file object (f) and converts
            # the JSON text back into a Python object (a list in this case).
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, this block runs instead of crashing.
        # We return an empty list to start fresh.
        return []

def main_persistent_todo_app():
    """A to-do app that saves and loads its data."""
    FILE_NAME = "my_todo_list.json" # Define the filename as a constant.

    # At the start, load the list from the file.
    todo_items = load_list_from_file(FILE_NAME)

    print("\n--- Persistent To-Do List Application ---")

    while True:
        # We can reuse the functions from the previous chapter's exercise.
        # For simplicity, we'll just put the logic here.
        print("\nMenu: 1: Add, 2: View, q: Save & Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("What to add? ")
            todo_items.append(item)
            print(f"Added: {item}")
        elif choice == '2':
            print("\n--- Your List ---")
            for i, item in enumerate(todo_items, 1):
                print(f"{i}. {item}")
        elif choice == 'q':
            # Before quitting, save the current list to the file.
            save_list_to_file(todo_items, FILE_NAME)
            print("List saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# --- Run the application ---
# The file I/O practice is paused for now.
# main_persistent_todo_app()


def group_sales_by_date(sales_list):
    """Groups a list of sales records by date."""
    group_result = {}
    for sale in sales_list:
        date = sale['date']
        product_sold = sale['product']
        total_sale = sale['amount']
        if date not in group_result:
            group_result[date] = {'total_sale': 0, 'product_sold': []}
        else:
            group_result[date]['total_sale'] += total_sale
            group_result[date]['product_sold'].append(product_sold)

    return group_result
# --- Test your function ---
sales_data = [
    {'date': '2023-10-01', 'product': 'Laptop', 'amount': 1200},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 25},
    {'date': '2023-10-02', 'product': 'Laptop', 'amount': 1250},
    {'date': '2023-10-02', 'product': 'Keyboard', 'amount': 75},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 30},
]

grouped_report = group_sales_by_date(sales_data)
print("\n--- Sales Report Grouped by Date ---")
# We use pprint (pretty-print) to make the nested dictionary output easier to read.
import pprint
pprint.pprint(grouped_report)
# Expected output (order of products in list might vary):
# {'2023-10-01': {'products_sold': ['Laptop', 'Mouse', 'Mouse'], 'total_sales': 1255},
#  '2023-10-02': {'products_sold': ['Laptop', 'Keyboard'], 'total_sales': 1325}}


# --- Practice 8: Data Transformation - Flattening Data ---

# This is the reverse of grouping. We take a structured dictionary and
# flatten it into a single list, often adding information along the way.

import pprint

def flatten_employee_data(grouped_employees):
    """
    Takes a dictionary of employees grouped by department and returns a single
    list of all employees, with their department added to their record.
    """
    flat_list = []
    for department_name, employee_list in grouped_employees.items():
        for emp in employee_list:
            new_employee_list = emp.copy()
            new_employee_list['department'] = department_name
            flat_list.append(new_employee_list)
    return flat_list

# --- Test your function ---
employees_by_department = {
    'Sales': [
        {'name': 'Alice', 'employee_id': 'S001'},
        {'name': 'Bob', 'employee_id': 'S002'}
    ],
    'Engineering': [
        {'name': 'Charlie', 'employee_id': 'E001'},
        {'name': 'Diana', 'employee_id': 'E002'}
    ]
}

flat_employee_list = flatten_employee_data(employees_by_department)
print("\n--- Flattened Employee List ---")
pprint.pprint(flat_employee_list)


# --- Practice 9: Data Transformation - inverted_index ---

import pprint

def create_inverted_index(document):
    inverted_index = {}
    for index, doc in enumerate(document):
        new_doc = doc.lower().split(" ")
        for word in new_doc:
            if word not in inverted_index:
                inverted_index[word] = [index]
            else:
                inverted_index[word].append(index)
    return inverted_index            


documents = [
    "the quick brown fox jumps over the lazy dog",
    "the dog is lazy",
    "the fox is quick"
]

inverted_index_result = create_inverted_index(documents)
pprint.pprint(inverted_index_result)



# --- Practice 10: Merging and Summarizing Data ---

# This is a very common real-world task: combining data from multiple sources
# based on a shared key and creating a summary.

import pprint

def create_product_summary(sales, products):
    """
    Merges product information with sales data to create a summary report.
    """
    sales_summary = {}
    
    for sale in sales:
        total_quantity = sale['quantity_sold']
        product_id = sale['product_id']
        #if not yet exist in sales_summary
        if product_id not in sales_summary:
            sales_summary[product_id] = {
                'total_quantity': total_quantity,
                'transaction_count': 1
            }
        else:
            sales_summary[product_id]['total_quantity'] += total_quantity
            sales_summary[product_id]['transaction_count'] += 1
    

    summary_report =[]
    for product in products:
        id_ = product.get('product_id')
        product_name = product.get('name')
        default_sales_data = {'total_quantity': 0, 'transaction_count': 0}
        product_sales_data = sales_summary.get(product_id, default_sales_data)
        current_summary = {
            'product_id': id_,
            'name': product_name,
            'total_quantity_sold': product_sales_data['total_quantity'],
            'number_of_transactions': product_sales_data['transaction_count']
        }
        summary_report.append(current_summary)
    return summary_report  




# --- Test your function ---
product_list = [
    {'product_id': 'p001', 'name': 'Laptop'},
    {'product_id': 'p002', 'name': 'Mouse'},
    {'product_id': 'p003', 'name': 'Keyboard'},
    {'product_id': 'p004', 'name': 'Monitor'}
]

sales_list = [
    {'product_id': 'p001', 'quantity_sold': 2},
    {'product_id': 'p002', 'quantity_sold': 5},
    {'product_id': 'p001', 'quantity_sold': 3},
    {'product_id': 'p003', 'quantity_sold': 1},
    {'product_id': 'p002', 'quantity_sold': 10}
]


result = create_product_summary(sales_list, product_list)
pprint.pprint(result)
              


import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

def generate_student_report_cards(roster, scores):
    """
    Merges student roster information with assignment scores to create
    a list of comprehensive report cards.
    """
    # --- Step 1: Group all scores by student ID ---
    # TODO: Create an empty dictionary `scores_by_student`.
    # TODO: Loop through each `record` in the `scores` list.
        # TODO: Get the student_id and score.
        # TODO: If the student_id is new, initialize its value in `scores_by_student` as an empty list [].
        # TODO: Append the current score to the list for that student_id.
    scores_by_student = {}
    for record in scores:
        student_id = record['student_id']
        student_score = record['score']
        if student_id not in scores_by_student:
            scores_by_student[student_id] = []
        scores_by_student[student_id].append(student_score)    


    # --- Step 2: Create report cards by merging with the roster ---
    # TODO: Create an empty list `report_cards`.
    # TODO: Loop through each `student` in the `roster` list.
        # TODO: Get the student's id and name.
        # TODO: Use .get(student_id, []) to get the list of scores.
        # TODO: Calculate the average score. (Handle the case of an empty list!)
        # TODO: Determine the 'status' ('Pass' or 'Fail').
        # TODO: Create a new dictionary for the report card.
        # TODO: Append the new report card to the `report_cards` list.
    report_cards = []
    for student in roster:
        id_ = student['student_id']
        name = student['name']
        student_scores = scores_by_student.get(id_, [])
        if not student_scores:
            avg_score = 0
        else:
            avg_score = sum(student_scores) / len(student_scores)
        status = 'Pass' if avg_score >= 60 else 'Fail'

        report_card = {
            'student_id': id_,
            'name': name,
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

student_reports = generate_student_report_cards(student_roster, assignment_scores)
print("\n--- Student Report Cards ---")
pprint.pprint(student_reports)


# --- Learning Topic 1: In-depth Lists/Dictionaries ---
# --- Sub-topic 1.1: List Comprehensions ---

# Practice 12: Filtering and Transforming Data with List Comprehensions

def process_sensor_data(readings):
    """
    Processes a list of sensor readings.
    It should:
    1. Filter out any readings that are None (invalid data).
    2. Convert valid readings from Celsius to Fahrenheit (F = C * 9/5 + 32).
    3. Return a new list of Fahrenheit temperatures, rounded to 2 decimal places.
    """
    # TODO: Use a list comprehension to achieve the above.
    # Hint: The comprehension should have both a transformation (expression)
    # and a filtering condition (if).
    return [
        round(read * 9/5 + 32, 2) for read in readings if read is not None
        ]

# Test cases
sensor_readings_1 = [20.5, 22.0, None, 18.3, 25.1]
expected_output_1 = [68.9, 71.6, 64.94, 77.18]
# ------chapter 4: data structures--------

# --- Practice 5: Working with Nested Dictionaries ---

# In this exercise, we'll work with a list of students. Each student is a
# dictionary, and their 'grades' are stored in another nested dictionary.

def calculate_student_gpa(student):
    """Calculates the Grade Point Average (GPA) for a single student."""
    grades = student['grades']
    if not grades:
        return 0
    scores = grades.values()
    return sum(scores) / len(scores)
        

def find_top_student(student_list):
    """Finds the student with the highest GPA in a list of students."""
    top_student_name = None
    highest_gpa = -1 
    for student in student_list:
        current_gpa = calculate_student_gpa(student)
        if current_gpa > highest_gpa:
            highest_gpa = current_gpa
            top_student_name = student['name']
    return top_student_name
# --- Test your functions ---

students = [
    {
        'name': 'Alice',
        'grades': {'math': 90, 'science': 88, 'history': 92} 
    },
    {
        'name': 'Bob',
        'grades': {'math': 78, 'science': 82, 'history': 80} 
    },
    {
        'name': 'Charlie',
        'grades': {} 
    },
    {
        'name': 'Diana',
        'grades': {'math': 95, 'science': 98, 'history': 99} 
    }
]

top_student = find_top_student(students)
print(f"--- Top Student Report ---")
print(f"The student with the highest GPA is: {top_student}") # Expected: Diana


# --- Practice 6: File I/O - Making Data Persistent ---

import json # Import the json module to work with JSON files.

def save_list_to_file(todo_list, filename):
    """Saves the to-do list to a file using JSON."""
    # 'w' stands for 'write' mode. It will create the file if it doesn't exist,
    # or overwrite it if it does.
    # 'with open' ensures the file is automatically closed.
    with open(filename, 'w') as f:
        # json.dump takes the Python object (todo_list) and writes it
        # into the file object (f) in JSON format.
        json.dump(todo_list, f, indent=4)

def load_list_from_file(filename):
    """Loads the to-do list from a file. Returns an empty list if the file doesn't exist."""
    # We use a try-except block to handle the first run when the file is not yet created.
    try:
        # 'r' stands for 'read' mode.
        with open(filename, 'r') as f:
            # json.load reads from the file object (f) and converts
            # the JSON text back into a Python object (a list in this case).
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, this block runs instead of crashing.
        # We return an empty list to start fresh.
        return []

def main_persistent_todo_app():
    """A to-do app that saves and loads its data."""
    FILE_NAME = "my_todo_list.json" # Define the filename as a constant.

    # At the start, load the list from the file.
    todo_items = load_list_from_file(FILE_NAME)

    print("\n--- Persistent To-Do List Application ---")

    while True:
        # We can reuse the functions from the previous chapter's exercise.
        # For simplicity, we'll just put the logic here.
        print("\nMenu: 1: Add, 2: View, q: Save & Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("What to add? ")
            todo_items.append(item)
            print(f"Added: {item}")
        elif choice == '2':
            print("\n--- Your List ---")
            for i, item in enumerate(todo_items, 1):
                print(f"{i}. {item}")
        elif choice == 'q':
            # Before quitting, save the current list to the file.
            save_list_to_file(todo_items, FILE_NAME)
            print("List saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# --- Run the application ---
# The file I/O practice is paused for now.
# main_persistent_todo_app()


def group_sales_by_date(sales_list):
    """Groups a list of sales records by date."""
    group_result = {}
    for sale in sales_list:
        date = sale['date']
        # setdefault 會回傳該 date 對應的字典。如果 date 是新的，它會先建立一個空字典。
        date_summary = group_result.setdefault(date, {'total_sale': 0, 'product_sold': []})
        date_summary['total_sale'] += sale['amount']
        date_summary['product_sold'].append(sale['product'])
    return group_result
# --- Test your function ---
sales_data = [
    {'date': '2023-10-01', 'product': 'Laptop', 'amount': 1200},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 25},
    {'date': '2023-10-02', 'product': 'Laptop', 'amount': 1250},
    {'date': '2023-10-02', 'product': 'Keyboard', 'amount': 75},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 30},
]

grouped_report = group_sales_by_date(sales_data)
print("\n--- Sales Report Grouped by Date ---")
# We use pprint (pretty-print) to make the nested dictionary output easier to read.
import pprint
pprint.pprint(grouped_report)
# Expected output (order of products in list might vary):
# {'2023-10-01': {'products_sold': ['Laptop', 'Mouse', 'Mouse'], 'total_sales': 1255},
#  '2023-10-02': {'products_sold': ['Laptop', 'Keyboard'], 'total_sales': 1325}}


# --- Practice 8: Data Transformation - Flattening Data ---

# This is the reverse of grouping. We take a structured dictionary and
# flatten it into a single list, often adding information along the way.

import pprint

def flatten_employee_data(grouped_employees):
    """
    Takes a dictionary of employees grouped by department and returns a single
    list of all employees, with their department added to their record.
    """
    flat_list = []
    for department_name, employee_list in grouped_employees.items():
        for emp in employee_list:
            new_employee_list = emp.copy()
            new_employee_list['department'] = department_name
            flat_list.append(new_employee_list)
    return flat_list

# --- Test your function ---
employees_by_department = {
    'Sales': [
        {'name': 'Alice', 'employee_id': 'S001'},
        {'name': 'Bob', 'employee_id': 'S002'}
    ],
    'Engineering': [
        {'name': 'Charlie', 'employee_id': 'E001'},
        {'name': 'Diana', 'employee_id': 'E002'}
    ]
}

flat_employee_list = flatten_employee_data(employees_by_department)
print("\n--- Flattened Employee List ---")
pprint.pprint(flat_employee_list)


# --- Practice 9: Data Transformation - inverted_index ---

import pprint

def create_inverted_index(document):
    inverted_index = {}
    for index, doc in enumerate(document):
        new_doc = doc.lower().split(" ")
        for word in new_doc:
            if word not in inverted_index:
                inverted_index[word] = [index]
            else:
                inverted_index[word].append(index)
    return inverted_index            


documents = [
    "the quick brown fox jumps over the lazy dog",
    "the dog is lazy",
    "the fox is quick"
]

inverted_index_result = create_inverted_index(documents)
pprint.pprint(inverted_index_result)



# --- Practice 10: Merging and Summarizing Data ---

# This is a very common real-world task: combining data from multiple sources
# based on a shared key and creating a summary.

import pprint

def create_product_summary(sales, products):
    """
    Merges product information with sales data to create a summary report.
    """
    sales_summary = {}
    
    for sale in sales:
        total_quantity = sale['quantity_sold']
        product_id = sale['product_id']
        #if not yet exist in sales_summary
        if product_id not in sales_summary:
            sales_summary[product_id] = {
                'total_quantity': total_quantity,
                'transaction_count': 1
            }
        else:
            sales_summary[product_id]['total_quantity'] += total_quantity
            sales_summary[product_id]['transaction_count'] += 1
    

    summary_report =[]
    for product in products:
        id_ = product.get('product_id')
        product_name = product.get('name')
        default_sales_data = {'total_quantity': 0, 'transaction_count': 0}
        product_sales_data = sales_summary.get(product_id, default_sales_data)
        current_summary = {
            'product_id': id_,
            'name': product_name,
            'total_quantity_sold': product_sales_data['total_quantity'],
            'number_of_transactions': product_sales_data['transaction_count']
        }
        summary_report.append(current_summary)
    return summary_report  




# --- Test your function ---
product_list = [
    {'product_id': 'p001', 'name': 'Laptop'},
    {'product_id': 'p002', 'name': 'Mouse'},
    {'product_id': 'p003', 'name': 'Keyboard'},
    {'product_id': 'p004', 'name': 'Monitor'}
]

sales_list = [
    {'product_id': 'p001', 'quantity_sold': 2},
    {'product_id': 'p002', 'quantity_sold': 5},
    {'product_id': 'p001', 'quantity_sold': 3},
    {'product_id': 'p003', 'quantity_sold': 1},
    {'product_id': 'p002', 'quantity_sold': 10}
]


result = create_product_summary(sales_list, product_list)
pprint.pprint(result)
              


import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

def generate_student_report_cards(roster, scores):
    """
    Merges student roster information with assignment scores to create
    a list of comprehensive report cards.
    """
    # --- Step 1: Group all scores by student ID ---
    # TODO: Create an empty dictionary `scores_by_student`.
    # TODO: Loop through each `record` in the `scores` list.
        # TODO: Get the student_id and score.
        # TODO: If the student_id is new, initialize its value in `scores_by_student` as an empty list [].
        # TODO: Append the current score to the list for that student_id.
    scores_by_student = {}
    for record in scores:
        student_id = record['student_id']
        student_score = record['score']
        if student_id not in scores_by_student:
            scores_by_student[student_id] = []
        scores_by_student[student_id].append(student_score)    


    # --- Step 2: Create report cards by merging with the roster ---
    # TODO: Create an empty list `report_cards`.
    # TODO: Loop through each `student` in the `roster` list.
        # TODO: Get the student's id and name.
        # TODO: Use .get(student_id, []) to get the list of scores.
        # TODO: Calculate the average score. (Handle the case of an empty list!)
        # TODO: Determine the 'status' ('Pass' or 'Fail').
        # TODO: Create a new dictionary for the report card.
        # TODO: Append the new report card to the `report_cards` list.
    report_cards = []
    for student in roster:
        id_ = student['student_id']
        name = student['name']
        student_scores = scores_by_student.get(id_, [])
        if not student_scores:
            avg_score = 0
        else:
            avg_score = sum(student_scores) / len(student_scores)
        status = 'Pass' if avg_score >= 60 else 'Fail'

        report_card = {
            'student_id': id_,
            'name': name,
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

student_reports = generate_student_report_cards(student_roster, assignment_scores)
print("\n--- Student Report Cards ---")
pprint.pprint(student_reports)


# ------chapter 4: data structures--------

# --- Practice 5: Working with Nested Dictionaries ---

# In this exercise, we'll work with a list of students. Each student is a
# dictionary, and their 'grades' are stored in another nested dictionary.

def calculate_student_gpa(student):
    """Calculates the Grade Point Average (GPA) for a single student."""
    grades = student['grades']
    if not grades:
        return 0
    scores = grades.values()
    return sum(scores) / len(scores)
        

def find_top_student(student_list):
    """Finds the student with the highest GPA in a list of students."""
    top_student_name = None
    highest_gpa = -1 
    for student in student_list:
        current_gpa = calculate_student_gpa(student)
        if current_gpa > highest_gpa:
            highest_gpa = current_gpa
            top_student_name = student['name']
    return top_student_name
# --- Test your functions ---

students = [
    {
        'name': 'Alice',
        'grades': {'math': 90, 'science': 88, 'history': 92} 
    },
    {
        'name': 'Bob',
        'grades': {'math': 78, 'science': 82, 'history': 80} 
    },
    {
        'name': 'Charlie',
        'grades': {} 
    },
    {
        'name': 'Diana',
        'grades': {'math': 95, 'science': 98, 'history': 99} 
    }
]

top_student = find_top_student(students)
print(f"--- Top Student Report ---")
print(f"The student with the highest GPA is: {top_student}") # Expected: Diana


# --- Practice 6: File I/O - Making Data Persistent ---

import json # Import the json module to work with JSON files.

def save_list_to_file(todo_list, filename):
    """Saves the to-do list to a file using JSON."""
    # 'w' stands for 'write' mode. It will create the file if it doesn't exist,
    # or overwrite it if it does.
    # 'with open' ensures the file is automatically closed.
    with open(filename, 'w') as f:
        # json.dump takes the Python object (todo_list) and writes it
        # into the file object (f) in JSON format.
        json.dump(todo_list, f, indent=4)

def load_list_from_file(filename):
    """Loads the to-do list from a file. Returns an empty list if the file doesn't exist."""
    # We use a try-except block to handle the first run when the file is not yet created.
    try:
        # 'r' stands for 'read' mode.
        with open(filename, 'r') as f:
            # json.load reads from the file object (f) and converts
            # the JSON text back into a Python object (a list in this case).
            return json.load(f)
    except FileNotFoundError:
        # If the file doesn't exist, this block runs instead of crashing.
        # We return an empty list to start fresh.
        return []

def main_persistent_todo_app():
    """A to-do app that saves and loads its data."""
    FILE_NAME = "my_todo_list.json" # Define the filename as a constant.

    # At the start, load the list from the file.
    todo_items = load_list_from_file(FILE_NAME)

    print("\n--- Persistent To-Do List Application ---")

    while True:
        # We can reuse the functions from the previous chapter's exercise.
        # For simplicity, we'll just put the logic here.
        print("\nMenu: 1: Add, 2: View, q: Save & Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("What to add? ")
            todo_items.append(item)
            print(f"Added: {item}")
        elif choice == '2':
            print("\n--- Your List ---")
            for i, item in enumerate(todo_items, 1):
                print(f"{i}. {item}")
        elif choice == 'q':
            # Before quitting, save the current list to the file.
            save_list_to_file(todo_items, FILE_NAME)
            print("List saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

# --- Run the application ---
# The file I/O practice is paused for now.
# main_persistent_todo_app()


def group_sales_by_date(sales_list):
    """Groups a list of sales records by date."""
    group_result = {}
    for sale in sales_list:
        date = sale['date']
        product_sold = sale['product']
        total_sale = sale['amount']
        if date not in group_result:
            group_result[date] = {'total_sale': 0, 'product_sold': []}
        else:
            group_result[date]['total_sale'] += total_sale
            group_result[date]['product_sold'].append(product_sold)

    return group_result
# --- Test your function ---
sales_data = [
    {'date': '2023-10-01', 'product': 'Laptop', 'amount': 1200},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 25},
    {'date': '2023-10-02', 'product': 'Laptop', 'amount': 1250},
    {'date': '2023-10-02', 'product': 'Keyboard', 'amount': 75},
    {'date': '2023-10-01', 'product': 'Mouse', 'amount': 30},
]

grouped_report = group_sales_by_date(sales_data)
print("\n--- Sales Report Grouped by Date ---")
# We use pprint (pretty-print) to make the nested dictionary output easier to read.
import pprint
pprint.pprint(grouped_report)
# Expected output (order of products in list might vary):
# {'2023-10-01': {'products_sold': ['Laptop', 'Mouse', 'Mouse'], 'total_sales': 1255},
#  '2023-10-02': {'products_sold': ['Laptop', 'Keyboard'], 'total_sales': 1325}}


# --- Practice 8: Data Transformation - Flattening Data ---

# This is the reverse of grouping. We take a structured dictionary and
# flatten it into a single list, often adding information along the way.

import pprint

def flatten_employee_data(grouped_employees):
    """
    Takes a dictionary of employees grouped by department and returns a single
    list of all employees, with their department added to their record.
    """
    flat_list = []
    for department_name, employee_list in grouped_employees.items():
        for emp in employee_list:
            new_employee_list = emp.copy()
            new_employee_list['department'] = department_name
            flat_list.append(new_employee_list)
    return flat_list

# --- Test your function ---
employees_by_department = {
    'Sales': [
        {'name': 'Alice', 'employee_id': 'S001'},
        {'name': 'Bob', 'employee_id': 'S002'}
    ],
    'Engineering': [
        {'name': 'Charlie', 'employee_id': 'E001'},
        {'name': 'Diana', 'employee_id': 'E002'}
    ]
}

flat_employee_list = flatten_employee_data(employees_by_department)
print("\n--- Flattened Employee List ---")
pprint.pprint(flat_employee_list)


# --- Practice 9: Data Transformation - inverted_index ---

import pprint

def create_inverted_index(document):
    inverted_index = {}
    for index, doc in enumerate(document):
        new_doc = doc.lower().split(" ")
        for word in new_doc:
            if word not in inverted_index:
                inverted_index[word] = [index]
            else:
                inverted_index[word].append(index)
    return inverted_index            


documents = [
    "the quick brown fox jumps over the lazy dog",
    "the dog is lazy",
    "the fox is quick"
]

inverted_index_result = create_inverted_index(documents)
pprint.pprint(inverted_index_result)



# --- Practice 10: Merging and Summarizing Data ---

# This is a very common real-world task: combining data from multiple sources
# based on a shared key and creating a summary.

import pprint

def create_product_summary(sales, products):
    """
    Merges product information with sales data to create a summary report.
    """
    sales_summary = {}
    
    for sale in sales:
        total_quantity = sale['quantity_sold']
        product_id = sale['product_id']
        #if not yet exist in sales_summary
        if product_id not in sales_summary:
            sales_summary[product_id] = {
                'total_quantity': total_quantity,
                'transaction_count': 1
            }
        else:
            sales_summary[product_id]['total_quantity'] += total_quantity
            sales_summary[product_id]['transaction_count'] += 1
    

    summary_report =[]
    for product in products:
        id_ = product.get('product_id')
        product_name = product.get('name')
        default_sales_data = {'total_quantity': 0, 'transaction_count': 0}
        product_sales_data = sales_summary.get(product_id, default_sales_data)
        current_summary = {
            'product_id': id_,
            'name': product_name,
            'total_quantity_sold': product_sales_data['total_quantity'],
            'number_of_transactions': product_sales_data['transaction_count']
        }
        summary_report.append(current_summary)
    return summary_report  




# --- Test your function ---
product_list = [
    {'product_id': 'p001', 'name': 'Laptop'},
    {'product_id': 'p002', 'name': 'Mouse'},
    {'product_id': 'p003', 'name': 'Keyboard'},
    {'product_id': 'p004', 'name': 'Monitor'}
]

sales_list = [
    {'product_id': 'p001', 'quantity_sold': 2},
    {'product_id': 'p002', 'quantity_sold': 5},
    {'product_id': 'p001', 'quantity_sold': 3},
    {'product_id': 'p003', 'quantity_sold': 1},
    {'product_id': 'p002', 'quantity_sold': 10}
]


result = create_product_summary(sales_list, product_list)
pprint.pprint(result)
              


import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

import pprint
# --- Practice 11: Summarizing and Merging (Student Reports) ---

# This is another practice on the same theme as Practice 10 to help
# solidify the concept of summarizing and merging data.

def generate_student_report_cards(roster, scores):
    """
    Merges student roster information with assignment scores to create
    a list of comprehensive report cards.
    """
    # --- Step 1: Group all scores by student ID ---
    # TODO: Create an empty dictionary `scores_by_student`.
    # TODO: Loop through each `record` in the `scores` list.
        # TODO: Get the student_id and score.
        # TODO: If the student_id is new, initialize its value in `scores_by_student` as an empty list [].
        # TODO: Append the current score to the list for that student_id.
    scores_by_student = {}
    for record in scores:
        student_id = record['student_id']
        student_score = record['score']
        if student_id not in scores_by_student:
            scores_by_student[student_id] = []
        scores_by_student[student_id].append(student_score)    


    # --- Step 2: Create report cards by merging with the roster ---
    # TODO: Create an empty list `report_cards`.
    # TODO: Loop through each `student` in the `roster` list.
        # TODO: Get the student's id and name.
        # TODO: Use .get(student_id, []) to get the list of scores.
        # TODO: Calculate the average score. (Handle the case of an empty list!)
        # TODO: Determine the 'status' ('Pass' or 'Fail').
        # TODO: Create a new dictionary for the report card.
        # TODO: Append the new report card to the `report_cards` list.
    report_cards = []
    for student in roster:
        id_ = student['student_id']
        name = student['name']
        student_scores = scores_by_student.get(id_, [])
        if not student_scores:
            avg_score = 0
        else:
            avg_score = sum(student_scores) / len(student_scores)
        status = 'Pass' if avg_score >= 60 else 'Fail'

        report_card = {
            'student_id': id_,
            'name': name,
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

student_reports = generate_student_report_cards(student_roster, assignment_scores)
print("\n--- Student Report Cards ---")
pprint.pprint(student_reports)


# --- Learning Topic 1: In-depth Lists/Dictionaries ---
# --- Sub-topic 1.1: List Comprehensions ---

# Practice 12: Filtering and Transforming Data with List Comprehensions

def process_sensor_data(readings):
    """
    Processes a list of sensor readings.
    It should:
    1. Filter out any readings that are None (invalid data).
    2. Convert valid readings from Celsius to Fahrenheit (F = C * 9/5 + 32).
    3. Return a new list of Fahrenheit temperatures, rounded to 2 decimal places.
    """
    # TODO: Use a list comprehension to achieve the above.
    # Hint: The comprehension should have both a transformation (expression)
    # and a filtering condition (if).
    []

# Test cases
sensor_readings_1 = [20.5, 22.0, None, 18.3, 25.1]
expected_output_1 = [68.9, 71.6, 64.94, 77.18]

sensor_readings_2 = [None, 0.0, 100.0, None]
expected_output_2 = [32.0, 212.0]

sensor_readings_3 = []
expected_output_3 = []

print("\n--- Practice 12: List Comprehensions ---")

result_1 = process_sensor_data(sensor_readings_1)
print(f"Readings 1: {sensor_readings_1}")
print(f"Processed 1: {result_1}")
print(f"Expected 1: {expected_output_1}")
assert result_1 == expected_output_1
print("Test 1 Passed!")

result_2 = process_sensor_data(sensor_readings_2)
print(f"Readings 2: {sensor_readings_2}")
print(f"Processed 2: {result_2}")
print(f"Expected 2: {expected_output_2}")
assert result_2 == expected_output_2
print("Test 2 Passed!")

result_3 = process_sensor_data(sensor_readings_3)
print(f"Readings 3: {sensor_readings_3}")
print(f"Processed 3: {result_3}")
print(f"Expected 3: {expected_output_3}")
assert result_3 == expected_output_3
print("Test 3 Passed!")

print("All List Comprehension tests passed!")


# --- Sub-topic 1.1: List Comprehensions (Continued) ---

# Practice 13: Extracting from a List of Dictionaries

def get_active_user_emails(users):
    """
    From a list of user dictionaries, extract the lowercase emails of
    only the active users.
    """
    # TODO: Write a single list comprehension to solve this.
    # Hint: The item in the loop will be a dictionary, e.g., `user`.
    # You'll need to access its keys, like `user['is_active']` and `user['email']`.
    return [user['email'].lower() for user in users if user['is_active'] == True]

# Test data
user_list = [
    {'username': 'alice', 'email': 'Alice@Example.com', 'is_active': True},
    {'username': 'bob', 'email': 'Bob@Example.com', 'is_active': False},
    {'username': 'charlie', 'email': 'Charlie@Example.com', 'is_active': True},
    {'username': 'diana', 'email': 'Diana@Example.com', 'is_active': True},
    {'username': 'edward', 'email': 'Edward@Example.com', 'is_active': False},
]

expected_emails = ['alice@example.com', 'charlie@example.com', 'diana@example.com']

print("\n--- Practice 13: List Comprehensions with Dictionaries ---")

active_emails = get_active_user_emails(user_list)
print(f"User List: {user_list}")
print(f"Active Emails: {active_emails}")
print(f"Expected Emails: {expected_emails}")

# Using set for comparison to ignore order, which is a robust testing practice.
assert set(active_emails) == set(expected_emails)

print("Test Passed!")

print("All List Comprehension (Continued) tests passed!")


# --- Sub-topic 1.1: List Comprehensions (Conditional Expressions) ---

# Practice 14: Categorizing Data with Conditional Expressions

def categorize_scores(test_results):
    """
    Categorizes student scores into 'Excellent', 'Pass', or 'Fail'
    using a list comprehension with a nested conditional expression.
    """
    # TODO: Write a single list comprehension.
    # The expression part will need a nested if-else structure:
    # 'value1' if condition1 else ('value2' if condition2 else 'value3')
    return [f"{score['student_name']}: Excellent" if score['score'] >= 90 
        else (f"{score['student_name']}: Pass" if 60 <= score['score'] < 90 
        else f"{score['student_name']}: Fail") for score in test_results
        ]

# Test data
scores_list = [
    {'student_name': 'Alice', 'score': 95},
    {'student_name': 'Bob', 'score': 78},
    {'student_name': 'Charlie', 'score': 59},
    {'student_name': 'Diana', 'score': 90},
    {'student_name': 'Edward', 'score': 60},
]

expected_categories = [
    'Alice: Excellent',
    'Bob: Pass',
    'Charlie: Fail',
    'Diana: Excellent',
    'Edward: Pass',
]

print("\n--- Practice 14: List Comprehensions with Conditional Expressions ---")

categorized_list = categorize_scores(scores_list)
print(f"Categorized List: {categorized_list}")
print(f"Expected List:    {expected_categories}")
assert categorized_list == expected_categories
print("Test Passed!")


# --- Sub-topic 1.1: List Comprehensions (Nested Loops) ---

# Practice 15: Flattening a List of Lists

def get_all_players(teams_data):
    """
    Creates a single flat list of all player names from a list of teams.
    """
    # TODO: Use a list comprehension with nested loops.
    # The outer loop will be `for team in teams_data`.
    # The inner loop will be `for player in team['players']`.
    return [ data for team in teams_data for data in team['players']]
# Test data
teams = [
    {'name': 'Warriors', 'players': ['Curry', 'Thompson', 'Green']},
    {'name': 'Lakers', 'players': ['LeBron', 'Davis']},
    {'name': 'Nets', 'players': ['Durant', 'Irving', 'Simmons']},
]

expected_player_list = ['Curry', 'Thompson', 'Green', 'LeBron', 'Davis', 'Durant', 'Irving', 'Simmons']

print("\n--- Practice 15: List Comprehensions with Nested Loops ---")

all_players = get_all_players(teams)
print(f"All Players: {all_players}")
print(f"Expected:    {expected_player_list}")
assert set(all_players) == set(expected_player_list)
print("Test Passed!")


# --- Sub-topic 1.2: Dictionary Comprehensions ---

# Practice 16: Creating a Lookup Table with Dictionary Comprehension

def create_price_lookup(products):
    """
    Creates a dictionary mapping lowercase product names to their prices.
    """
    # TODO: Use a dictionary comprehension to create the lookup table.
    # Syntax: {key_expression: value_expression for item in iterable}
    return {product['name'].lower(): product['price'] for product in products}

# Test data
product_list = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Keyboard', 'price': 75},
]

expected_lookup = {'laptop': 1200, 'mouse': 25, 'keyboard': 75}

print("\n--- Practice 16: Dictionary Comprehensions ---")
price_lookup = create_price_lookup(product_list)
print(f"Price Lookup Table: {price_lookup}")
assert price_lookup == expected_lookup
print("Test Passed!")


# --- Sub-topic 1.2: Dictionary Comprehensions (Continued) ---

# Practice 17: Dictionary Comprehension with a Condition

def create_admin_email_map(users):
    """
    Creates a dictionary mapping user IDs to their emails, but only for admins.
    """
    # TODO: Use a dictionary comprehension with an `if` condition.
    # The condition should check if user['role'] == 'admin'.
    return {user['id']: user['email'] for user in users if user['role'] == 'admin'}

# Test data
user_list_with_roles = [
    {'id': 101, 'email': 'alice@web.com', 'role': 'admin'},
    {'id': 102, 'email': 'bob@web.com', 'role': 'user'},
    {'id': 103, 'email': 'charlie@web.com', 'role': 'user'},
    {'id': 104, 'email': 'diana@web.com', 'role': 'admin'},
]

expected_admin_map = {101: 'alice@web.com', 104: 'diana@web.com'}

print("\n--- Practice 17: Dictionary Comprehensions with Condition ---")
admin_map = create_admin_email_map(user_list_with_roles)
print(f"Admin Email Map: {admin_map}")
assert admin_map == expected_admin_map
print("Test Passed!")


# --- Sub-topic 1.2: Dictionary Comprehensions (Swapping Keys/Values) ---

# Practice 18: Inverting a Dictionary

def invert_and_format_user_map(user_map):
    """
    Inverts a dictionary, swapping keys and values.
    The new value (the original key) should be capitalized.
    """
    # TODO: Use a dictionary comprehension and the .items() method.
    # The loop should look like `for key, value in user_map.items()`.
    return {value: key.upper() for key, value in user_map.items()}
# Test data
username_to_id = {
    'alice': 101,
    'bob': 102,
    'charlie': 103,
}

expected_id_to_username = {101: 'ALICE', 102: 'BOB', 103: 'CHARLIE'}

print("\n--- Practice 18: Inverting a Dictionary ---")
id_to_username_map = invert_and_format_user_map(username_to_id)
print(f"Inverted Map: {id_to_username_map}")
assert id_to_username_map == expected_id_to_username
print("Test Passed!")

#practice 18 sol 2

def find_duplicate_values(user_map):
    """
    Groups a dictionary by its values to find which values are used by multiple keys.
    """
    # 1. Create an empty dictionary to store the grouped results.
    # The keys will be the values from the original map, 
    # and the values will be a list of original keys.
    value_to_keys_map = {}

    # 2. Iterate through the original map's items.
    for key, value in user_map.items():
        # 3. Use setdefault to ensure a list exists for this value, then append the key.
        # This is the core of the grouping pattern.
        value_to_keys_map.setdefault(value, []).append(key)

    # 4. Now, find the duplicates by checking the length of the lists.
    duplicates = {}
    for value, keys in value_to_keys_map.items():
        if len(keys) > 1:
            duplicates[value] = keys
            
    return duplicates

# --- Test with a dictionary that has duplicate values ---
username_to_id_with_duplicates = {
    'alice': 101,
    'bob': 102,
    'charlie': 103,
    'diana': 101,  # 'diana' has the same ID as 'alice'
    'edward': 103  # 'edward' has the same ID as 'charlie'
}

duplicate_report = find_duplicate_values(username_to_id_with_duplicates)

print("\n--- Duplicate Value Report ---")
if duplicate_report:
    print("Found duplicate values:")
    for value, keys in duplicate_report.items():
        print(f"- Value '{value}' is shared by keys: {keys}")
else:
    print("No duplicate values found.")

# --- Comprehensive Practice: Combining Comprehensions ---

# --- Comprehensive Practice: Combining Comprehensions ---
import pprint
# Practice 19: Log File Processor

def process_logs(log_lines):
    """
    Parses and summarizes a list of log strings.
    """
    # --- Step 1: Parse log strings into a list of dictionaries ---
    # Each string is in the format: "LEVEL:YYYY-MM-DD:Message"
    # Use a list comprehension to transform each line into a dictionary.
    # Hint: Use line.split(':', 2) to split the string into exactly 3 parts. The walrus operator (:=) is used here for efficiency.
    # The result of split will be a list like ['LEVEL', 'YYYY-MM-DD', 'Message'].
    parsed_logs = [
        # The walrus operator (:=) assigns to `parts` and then the expression is evaluated.
        {'level': parts[0], 'date': parts[1], 'message': parts[2]}
        for line in log_lines
        if (parts := line.split(':', 2)) and len(parts) == 3
    ]
    # --- Step 2: Count log entries by level ---
    # Now, loop through your new `parsed_logs` list.
    # Create a summary dictionary that counts how many logs of each level exist.
    # Use the .get(key, 0) + 1 pattern we've practiced.
    level_counts = {}
    for log_dict in parsed_logs:
        level = log_dict['level']
        level_counts[level] = level_counts.get(level, 0) + 1

    # --- Step 3: Return a structured report ---
    report = {
        "level_summary": level_counts,
        "parsed_logs": parsed_logs
    }
    return report

# Test data
log_data = [
    "INFO:2023-10-28:User 'alice' logged in.",
    "ERROR:2023-10-28:Database connection failed.",
    "WARNING:2023-10-28:Disk space is running low.",
    "INFO:2023-10-28:User 'bob' logged out.",
    "ERROR:2023-10-28:Invalid API key provided.",
    "INFO:2023-10-28:Scheduled task completed successfully."
]

print("\n--- Practice 19: Comprehensive Log Processor ---")
final_report = process_logs(log_data)
pprint.pprint(final_report)


# --- Comprehensive Practice 2: Grouping and Aggregation ---

# Practice 20: E-commerce Order Summarizer

def summarize_orders(order_items):
    """
    Groups a list of order items by order_id and calculates a summary for each order.
    """
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
    {'order_id': 'O-1001', 'product_name': 'Keyboard', 'quantity': 1, 'price': 75},
    {'order_id': 'O-1003', 'product_name': 'Monitor', 'quantity': 1, 'price': 300},
    {'order_id': 'O-1002', 'product_name': 'Webcam', 'quantity': 1, 'price': 50},
]

print("\n--- Practice 20: E-commerce Order Summarizer ---")
order_summary_report = summarize_orders(order_data)
pprint.pprint(order_summary_report)


# --- Final Challenge: Website Traffic Analyzer ---

# Practice 21: Website Traffic Analyzer

def analyze_traffic(traffic_logs):
    """
    Analyzes website traffic logs to find total visits and top articles.
    """
    # --- Step 1: Extract URLs from logs ---
    # This list comprehension splits each line and extracts the URL part.
    # It's more readable to do this in a simple loop or a clearer comprehension.
    extracted_urls = [line.split(' - ')[1] for line in traffic_logs]
    
    # --- Step 2: Count URL visits ---
    # Use a dictionary to count how many times each URL appears.
    url_counts = {}
    for url in extracted_urls:
        url_counts[url] = url_counts.get(url, 0) + 1

    # --- Step 3: Find the top 3 articles ---
    # Sort the URL counts by visit count in descending order and get the top 3.
    # FIX: It should be url_counts.items() with parentheses.
    # The key=lambda item: item[1] tells sorted() to use the second element of each item (the count) for sorting.
    sorted_items = sorted(url_counts.items(), key=lambda item: item[1], reverse=True)
    # Extract just the URL (the first element of the tuple) from the top 3 sorted items.
    top_articles = [item[0] for item in sorted_items[:3]]

    # --- Step 4: Prepare the report ---
    report = {
        "total_visits": len(traffic_logs),
        "top_articles": top_articles
    }
    return report

# Test data
traffic_data = [
    "2023-11-05 10:00:00 - /articles/python-best-practices - Chrome",
    "2023-11-05 10:05:00 - /articles/data-structures-explained - Firefox",
    "2023-11-05 10:10:00 - /articles/python-best-practices - Safari",
    "2023-11-05 10:15:00 - /articles/web-development-tips - Chrome",
    "2023-11-05 10:20:00 - /articles/python-best-practices - Chrome",
    "2023-11-05 10:25:00 - /articles/data-structures-explained - Chrome",
    "2023-11-05 10:30:00 - /articles/web-development-tips - Firefox",
    "2023-11-05 10:35:00 - /articles/python-best-practices - Safari",
    "2023-11-05 10:40:00 - /articles/javascript-tips - Chrome",
    "2023-11-05 10:45:00 - /articles/python-best-practices - Chrome"
]

print("\n--- Practice 21: Website Traffic Analyzer ---")
traffic_report = analyze_traffic(traffic_data)
pprint.pprint(traffic_report)
