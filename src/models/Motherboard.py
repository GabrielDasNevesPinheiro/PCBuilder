from .Component import Component
from .Processor import Processor
from .enum.HardwareStatus import HardwareStatus
from .enum.Certificate import Certificate
from .GPU import GPU
from .RAM import RAM
from .Font import Font

class Motherboard(Component):
    
    def __init__(self, name: str, brand: str, socket: str, ramSlots: int, processor: Processor = None, gpu: GPU = None, font: Font = None, ram: list[RAM] = None):
        super().__init__(name, brand)
        self.socket = socket
        
        #init attr
        self.ram = [None for x in range(0, ramSlots)]
        self.gpu = None
        self.processor = None
        self.font = None
        
        self.attach(gpu)
        self.attach(processor)
        self.attach(font)
        self.attach(ram)
    
    def getTDP(self) -> int:
        tdp = 0
        
        if self.gpu:
            tdp += self.gpu.getTDP()
        
        if self.processor:
            tdp += self.processor.getTDP()
        
        if self.ram[0]:
             for ram in self.ram:
                if ram:
                    tdp += ram.getTDP()
        
        return tdp
        
    def attach(self, component: Processor | list[RAM] | GPU | Font) -> bool:
        
        if component is None:
            return False
        
        if isinstance(component, Processor):
            if self.socket == component.socket:
                self.processor = component
                return True
            
            return False
        
        
        if isinstance(component, list):
            for ram,index in zip(self.ram, range(len(component))):
                if ram == None:
                    
                    if self.processor:
                        component[index].clock = self.processor.maxMemoryClock if self.processor.maxMemoryClock <= component[index].maxClock else component[index].maxClock 
                    
                    self.ram[index] = component[index]
            
            return True
            
        if isinstance(component, Font):
            self.font = component
            return True
        
        if isinstance(component, GPU):
            self.gpu = component
            return True
    
    
    def turnOn(self) -> int:
        if not self.processor:
            self.status = HardwareStatus.OFF
            return self.status
        
        if not self.font:
            self.status = HardwareStatus.OFF
            return self.status
        
        if not self.ram[0]:
            self.status = HardwareStatus.NO_VIDEO
            return self.status
        
        if not self.gpu:
            self.status = HardwareStatus.NO_VIDEO
            return self.status
        
        if self.font.power < self.getTDP() and self.font.certificate > Certificate.BRONZE:
            self.font.status = HardwareStatus.BURNING
            return HardwareStatus.BURNING
        
        if self.font.power < self.getTDP() and self.font.certificate <= Certificate.BRONZE:
            return HardwareStatus.OFF
        
        if self.font.power >= 600 and self.font.certificate == Certificate.BOMB:
            self.processor.status =  HardwareStatus.MELTED
            self.font.status = HardwareStatus.BURNING
            self.gpu.status = HardwareStatus.BURNING
            self.status = HardwareStatus.BURNING
            return self.status
        
        self.status = HardwareStatus.WORKING
        self.processor.status = HardwareStatus.WORKING
        self.font.status = HardwareStatus.WORKING
        self.gpu.status = HardwareStatus.WORKING
        return self.status
    
    def __str__(self):
        
        
        
        return f'''
    {self.brand} {self.name} {self.socket} Platform
    Processor: {str(self.processor)}
    Ram ({len(self.ram)} slots): {[f"{str(ram)}" for ram in self.ram]}
    GPU: {str(self.gpu)}
    Power Supply: {str(self.font)}
    System TDP: {self.getTDP()}W
    System Status: {HardwareStatus.__str__(self.status)}
    '''