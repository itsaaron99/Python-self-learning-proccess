"""
CHAPTER 3 Recursion
TD;RL
 - When function calls itself in the funtion
 - The function requred:
    - Required a "Base case" to be the condition to stop the recursion.
    - Required a "Recusive case" as executing the repeat action.
"""

def countdown(i):
    print(i)
    if i <= 1:
        return
    else:
        countdown(i-1)


def ispowerOfThree(n):
    if n < 1:
        return False
    if n == 1:
        return True
    return n % 3 == 0 and ispowerOfThree(n // 3)

"""
D & C

Find the base case,
write Sum function with recursion
"""

def sum_array(arr):
    """
    Practice 4.1 sum function -> add all variables
    base case: try to decrease the variables amount in the arr to 0
        example: [2, 4, 6] -> 2 + [4, 6] -> 4 + [6] -> 6 + []
    """
    if arr == []:
        return 0
    return arr[0] + sum_array(arr[1:])


def count_var(arr):
    """
    Practice 4.2 count_var -> count variable amount in arr
    base case: try to decrease the variables amount in the arr to 0, set a counter if there're variable exists
    example: [2, 4, 6] -> return 3
    """
    if arr == []:
        return 0
    return 1 + count_var(arr[1:])


def find_max(arr):
    """
    Pick the first var, let the rest of the vars do comparision,
    last step: let fist var compaare with the max(the_rest)
    example: [2, 4, 6] -> return 6
    """
    
    if len(arr) == 1:
        return arr[0]
    sub_max = find_max(arr[1:])
    if sub_max > arr[0]: 
        return sub_max
    return arr[0]

    

def mult(arr):
    """
    Product of Array
    base case: if arr == [], return 1
    example: [2, 4, 6] -> return 48

    """

    if arr == []:
        return 1
    if len(arr) == 1:
        return arr[0]
    product = mult(arr[1:])
    return arr[0] * product    


def in_list(arr, target):
    """
    Find the var is in list or not
    base case: 
        if target is in the first index, return the target
        if arr is []
    example: arr = [2, 4, 6], target = 4 -> return True
    """
    if arr[0] == target:
        return True
    if arr == []:
        return False

    return in_list(arr[1:], target)


def count_num(arr, target):
    """
    Count the amount of the target
    base case: if arr == [], return 0
    example: arr = [2, 4, 6, 2], target = 2 -> return 2
    """

    if arr == []:
        return 0
    sub_count = count_num(arr[1:], target)
    if arr[0] == target:
        return 1 + sub_count
    return sub_count


def remove_var(arr, target):
    """
    Remove the target in arr, and return a new list
    base case: 
        if arr == []: return []
        example: remove_var([2, 4, 6, 2], 2) -> return [4, 6]
    """
    result = []
    if not arr: return []
    sub_list = remove_var(arr[1:], target)
    if arr[0] == target:
        return sub_list
    return arr[0] + sub_list


def are_all_odd(arr):
    """
    return True if all vals are odd, else return False
    base case:
        if not arr, return []
        example: are_all_odd([2, 4, 6, 2]) -> return False
    """
    if not arr:
        return True
    is_rest_odd = are_all_odd(arr[1:])
    if arr[0] % 2 == 0 or is_rest_odd == False:
        return False
    return True
    

    
def count_char(arr, target):
    """
    count the target var
    base case:
        if not arr, return 0
    example : count_char(arr = [2, 5, 6, 2, 2], 2) -> return 3
    """
    if not arr:
        return 0
    sub_count = count_char(arr[1:], target)
    if arr[0] == target:
        return 1 + sub_count
    return sub_count

def remove_char(s, target):
    """
    remove the char from the arr, and return the rest
    base case:
        if not s, return ""
    example : remove_char(s = "apple", p) -> return "ale"
    """

    if not s:
        return ""
    sub_char = remove_char(s[1:], target)
    if s[0] != target:
        return s[0] + sub_char
    return sub_char


def is_palindrome(s):
    """
    Find if s is palindrome
    base case:
        if not s, return False
    example: is_palindrome("sdghgds") -> return True
    """
    if s == "" or len(s) == 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


def get_smaller(arr, pivot):
    """
    Find numbers <= than pivot, and return them into a new list
    Base case:
        if not arr or len(arr) == 0, return []
    example: get_smaller([8, 3, 1, 7], 5) -> return [3, 1]
    """
    if not arr or len(arr) == 0:
        return []
    sub_list = get_smaller(arr[1:], pivot)
    if arr[0] <= pivot:
        return [arr[0]] + sub_list
    return sub_list

    
    

