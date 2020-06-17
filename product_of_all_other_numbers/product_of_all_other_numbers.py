'''
Input: a List of integers
Returns: a List of integers
'''

arr1 = [1, 7, 3, 4]
expected = [84, 12, 28, 21]


def product_of_all_other_numbers(arr):
    new_arr = []

    for i in range(len(arr)):
        result = 1
        left = arr[:i]
        right = arr[i+1:]
        terms = []
        # print('left', left)
        # print('right', right)
        if len(left) > 0:
            terms += left
        if len(right) > 0:
            terms += right
        print(arr[i], terms)
        for x in terms:
            result *= x
        new_arr.append(result)

    return new_arr


print(product_of_all_other_numbers(arr1))


# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     # arr = [1, 2, 3, 4, 5]
#     arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

#     print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
