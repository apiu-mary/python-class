class Fruit:
    type =  "category"
    def __init__(self, name, color, taste):
        self.name = name
        self.color = color
        self.taste = taste
    def peel(self):
        return f"Peeling the {self.color} {self.name}"
    def eat(self):
        return f"Eating the {self.color} {self.name} with {self.taste} taste"
    def discard(self):
        return f"Discarding the {self.color} {self.name}."
