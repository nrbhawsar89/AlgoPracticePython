# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum
# of any contiguous subarray of size ‘k’.
#
# Example 1:
#
# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:
#
# Input: [2, 3, 4, 1, 5], k=2
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].

def find_max_sub_array(arr, K):
    _sum = 0
    for i in range(0, K):
        _sum = _sum + arr[i]
    _max = 0
    for i in range(1, len(arr) - K + 1):
        _sum = _sum - arr[i - 1] + arr[i + K - 1]
        _max = max(_max, _sum)
    return _max

print (find_max_sub_array([2, 1, 5, 1, 3, 2], 3))