def find_sum_sub_array(arr, K):
    result = []
    sum = 0
    for i in range(0, K):
        sum = sum + arr[i];
    result.append(sum)
    for i in range(1, len(arr) - K + 1):
        result.append(result[i - 1] - arr[i -1] + arr[i + K - 1])
    return result
print (find_sum_sub_array([1,2,3,4,5,6,7], 2))

