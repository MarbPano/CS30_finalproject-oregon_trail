import pygame
import time


class Player():
    def __init__(self, name, char_job):
        self.money = 0
        self.name = name
        self.char_job = char_job
        self.inventory = {"Pounds of Food": 0,
             "Spare Parts": 0,
             "Bullets": 0,
             "Horses": 0,
             "Clothing": 0,
             }
        
        
        
        if char_job == "Voyaguer":
            self.money = 2000
            self.bonus = 1.5
            
        elif char_job == "Hunter":
            self.money = 1500
            self.bonus = 1.25
        
        elif char_job == "Farmer":
            self.money = 1000
            self.bonus = 1.0
    
   
        
          
                  
    
player = Player("Player", "Hunter")#for the shop screen to work






