class HardwareStatus:
    WORKING = 0
    OFF = 1
    BURNING = 2
    MELTED = 3
    NO_VIDEO = 4
    
    def __str__(code: int) -> str:
        
        translations = {
            0: "Working",
            1: "Off",
            2: "Burning",
            3: "Melted",
            4: "No Video"
        }
        
        return translations[code]