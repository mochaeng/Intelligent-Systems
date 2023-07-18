# article
# https://en.wikipedia.org/wiki/Automatic_differentiation
# backpropagation example from gilbert strang class

import math

class Var:
    def __init__(self, value, children=None) -> None:
        self.value = value
        self.children = children or []
        self.grad = 0

    def __add__(self, other):
        return Var(self.value + other.value, [(1, self), (1, other)])

    def __mul__(self, other):
        if isinstance(other, Var):
            return Var(self.value * other.value, [(other.value, self), (self.value, other)])
        return Var(self.value * other, [(other, self)])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, exponent):
        return Var(self.value ** exponent, [(exponent * self.value ** (exponent - 1), self)])

    def sin(self):
        return Var(math.sin(self.value), [(math.cos(self.value), self)])
    
    def calc_grad(self, grad=1):
        self.grad += grad
        for coef, child in self.children:
            child.calc_grad(grad * coef)


x = Var(2)
y = Var(3)

# f = x * y + x.sin()
f = x ** 3 * (x + 3 * y)

f.calc_grad()

print(f'f = {f.value}')
print(f'∂f/∂x = {x.grad}')
print(f'∂f/∂y = {y.grad}')

