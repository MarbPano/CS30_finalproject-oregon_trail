class player():
    def __init__(self, money, bullet, sell_item, buy_item, name, char_job):
        self.money = 0
        self.bullet = 0
        self.bonus = 0
        self.sell_item ={}#name of item and the value
        self.buy_item = {}#buy and selling
        self.name = name
        self.bonus = None
        self.char_job = char_job
        
        if char_job == "Voyaguer":
            self.money = 2000
            self.bonus = 1.5
            
        elif char_job = "Hunter":
            self.money = 1500
            self.bonus = 1.25
        
        elif char_job = "Farmer":
            self.money = 1000
            self.bonus = 1.0
            

        

        
        

        