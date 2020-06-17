'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # iterate over the array
    # if we find a zero, swap with the last non-zero value in the array
    last = len(arr)-1
    cur = 0

    while cur < last:
        if arr[cur] == 0:
            while arr[last] == 0 and cur < last:
                last -= 1
            if arr[last] != 0:
                arr[cur], arr[last] = arr[last], arr[cur]
            else:
                break
        cur += 1

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")