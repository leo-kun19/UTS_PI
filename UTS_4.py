class BMI:
    def __init__(self, weight_lb, height_ft):
        self.weight = weight_lb
        self.height = height_ft

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight_lb):
        if weight_lb <= 0:
            raise ValueError("harus positive.")
        self._weight = weight_lb

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height_ft):
        if height_ft <= 0:
            raise ValueError("Harus positive.")
        self._height = height_ft

    def bmi_value(self):
        height_m = self.height * 0.3048  # Convert feet to meters
        weight_kg = self.weight * 0.453592  # Convert pounds to kilograms
        return weight_kg / (height_m ** 2)

    def __eq__(self, other):
        if isinstance(other, BMI):
            return self.weight == other.weight and self.height == other.height
        return False

# Example usage:
person1 = BMI(weight_lb=123, height_ft=5.7)
person2 = BMI(weight_lb=113, height_ft=5.5)

print("Person 1 BMI:", person1.bmi_value())
print("Person 2 BMI:", person2.bmi_value())

print("Are the weights and heights equal?", person1 == person2)
