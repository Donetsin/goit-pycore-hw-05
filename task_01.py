'''Module providing a function.'''
def caching_fibonacci():
    '''returns fibonacci using recursion'''
    cached_numbers = {}
    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n not in cached_numbers:
            cached_numbers[n] = fibonacci(n - 1) + fibonacci(n - 2)

        return cached_numbers[n]
    return fibonacci
