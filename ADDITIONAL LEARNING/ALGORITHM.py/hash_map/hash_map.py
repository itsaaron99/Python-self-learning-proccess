"""
 - Leetcode: TwoSum

By using hashmap to solve the problem.
- Store the data into dict if the data doesn't exist.
- If data already exist in dict, return the data.
- Practical application: Web DSN Resolution, Cache (hit or miss)...etc
"""

def TwoSum(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]

        hash_map[num] = i
    return None

if __name__ == "__main__":
    """ Test case 1: Original test, corrected call """
    nums1, target1 = [2, 5, 4, 7, 3], 10
    assert TwoSum(nums1, target1) == [3, 4]

    """ Test case 2: Original test with duplicates, corrected call """
    nums2, target2 = [0, 3, 3, 6], 3
    assert TwoSum(nums2, target2) == [0, 1]

    """ Test case 3: Another common case """
    nums3, target3 = [3, 3], 6
    assert TwoSum(nums3, target3) == [0, 1]

    """ Test case 4: No solution found """
    nums4, target4 = [1, 2, 3, 4], 8
    assert TwoSum(nums4, target4) is None

    """ Test case 5: With negative numbers """
    nums5, target5 = [-1, -3, 5, 9], 4
    assert TwoSum(nums5, target5) == [0, 2]

    """ Test case 6: Empty list """
    nums6, target6 = [], 10
    assert TwoSum(nums6, target6) is None

    print("All tests passed!")