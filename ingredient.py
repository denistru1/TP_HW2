class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit 

    @property
    def quantity(self):
        return self.quantity

    @quintity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
    
    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"
    
    def __repr__(self):
        return f"Ingredient('{self.name}', '{self.quantity}', '{self.unit}')"
    
    def __eq__(self, other):
        if self.name == other.name and self.unit == other.unit:
            return True
        return False
    

