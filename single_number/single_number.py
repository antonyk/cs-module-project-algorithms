'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # adds a new array that is sorted. => doubles memory usage
    # arr = sorted(arr)

    # best space complexity but probably slowest in time complexity
    for i in range(len(arr)):
        if arr.count(arr[i]) < 2:
            return arr[i]
    
    return None


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")

