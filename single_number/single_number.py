'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''

e1 = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]


def single_number(arr):

    non_duplicates = []
    for i in arr:
        if not i in non_duplicates:
            non_duplicates.append(i)

    count = [0] * len(non_duplicates)
    for x in arr:
        if x in non_duplicates:
            idx = non_duplicates.index(x)
            count[idx] += 1

    return non_duplicates[count.index(1)]


print(single_number(e1))

# if __name__ == '__main__':
#     # Use the main function to test your implementation
#     arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

#     print(f"The odd-number-out is {single_number(arr)}")
