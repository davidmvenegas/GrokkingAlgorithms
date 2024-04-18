def fibonacci(target):
    cur = 0
    memo = {}

    def get_fib_num(num):
        if num in memo:
            return memo[num]
        if num <= 1:
            return num
        memo[num] = get_fib_num(num - 1) + get_fib_num(num - 2)
        return memo[num]

    while True:
        fib_number = get_fib_num(cur)
        if fib_number > target:
            break
        print(fib_number, end=" ")
        cur += 1

    print()


fibonacci(10)  # => 0 1 1 2 3 5 8
fibonacci(100)  # => 0 1 1 2 3 5 8 13 21 34 55 89
fibonacci(1000)  # => 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
