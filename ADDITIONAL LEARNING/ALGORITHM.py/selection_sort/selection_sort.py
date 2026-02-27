"""
CHAPTER 2 selection sort.
Array & linked list

TD;RL
1. Selection sort trade-off
    - Read fast -> Array
    - Add / Delete fast -> Linked list(based on it finds the target element)
2. Demonstrates the O(n^2) / O(n) / O(1) Time complexity 
"""


def FindSmallest(arr) -> int:
    """ Find smallest elemet int arr (normal) """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
            smallest = arr[i]
    return smallest_index


""" Use Selection Sort """

def Selection_sort(arr):
    newArr = []
    for i in range(len(arr)):
        Smallest = FindSmallest(arr)
        newArr.append(arr.pop(Smallest))
    return newArr


if __name__ == "__main__":
    test_arr = [5, 3, 6, 2, 10]

    assert Selection_sort(test_arr) == [2, 3, 5, 6, 10]

    print("All tests passed!!!")

