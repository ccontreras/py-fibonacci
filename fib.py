
class Fibonacci(object):
    """docstring for Fibonacci."""
    def __init__(self):
        super(Fibonacci, self).__init__()

    def recursive(self, num):
        if (num <= 2):
            return 1

        return self.recursive(num - 1) + self.recursive(num - 2)

    def normal(self, num):
        if (num <= 2):
            return 1

        i = 0
        j = 1
        m = 0

        for n in range(1, num):
            m = i + j
            i = j
            j = m

        return m

fib = Fibonacci()

print('Recursive mode:', fib.recursive(num = 10))
print('Normal mode:', fib.normal(num = 10))
