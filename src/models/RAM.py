from .Component import Component

class RAM(Component):
    
    def __init__(self, name: str, brand: str, size: int, clock: int, maxClock: int):
        super().__init__(name, brand)
        self.size = size
        self.clock = clock
        self.maxClock = maxClock
    
    def getTDP(self) -> int:
        energyMultiplier = 0.005
        tdp = self.clock * energyMultiplier
        return int(tdp)
    
    def __str__(self):
        return f"{self.brand} {self.name} {self.size} MB @ {self.clock} Mhz"