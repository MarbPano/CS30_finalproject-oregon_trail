import pygame
import time
import random
#----------------------#
#CS30_finalproject-main_body 
#Marb Pano
#Sedric Ascunsion
#December 4th
#----------------------#

def main():
    
        print(
    "The Oregon Trail")
        print('')

        menu = int(input((
    """You May:
            1. Travel the Trail
            2. Learn about the Trail
            3. End
    """)))
        
        
        if menu == 1:
            travel_the_trail()
        
        elif menu == 2:
            learn_about_the_trail()
        
        elif menu == 3:
            break#break to end to whole process 
            
        else:
            print("""
    Chose only the Numbers above
    """)
        
main()#main function will play



