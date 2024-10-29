from doctest import testmod

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

class Fraction:
    """
    A class to represent fractions and perform arithmetic with them.

    >>> Fraction(5)  # Whole number fraction
    Fraction(5)

    >>> Fraction(0)  # Zero numerator
    Fraction(0)

    >>> Fraction(6, 3)  # Fraction that reduces to a whole number
    Fraction(2)

    >>> Fraction(15, 5)  # Another fraction that reduces to a whole number
    Fraction(3)

    >>> Fraction(4, 8)  # Fraction that simplifies to 1/2
    Fraction(1, 2)

    >>> Fraction(-4, 8)  # Negative fraction that simplifies to -1/2
    Fraction(-1, 2)

    >>> Fraction(9, -12)  # Negative denominator, simplifies to -3/4
    Fraction(-3, 4)

    >>> Fraction(-10, -20)  # Negative numerator and denominator, simplifies to 1/2
    Fraction(1, 2)

    >>> Fraction(1, 2) + Fraction(1, 2)  # Adding two fractions
    Fraction(1)

    >>> Fraction(2, 3) + Fraction(1, 6)  # Adding two fractions with different denominators
    Fraction(5, 6)

    >>> Fraction(3, 4) - Fraction(1, 2)  # Subtracting fractions
    Fraction(1, 4)

    >>> Fraction(5, 6) - Fraction(1, 3)  # Subtracting fractions with different denominators
    Fraction(1, 2)

    >>> Fraction(2, 3) * Fraction(3, 4)  # Multiplying fractions
    Fraction(1, 2)

    >>> Fraction(5, 7) * Fraction(2, 3)  # Multiplying fractions with different denominators
    Fraction(10, 21)

    >>> Fraction(3, 4) / Fraction(3, 4)  # Dividing fractions
    Fraction(1)

    >>> Fraction(1, 2) / Fraction(1, 4)  # Dividing fractions with different denominators
    Fraction(2)

    >>> Fraction(1, 3) == Fraction(2, 6)  # Test equality with simplified fractions
    True

    >>> Fraction(4, 9) == Fraction(4, 9)  # Test equality with identical fractions
    True

    >>> Fraction(1, 2) < Fraction(3, 4)  # Less than comparison
    True

    >>> Fraction(-1, 3) < Fraction(1, 3)  # Less than comparison with negative fraction
    True

    >>> Fraction(3, 4) > Fraction(1, 2)  # Greater than comparison
    True

    >>> Fraction(2, 3) > Fraction(-1, 3)  # Greater than comparison with negative fraction
    True

    >>> Fraction(1, 2) <= Fraction(2, 4)  # Less than or equal comparison
    True

    >>> Fraction(1, 3) <= Fraction(1, 3)  # Less than or equal with equality
    True

    >>> Fraction(3, 4) >= Fraction(3, 5)  # Greater than or equal comparison
    True

    >>> Fraction(-1, 2) >= Fraction(-1, 3)  # Greater than or equal with negative fractions
    False

    >>> Fraction(1, 3) != Fraction(2, 3)  # Not equal comparison
    True

    >>> Fraction(1, 4) != Fraction(1, 4)  # Not equal comparison with equality (should be False)
    False

    >>> str(Fraction(1, 2))  # String representation
    '1/2'

    >>> str(Fraction(-1, 3))  # Negative fraction string representation
    '-1/3'

    >>> repr(Fraction(1, 2))  # Representation with fraction
    'Fraction(1, 2)'

    >>> repr(Fraction(3))  # Representation with whole number
    'Fraction(3)'
    """

    def __init__(self, numerator, denominator=1):
        common = gcd(numerator, denominator)
        self.numerator = numerator // common
        self.denominator = denominator // common
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        if self.denominator == 1:
            return f"Fraction({self.numerator})"
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other):
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __lt__(self, other):
        return (self.numerator * other.denominator <
                other.numerator * self.denominator)

    def __le__(self, other):
        return (self.numerator * other.denominator <=
                other.numerator * self.denominator)

    def __gt__(self, other):
        return (self.numerator * other.denominator >
                other.numerator * self.denominator)

    def __ge__(self, other):
        return (self.numerator * other.denominator >=
                other.numerator * self.denominator)

    def __ne__(self, other):
        return not self == other

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __sub__(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def __truediv__(self, other):
        new_num = self.numerator * other.denominator
        new_den = self.denominator * other.numerator
        return Fraction(new_num, new_den)

if __name__ == "__main__":
    testmod()
