'''
Input: an integer
Returns: an integer
'''

n = 5  # how many cookies in a jar
x = 3  # how many can cookie monster eat at once
result = 13


def eating_cookies(n, cache=None):
    # cookies = [1, 2, 3, 4, 5]
    # eaten = cookies
    # bite3 = []
    # bite2 = []
    # bite1 = []
    # current_bite = 3

    if n < 0:
        return 0

    # base case
    if n == 0:
        return 1

    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]

    cache[n] = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

    return cache[n]

    # while current_bite > 0:
    #     for i in range(len(cookies)):
    #         if len(cookies[i:i+current_bite]) == current_bite:
    #             print(cookies[i:i+3])
    #             bite3 += cookies[i:i+3]
    #             # eaten[i] = 0
    #     current_bite -= 1
    # total = bite1 + bite2 + bite3

    # for i in range(len(cookies)):
    #     if len(cookies[i:i+3]) == 3:
    #         print(cookies[i:i+3])
    #         bite3 += cookies[i:i+3]
    #     elif len(cookies[i:i+3]) == 2:
    #         print(cookies[i:i+3])
    #         bite2 += 1
    #     elif len(cookies[i:i+3]) == 1:
    #         print(cookies[i:i+3])
    #         bite1 += 1
    # eating_cookies(cookies)
    # total = bite1 + bite2 + bite3

    # return total[n]


print(eating_cookies(10))


# if __name__ == "__main__":
#     # Use the main function here to test out your implementation
#     num_cookies = 5

#     print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
