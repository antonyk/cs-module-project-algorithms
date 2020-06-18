'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    mix = [1] * len(arr)

    # O(n^2) time, O(1) space, no division
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                mix[i] = mix[i] * arr[j]


    # O(n) time, O(1) space, uses division
    # total = 1
    # for i in range(len(arr)):
    #     total *= arr[i]
    # for i in range(len(arr)):
    #     mix[i] = total / arr[i]

    return mix

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
