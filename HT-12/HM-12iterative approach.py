"""
Hometask 12.
This updated code uses a stack for iterative traversal of nested lists instead
of recursive calls.
This way, you will avoid the "RecursionError" when processing large or deeply
nested lists.

Task description:
 Given list of list of list etc of integers
 write recursive function that will accept as argument target list
 and return sum of all integers inside it
 Input: [[[[1, 4, 5], [[6, 9],[[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]
 Output: Target sum = 72
"""


def nested_list_sum(target_list):
    total = 0
    stack = [target_list]

    while stack:
        current_list = stack.pop()
        for item in current_list:
            if isinstance(item, list):
                stack.append(item)
            elif isinstance(item, int):
                total += item

    return total


input_list = [[[[1, 4, 5], [[6, 9], [[[8, 1], 7], 3], 2], 7], 5, 2], 9, [1, 2]]

result = nested_list_sum(input_list)

print(f"Target sum = {result}")
