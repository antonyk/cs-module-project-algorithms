'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # as window moves to the right, if newest > than max, max = newest...
    if k > len(nums):
        raise Exception("window must be less than or equal to list width")
    if k < 1:
        raise Exception("window must be at least width of 1")

    # init
    start = 0
    result = []

    # iterate over nums array, moving the window (recreating it)
    # at each iteration, get largest in window and append to result
    while start <= (len(nums) - k):
        window = sorted(nums[start:start+k])
        result.append(window[-1])
        start += 1

    return result


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
