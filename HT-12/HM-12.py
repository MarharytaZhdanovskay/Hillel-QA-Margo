"""
Hometask 12. recursive_function

Task description:
 Given list of list of list etc of integers
 write recursive function that will accept as argument target list
 and return sum of all integers inside it
 Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
 Output: Target sum = 72
"""


def nested_list_sum(target_list):
    total = 0

    for item in target_list:
        if isinstance(item, list):
            total += nested_list_sum(item)
        elif isinstance(item, int):
            total += item

    return total


input_list = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

result = nested_list_sum(input_list)

print(f"Target sum = {result}")
