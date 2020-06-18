'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


def sliding_window_max(nums, k):
    length = len(nums) - k + 1
    output = []

    for i in range(len(nums)):
        win = []
        win = nums[i:i+k]
        # if len(dirty_win) == k:
        #     win = dirty_win
        m = max(win)
        output.append(m)
        # print(output)

    return output[:length]


print(sliding_window_max(arr, 3))

# if __name__ == '__main__':
#     # Use the main function here to test out your implementation
#     arr = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3

#     print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
