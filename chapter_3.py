def fibonacci(target):
    cur = 0
    memo = {}

    def get_fib_num(num):
        # if the number is in the memo, return it
        if num in memo:
            return memo[num]
        # if the number is 0 or 1, return it
        if num <= 1:
            return num
        # else, add the number to the memo and return the sum of the two previous numbers
        memo[num] = get_fib_num(num - 1) + get_fib_num(num - 2)
        return memo[num]

    # loop through the fibonacci numbers until the target is reached, using "cur" to keep track of the current number
    while True:
        fib_number = get_fib_num(cur)
        # if the number is greater than the target, exit the loop
        if fib_number > target:
            break
        # else, print the number and increment "cur"
        print(fib_number, end=" ")
        cur += 1

    print()


fibonacci(10)  # => 0 1 1 2 3 5 8
fibonacci(100)  # => 0 1 1 2 3 5 8 13 21 34 55 89
fibonacci(1000)  # => 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
