class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def __call__(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
        return result

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        sum_coefficients = [0] * max_len
        for i in range(len(self.coefficients)):
            sum_coefficients[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            sum_coefficients[i] += other.coefficients[i]
        return Polynomial(sum_coefficients)
    
    
poly1 = Polynomial([0, 1])
poly2 = Polynomial([10])
poly3 = poly1 + poly2
poly4 = poly2 + poly1

print(poly3(-2), poly4(-2))
print(poly3(-1), poly4(-1))
print(poly3(0), poly4(0))
print(poly3(1), poly4(1))
print(poly3(2), poly4(2))