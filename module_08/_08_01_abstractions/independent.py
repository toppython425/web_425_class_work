class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Знаменатель не может быть равен нулю")

        self.numerator = numerator
        self.denominator = denominator

    def add(self, numerator_1, denominator_1):
        new_denominator = self.denominator * denominator_1
        new_nomenator = self.numerator * denominator_1
        new_nomenator_1 = numerator_1 * self.denominator
        return f"{new_nomenator + new_nomenator_1}/{new_denominator}"

    def multiply(self, numerator_1, denominator_1):
        new_numerator = self.numerator * numerator_1
        new_denominator = self.denominator * denominator_1
        return f"{new_numerator}/{new_denominator}"

    def divide(self, numerator_1, denominator_1):
        if denominator_1 == 0:
            raise ZeroDivisionError("На ноль делить нельзя")
        new_numerator = self.numerator * denominator_1
        new_denominator = self.denominator * numerator_1
        return f"{new_numerator}/{new_denominator}"

fraction_1 = Fraction(2, 3)
print(fraction_1.add(3, 5))
print(fraction_1.multiply(2, 4))
print(fraction_1.divide(2, 3))

