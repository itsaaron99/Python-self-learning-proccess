"""
CHAPTER 1 Binary Search.
time complexity O(log n), before using this algorithm, the list should be sorted first.

Example: guess the number
"""

def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        """ Find the mid index """
        mid = (low + high) // 2
        """ Value of the mid """
        guess = arr[mid]

        """ 
        The mid will replace the low or high,
        It depends on the guess is higher or lower than mid.
        If higher, the mid will replace to be high, vice versa.
        """
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

if __name__ == "__main__":
    test_arr = [1, 3, 5, 7, 9]
    
    assert binary_search(test_arr, 5) == 2
    assert binary_search(test_arr, 11) == None
    assert binary_search(test_arr, 9) == 4
    
    print("Tests pass!!!")
