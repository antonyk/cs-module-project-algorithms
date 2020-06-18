'''
Input: an integer
Returns: an integer
'''

# def eating_cookies(n):
#     # Runtime: O(3^n)
#     if n < 0:
#         return 0
#     if n == 0:
#         return 1
#     else:
#         return eating_cookies(n - 1) + eating_cookies(n - 2) + eating_cookies(n - 3)


def eating_cookies(n, cache=None):
    if cache == None:
        cache = {i: 0 for i in range(n + 1)}

    # use dictionary as cache
    # key is n, value is the accumulated number
    if n < 0:
        return 0
    if n == 0:
        return 1

    # check if answer is in the cache
    if cache[n] > 0:
        return cache[n]
    else:
        # perform recursive logic and save the answer in the cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]



if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 10
    # cache = dict()

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")

    # print(f"There are {eating_cookies(num_cookies, cache)} ways for Cookie Monster to eat {num_cookies} cookies")


'''

cookies: 1, 2, 3

perms = 0
def cookie(n):
    perms = 0

    if n == 0:
        return perms
    else:
        if n > 0:
            # x = n - 1 = 0
            # cookie(n)
            perms += 1
            return perms += cookie(n-1)
    elif n > 1:
        if n == 2:
            perms += 1
        cookie(..., n-1)

         n > 1:


'''
