class Stack:  # Class Stack
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop()


class Queue:  # Class Queue
    def __init__(self):
        self.something = []

    def add(self, other):
        self.something.insert(0, other)

    def remove(self):
        return self.something.pop()

    def size(self):
        return len(self.something)


class Complex:  # Class Complex Number
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def __str__(self):
        sign = '+' if self.img >= 0 else ''
        return '{}{}{}i' .format(self.real, sign, self.img)
    __repr__ = __str__


class ComplexCalc:  # Arithmetic operations for the class Complex
    def add(self, x, y):
        real = x.real + y.real
        img = x.img + y.img
        return Complex(real, img)

    def sub(self, x, y):
        real = x.real - y.real
        img = x.img - y.img
        return Complex(real, img)

    def mul(self, x, y):
        real = x.real * y.real - x.img * y.img
        img = x.img * y.real + x.real * y.img
        return Complex(real, img)

    def abs(self, x):
        return (x.real ** 2 + x.img ** 2) ** 0.5


Stack_data = Stack()
Queue_data = Queue()
Calc = ComplexCalc()

Stack_data.push('World')
Stack_data.push('Hello')
Stack_data.pop()
Stack_data.pop()
Stack_data.push(Calc.add(Complex(5, 2), Complex(6, 2)))
Stack_data.pop()

Queue_data.add('Homework_1')
print(Queue_data.size())
Queue_data.add('It\'s little bit fun( ͡° ͜ʖ ͡°)')
print(Queue_data.size())
Queue_data.add(Calc.abs(Complex(4, 6)))
Queue_data.remove()
Queue_data.remove()
Queue_data.remove()
print(Queue_data.size())

Calc.add(Complex(2, 4), Complex(4, 6))
Calc.sub(Complex(5, 2), Complex(10, 7))
Calc.mul(Complex(4, 2), Complex(4, 2))
Calc.mul(Complex(4, 2), Complex(4, 2))
Calc.abs(Complex(3, 4))