"""
Merge Sort:
    The conceptual reverse of Quick Sort. (Easy divide, Hard merge)

Differences:
    Quick Sort: Time Complexity O(n log n) average, O(n^2) worst case.
    - Divides the array into 3 parts: less, pivot, and greater. 
    - The pivot should be randomly CHOSEN to avoid worst-case performance.
    - Finally, combines all parts EASILY using the `+` operator.
    - Edge case: May cause a Timeout or Recursion Crash (Stack Overflow) 
      if 'n' is extremely large and the pivot is chosen poorly (e.g., highly unbalanced splits).

    Merge Sort: Time Complexity strictly O(n log n).
    - No matter the elements, it always blindly splits the array in half: mid = len(arr) // 2.
    - Then, it uses a helper function `merge()`.
    - `merge()` uses two pointers (i & j) to compare elements from the `left` and `right` arrays, 
      picking the smaller one to append into the `result` array.
    - The final returned `result` will be perfectly sorted.
"""

def merge_sort(arr):
    if len(arr) < 2: return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return helper_merge(left, right)

def helper_merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

if __name__ == "__main__":
    
    test1 = [5, 7, 2, 9, 3, 0]
    test_hard = list(reversed(range(999))) 

    assert merge_sort(test1) == [0, 2, 3, 5, 7, 9]
    assert merge_sort(test_hard) == sorted(range(999))

    print("All tests passed !!!")
    