
class Certificate:
    PLATINUM = 0
    GOLD = 1
    SILVER = 2
    BRONZE = 3
    BOMB = 4 
    
    def __str__(level: int) -> str:
        
        translations = {
            0: "Platinum",
            1: "Gold",
            2: "Silver",
            3: "Bronze",
            4: "Bomb"
        }
        
        return translations[level]