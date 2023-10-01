from .Component import Component
from .enum.Certificate import Certificate

class Font(Component):
    
    def __init__(self, name: str, brand: str, power: int, certificate: int = Certificate.BOMB):
        super().__init__(name, brand)
        self.power = power
        self.certificate = certificate
    
    
    def __str__(self):
        return f"{self.brand} {self.name} {Certificate.__str__(self.certificate)} {self.power}W"