"""
Quick sort:

Find random element for pivot(assume = arr[0]), which will split the arr into 3 partitions, including:
- the pivot
- smaller than the pivot and greater
- use fro loop to compare the smaller and greater itself
- Finally, return [smaller] + [pivot] + [greater]

Example: arr = [3, 5, 2, 4, 1]

pick arr[0] for pivot:
-> [2, 1] + 3 + [5, 4]
-> qsort[2, 1] + 3 + qsort[5, 4]
-> Finally return [1, 2, 3, 4 ,5]


Base case:
    if len(arr) < 2 (1 element left)
"""


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        """ case for there elements duplicated in arr, <= pivot & >= pivot """
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":

    test = [3, 5, 2, 4, 1]
    fail = []
    mutiple_ele = [3, 5, 3, 2, 4, 1]

    assert quick_sort(test) == [1, 2, 3, 4 ,5]
    assert quick_sort(fail) == []
    assert quick_sort(mutiple_ele) == [1, 2, 3, 3, 4, 5]

    print("All tests pass!!!")

