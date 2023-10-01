from .Component import Component

class GPU(Component):
    
    def __init__(self, name: str, brand: str, coreClock: int, memoryClock: int, vram: int):
        super().__init__(name, brand)
        self.coreClock = coreClock
        self.memoryClock = memoryClock
        self.vram = vram
        
    
    
    def getTDP(self) -> int:
        energyMultiplier = 0.05
        tdp = (self.coreClock + self.memoryClock) * energyMultiplier
        return int(tdp)
    
    def __str__(self):
        return f"{self.brand} {self.name} {self.vram} MB"