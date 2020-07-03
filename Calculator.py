from dataclasses import dataclass

@dataclass
class Calculator:
       
    def add(self, x, y):
        return round(x + y, 12) #floating point precision

    def subtract(self, x, y):
        return round(x - y, 12) 
    
    def multiply(self, x, y):
        return round(x * y, 12)
