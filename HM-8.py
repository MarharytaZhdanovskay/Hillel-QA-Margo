"""
Hometask 08. max_three_multiplication

Sort the list in ascending order
Case 1: If two smallest negative numbers and the largest non-negative number give the maximum product
Case 2: If all numbers are non-negative or all negative

Task description:
Given the list of integers ( positive , negative, zeros)
Find max multiplication of three values in list
l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]

Input: [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]
Output: Max value = "360". Nums are: (12, 5, 6)

Input: [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
Output: Max value = "2016". Nums are: (-7, 12, -24)

"""


def max_multiplication_of_three(nums):
    nums.sort()
    n = len(nums)

    max_product_1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

    max_product_2 = nums[0] * nums[1] * nums[n - 1]

    return max(max_product_1, max_product_2)


l1 = [-7, 1, 2, 0, 3, 12, -24, 5, -1, 6]
result = max_multiplication_of_three(l1)
print(result)

l2 = [-1, 1, 2, 0, 3, 12, 4, 5, -1, 6]

result2 = max_multiplication_of_three(l2)
print(result2)
