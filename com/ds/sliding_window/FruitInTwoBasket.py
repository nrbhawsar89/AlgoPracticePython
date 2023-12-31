# You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.
#
# You will be given an array of characters where each character represents a fruit tree. The farm has following restrictions:
#
# Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
# You can start with any tree, but you can’t skip a tree once you have started.
# You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.
# Write a function to return the maximum number of fruits in both baskets.
#
# Example 1:
#
# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']
# Example 2:
#
# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket.
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

# ['A', 'B', 'C', 'A', 'C']
def find_max_fruit(arr):
    basket_count = {}
    start = 0
    end = 0
    max_count = 0
    count = 0
    while end < len(arr):

        while len(basket_count) <= 2 and end < len(arr):
            last_fruit = arr[end]
            if last_fruit in basket_count:
                basket_count[last_fruit] = basket_count[last_fruit] + 1
            else:
                basket_count[last_fruit] = 1
            end = end + 1
            count = count + 1
            if len(basket_count) <= 2:
                max_count = max(max_count, count)
        while len(basket_count) > 2:
            start_fruit = arr[start]
            basket_count[start_fruit] = basket_count[start_fruit] - 1
            count = count - 1
            if basket_count[start_fruit] == 0:
                del basket_count[start_fruit]
            start = start + 1
    return max_count

print (find_max_fruit(['A', 'B', 'C', 'A', 'C']))