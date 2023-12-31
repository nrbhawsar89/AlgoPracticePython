# Given an array of positive integers and a number ‘S,’ find the
# length of the smallest contiguous subarray whose sum is greater than or
# equal to ‘S’. Return 0 if no such subarray exists.
#
# Example 1:
#
# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].
#
# Example 2:
#
# Input: [2, 1, 5, 2, 8], S=7
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [8].
#
# Example 3:
#
# Input: [3, 4, 1, 1, 6], S=8
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to ‘8’ are [3, 4, 1] or [1, 1, 6].

def find_smallest_subarray(arr, S):
    start = 0;
    end = 0;
    array_sum = 0;
    min_length = len(arr)
    while end <= len(arr) - 1:
        while array_sum < S and end <= len(arr) - 1:
            array_sum += arr[end]
            end = end + 1
        while array_sum >= S:
            length = end - start
            min_length = min(min_length, length)
            start = start + 1
            array_sum = array_sum - arr[start - 1]

    return min_length

print (find_smallest_subarray([2, 1, 5, 2, 3, 2], 10))

