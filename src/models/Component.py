from .enum.HardwareStatus import HardwareStatus


class Component:
    
    def __init__(self, name: str, brand: str):
        self.status = HardwareStatus.OFF
        self.name = name
        self.brand = brand