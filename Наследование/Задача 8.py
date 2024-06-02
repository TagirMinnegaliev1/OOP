class Summator:
    def transform(self, n):
        return n

    def sum(self, N):
        return sum(self.transform(n) for n in range(1, N+1))


class SquareSummator(Summator):
    def transform(self, n):
        return n ** 2


class CubeSummator(Summator):
    def transform(self, n):
        return n ** 3

N = 5
summator = Summator()
square_summator = SquareSummator()
cube_summator = CubeSummator()

print("Сумма натуральных чисел от 1 до", N, ":", summator.sum(N))
print("Сумма квадратов натуральных чисел от 1 до", N, ":", square_summator.sum(N))
print("Сумма кубов натуральных чисел от 1 до", N, ":", cube_summator.sum(N))