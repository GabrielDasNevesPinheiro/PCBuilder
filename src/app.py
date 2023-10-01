from models.hardware import *

# teste de hardware, provavelmente vai explodir

cpu = Processor(
    name="Xeon E5-2620 v3",
    brand="Intel",
    socket="2066 LGA",
    clock=3192,
    maxMemoryClock=1866,
    cores=6,
    logicalCores=12   
)

ram = RAM(
    name="Furry", 
    brand="HyperX", 
    size=8192, 
    clock=3200, 
    maxClock=3200
)

font = Font(
    name="Energy", 
    brand="Robots", 
    power=950, 
    certificate=Certificate.BOMB
)

gpu = GPU(
    name="RX 580", 
    brand="AMD", 
    coreClock=1266, 
    memoryClock=1750, 
    vram=8196
)

mother = Motherboard(
    name="X99H", 
    brand="Atermiter", 
    socket="2066 LGA", 
    ramSlots=2, 
    gpu=gpu, 
    processor=cpu,
    font=font,
    ram=[ram, ram])

print("System is", HardwareStatus.__str__(mother.turnOn()))

print(str(mother))
