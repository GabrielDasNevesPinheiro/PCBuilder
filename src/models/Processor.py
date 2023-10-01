from .Component import Component

class Processor(Component):
    
    def __init__(self, name: str, brand: str, socket: str, clock: int, maxMemoryClock: int, cores: int, logicalCores: int):
        super().__init__(name, brand)
        self.socket = socket
        self.clock = clock
        self.maxMemoryClock = maxMemoryClock
        self.cores = cores
        self.logicalCores = logicalCores
        
        
    def getTDP(self) -> int:
        energyMultiplier = 0.05
        tdp = (self.clock * energyMultiplier)
        
        return int(tdp)
        
    def __str__(self):
        return f"{self.brand} {self.name} {self.cores}/{self.logicalCores} @ {(self.clock / 1000):.1f} Ghz"
        