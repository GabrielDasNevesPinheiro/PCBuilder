# O projeto PCBuilder
<p style="font-size: 2rem">Um sistema de montagem de computador onde teremos as peças principais:</p> 

* <p style="font-size: 1.2rem">Processador</p>
* <p style="font-size: 1.2rem">Placa mãe</p>
* <p style="font-size: 1.2rem">Memória</p>
* <p style="font-size: 1.2rem">Fonte</p>
* <p style="font-size: 1.2rem">Placa de vídeo</p>

# Sobre o projeto
<p>A Lógica do código, de uma forma básica, simula o funcionamento real de um sistema de hardware.</p>
<p>Cada classe foi pensada cuidadosamente enquanto eu estava sem internet e ouvia nirvana.</p>
<p>Sem mais delongas, abaixo está o que surgiu nas minhas ideias.</p>


## Classes and Objects

### Certificate
* `PLATINUM`
* `GOLD`
* `SILVER`
* `BRONZE`
* `BOMB`

### HardwareStatus
* `OFF`
* `WORKING`
* `BURNING`
* `MELTED`
* `NO_VIDEO`

### Component
* `status` -> `HardwareStatus`
* `name` -> `str`
* `brand` -> `str`

### Font < Component
* `power` -> `int`
* `certificate` -> `Certificate`

### Processor < Component
* `socket` -> `str`
* `clock` -> `int`
* `maxMemoryClock` -> `int`
* `cores` -> `int`
* `logicalCores` -> `int`
* `getTDP()` -> `int`

### RAM < Component
* `size` -> `int` < MB size, like 8192
* `clock` -> `int`
* `maxClock` -> `int`
* `getTDP()` -> `int`

### GPU < Component
* `coreClock` -> `int`
* `memoryClock` -> `int`
* `vram` -> `int` < MB size, like 4096
* `getTDP()` -> `int`

### Motherboard < Component
* `socket` -> `str`
* `processor` -> `Processor | None`
* `ramSlots` -> `int`
* `ram` -> `list[RAM | None]` < ram max lengh = ramSlots
* `gpu` -> `GPU`
* `getTDP()` -> `int`
* `attach(component)` -> `bool` < Can have overload
* `turnOn()` -> `void` < check status property on components.
* `__str__` -> `str` < Overwrite 
