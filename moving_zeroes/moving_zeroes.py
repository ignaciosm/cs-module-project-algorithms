'''
Input: a List of integers
Returns: a List of integers
'''

arr1 = [0, 3, 1, 0, -2]


def moving_zeroes(arr):
    zero_indexes = []
    for i in range(0, len(arr)):
        if arr[i] == 0:
            zero_indexes.append(i)
    number_of_zeros = len(zero_indexes)
    for z in ([0] * number_of_zeros):
        arr.append(z)
    for x in zero_indexes[::-1]:
        print('index', x)
        arr.pop(x)
    return arr


print(moving_zeroes(arr1))

# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [0, 3, 1, 0, -2]

#     print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
