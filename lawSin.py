import math

class Triangle:
    def __init__(self, a=None, b=None, c=None, A=None, B=None, C=None):
        # Assign the given parameters
        self.a = a
        self.b = b
        self.c = c
        self.A = math.radians(A) if A else None
        self.B = math.radians(B) if B else None
        self.C = math.radians(C) if C else None

        # Calculate the remaining angle using the fact that the sum of angles in a triangle is 180 degrees
        if self.A and self.B and not self.C:
            self.C = math.pi - self.A - self.B
        elif self.A and self.C and not self.B:
            self.B = math.pi - self.A - self.C
        elif self.B and self.C and not self.A:
            self.A = math.pi - self.B - self.C

    def calculate_missing_side(self):
        if self.a and self.A and self.B:
            return self.a * math.sin(self.B) / math.sin(self.A)
        elif self.b and self.B and self.A:
            return self.b * math.sin(self.A) / math.sin(self.B)
        elif self.c and self.C and self.A:
            return self.c * math.sin(self.A) / math.sin(self.C)
        elif self.c and self.C and self.B:
            return self.c * math.sin(self.B) / math.sin(self.C)
        elif self.a and self.A and self.C:
            return self.a * math.sin(self.C) / math.sin(self.A)
        elif self.b and self.B and self.C:
            return self.b * math.sin(self.C) / math.sin(self.B)
        else:
            raise ValueError("Insufficient data to calculate a missing side.")

    def calculate_missing_angle(self):
        if self.a and self.b and self.A:
            return math.asin(self.b * math.sin(self.A) / self.a)
        elif self.a and self.c and self.A:
            return math.asin(self.c * math.sin(self.A) / self.a)
        elif self.b and self.c and self.B:
            return math.asin(self.c * math.sin(self.B) / self.b)
        elif self.a and self.c and self.C:
            return math.asin(self.a * math.sin(self.C) / self.c)
        elif self.b and self.c and self.C:
            return math.asin(self.b * math.sin(self.C) / self.c)
        elif self.a and self.b and self.C:
            return math.asin(self.a * math.sin(self.C) / self.b)
        else:
            raise ValueError("Insufficient data to calculate a missing angle.")

# Example usage:
triangle = Triangle(a=5, A=30, B=60)
print("Side b:", triangle.calculate_missing_side())