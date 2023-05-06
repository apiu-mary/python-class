class Car:
    make = "benz"
    def __init__(self,model,color,year):
        self.model =model
        self.color=color
        self.year=year
    def start_engine(self):
        return f"{self.clor} {self.model} has a very good engine"
    def accelerate(self):
        return f"{self.color} was released in {self.year}"
    def stop(self):
        return f"the{self.medel} has stop at a junctions"
            
        
        