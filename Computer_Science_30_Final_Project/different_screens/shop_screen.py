import pygame
import sys
from os import path
import window_creation as wc
import classes_player as cp
#change the value of money, by character
#self.inventory is the same for everything - remain the same


class Shop:
    def __init__(self, player):
        self.money = 2000
        self.self.inventory = {
            "Pounds of Food": 0,
            "Spare Parts": 0,
            "Bullets": 0,
            "Horses": 0,
            "Clothing": 0,
        }
        self.player = player

    def draw_text(self, screen,text, x, y, size):
        font = pygame.font.SysFont('Corbel', size)
        #render box_text
        box_text = font.render(text, True, (255, 255, 255))
        screen.blit(box_text, (x,y))#x and y is coordinate where text should be
    

    def shop(self, screen, width, height, money):
    
        #getting the value of all the keys in the dict
        food_amount = self.inventory["Pounds of Food"]
        spare_parts_amount = self.inventory["Spare Parts"]
        bullets_amount = self.inventory["Bullets"]
        horses_amount = self.inventory["Horses"]
        clothing_amount = self.inventory["Clothing"]
        #price of things
        food_price = 5
        spare_parts_price = 30
        bullets_price = 2
        horses_price = 200
        clothing_price = 20
    
    
        img_dir = path.join(path.dirname(__file__), "images")
        shop_background = pygame.image.load(path.join(img_dir, "Store-f.png"))
    
        # define line
        line_width = 6
        line_colour = (165, 42, 42)

        # define lines
        line1 = wc.Line(1, height - 705, width, height - 705, line_width, line_colour, screen)
        line2 = wc.Line(1, height - 650, width, height - 650, line_width, line_colour, screen)
    

        # define font
        font = pygame.font.SysFont('Corbel', 40, bold=True)

        # render text
        shop_title = font.render("Dauvin's Country Development", True, (255, 140, 00))

        # rectangle coordinates
        rect_width = (width // 2) *1.5
        rect_height = ((height // 2) * 1.35) - 50
        rect_x = (width - rect_width) // 2
        rect_y = ((height - rect_height) // 2) - 35
    
    
        #mouse
        pos = pygame.mouse.get_pos()
        while True:
            #fill background
            screen.blit((shop_background), (0,0))
        
            #draw the text for the money
            text_money = str(money)
            draw_text(screen,f"${text_money}", 570, 120, 50)
        
            #draw text for the amount of each
            text_amount_food = str(food_amount)
            text_amount_spare_parts = str(spare_parts_amount)
            text_amount_bullets = str(bullets_amount)
            text_amount_horses = str(horses_amount)
            text_amount_clothing = str(clothing_amount)
        
            draw_text(screen,text_amount_food,508,195,50)
            draw_text(screen,text_amount_spare_parts,508,260,50)
            draw_text(screen,text_amount_bullets,508,325,50)
            draw_text(screen,text_amount_horses,508,390,50)
            draw_text(screen,text_amount_clothing,508,455,50)

            # draw line
            #pygame.draw.line(screen, line_colour, (x1, y1), (x2, y2), line_width)
            line1.draw(screen)
            line2.draw(screen)

            # draw title text
            title_text_rect = shop_title.get_rect(center=(width/2, height/3 - 195))
            screen.blit(shop_title, title_text_rect.topleft)
        
            #drawing un_pressable text
            draw_text(screen,"Things you Need:",30,150,55)
        
            draw_text(screen,"5 Pounds of Food",50,200,50)#5 pounds of food feeds family for 2 days, 3 miles travelled in 1 day, 2 000 miles. Need 270 pounds of food, which a buck a pound
            draw_text(screen,"1 Pack Spare Parts",50,265,50)
            draw_text(screen,"10 Bullets",50,330,50)
            draw_text(screen,"1 Horses",50,385,50)
            draw_text(screen,"2 Clothing",50,450,50)

        

            #creating the button----
                #border
            button_border = (150, 75, 0)
            button_color = (101, 67, 33)
                #Actual buttons - food
            food_button_plus = wc.Button(430, 190, 40, 40, button_border, button_color, screen)#x is same y change
            food_button_plus_rect = food_button_plus.rect
        
            food_button_minus = wc.Button(580, 190, 40, 40, button_border, button_color, screen)
            food_button_minus_rect = food_button_minus.rect
            
                #actual buttons - spare parts
            spare_parts_button_plus = wc.Button(430, 255, 40, 40, button_border, button_color, screen)#x is same y change
            spare_parts_button_plus_rect = spare_parts_button_plus.rect
        
            spare_parts_button_minus = wc.Button(580, 255, 40, 40, button_border, button_color, screen)
            spare_parts_button_minus_rect = spare_parts_button_minus.rect
            
                #actual buttons - bullets
            bullets_button_plus = wc.Button(430, 320, 40, 40, button_border, button_color, screen)#x is same y change
            bullets_button_plus_rect = bullets_button_plus.rect
        
            bullets_button_minus = wc.Button(580, 320, 40, 40, button_border, button_color, screen)
            bullets_button_minus_rect = bullets_button_minus.rect
            
            #actual buttons - horses
            horses_button_plus = wc.Button(430, 385, 40, 40, button_border, button_color, screen)#x is same y change
            horses_button_plus_rect = horses_button_plus.rect
        
            horses_button_minus = wc.Button(580, 385, 40, 40, button_border, button_color, screen)
            horses_button_minus_rect = horses_button_minus.rect
        
                #actual buttons - clothing
            clothing_button_plus = wc.Button(430, 450, 40, 40, button_border, button_color, screen)#x is same y change
            clothing_button_plus_rect = clothing_button_plus.rect
        
            clothing_button_minus = wc.Button(580, 450, 40, 40, button_border, button_color, screen)
            clothing_button_minus_rect = clothing_button_minus.rect
        
    ######-----------#######
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
        
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        #food
                        if food_button_plus_rect.collidepoint(event.pos):
                            if money < food_price:
                                None
                            
                            else:
                                #remove money and add into self.inventory
                                money -= food_price
                                food_amount += 5
                                self.inventory["Pounds of Food"] = food_amount
                            
                                print(self.inventory)
                                print(money)

                            
                        elif food_button_minus_rect.collidepoint(event.pos):
                            if food_amount == 0:
                                None
                            
                            else:
                                money += food_price
                                food_amount -= 5
                                self.inventory["Pounds of Food"] = food_amount
                            
                                print(self.inventory)
                                print(money)
                        #spare parts    
                        elif spare_parts_button_plus_rect.collidepoint(event.pos):
                            if money < spare_parts_price:
                                None
                            
                            else:
                                #remove money and add into self.inventory
                                money -= spare_parts_price
                                spare_parts_amount += 1
                                self.inventory["Spare Parts"] = spare_parts_amount
                            
                                print(self.inventory)
                                print(money)

                            
                        elif spare_parts_button_minus_rect.collidepoint(event.pos):
                            if spare_parts_amount == 0:
                                None
                            
                            else:
                                money += spare_parts_price
                                spare_parts_amount -= 1
                                self.inventory["Spare Parts"] = spare_parts_amount
                            
                                print(self.inventory)
                                print(money)
                            
                        #bullets
                        elif bullets_button_plus_rect.collidepoint(event.pos):
                            if money < bullets_price:
                                None
                        
                            else:
                                #remove money and add into self.inventory
                                money -= bullets_price
                                bullets_amount += 10
                                self.inventory["Bullets"] = bullets_amount
                            
                                print(self.inventory)
                                print(money)

                            
                        elif bullets_button_minus_rect.collidepoint(event.pos):
                            if bullets_amount == 0:
                                None
                            
                            else:
                                money += bullets_price
                                bullets_amount -= 10
                                self.inventory["Bullets"] = bullets_amount
                            
                                print(self.inventory)
                                print(money)
                            
                        #horses
                        elif horses_button_plus_rect.collidepoint(event.pos):
                            if money < horses_price:
                                None
                        
                            else:
                                #remove money and add into self.inventory
                                money -= horses_price
                                horses_amount += 1
                                self.inventory["Horses"] = horses_amount
                            
                                print(self.inventory)
                                print(money)

                            
                        elif horses_button_minus_rect.collidepoint(event.pos):
                            if horses_amount == 0:
                                None
                            
                            else:
                                money += horses_price
                                horses_amount -= 1
                                self.inventory["Horses"] = horses_amount
                            
                                print(self.inventory)
                                print(money)
                            
                        #clothing
                        elif clothing_button_plus_rect.collidepoint(event.pos):
                            if money < clothing_price:
                                None
                        
                            else:
                                #remove money and add into self.inventory
                                money -= clothing_price
                                clothing_amount += 2
                                self.inventory["Clothing"] = clothing_amount
                            
                                print(self.inventory)
                                print(money)

                            
                        elif clothing_button_minus_rect.collidepoint(event.pos):
                            if clothing_amount == 0:
                                None
                            
                            else:
                                money += clothing_price
                                clothing_amount -= 2
                                self.inventory["Clothing"] = clothing_amount
                            
                                print(self.inventory)
                                print(money)
                            
                            
        
        
        
            #drawing it out - food
            food_button_plus.draw(screen)
            food_button_plus.with_text('+','Corbel', 50, (255, 255, 255), screen, bold=True)
            food_button_plus.update()
        
            food_button_minus.draw(screen)
            food_button_minus.with_text('-','Corbel', 50, (255, 255, 255), screen, bold=True)
            food_button_minus.update()
        
            #drawing it out - spare parts
            spare_parts_button_plus.draw(screen)
            spare_parts_button_plus.with_text('+','Corbel', 50, (255, 255, 255), screen, bold=True)
            spare_parts_button_plus.update()
        
            spare_parts_button_minus.draw(screen)
            spare_parts_button_minus.with_text('-','Corbel', 50, (255, 255, 255), screen, bold=True)
            spare_parts_button_minus.update()
        
            #drawing it out - bullets
            bullets_button_plus.draw(screen)
            bullets_button_plus.with_text('+','Corbel', 50, (255, 255, 255), screen, bold=True)
            bullets_button_plus.update()
        
            bullets_button_minus.draw(screen)
            bullets_button_minus.with_text('-','Corbel', 50, (255, 255, 255), screen, bold=True)
            bullets_button_minus.update()
        
            #drawing it out - horses
            horses_button_plus.draw(screen)
            horses_button_plus.with_text('+','Corbel', 50, (255, 255, 255), screen, bold=True)
            horses_button_plus.update()
        
            horses_button_minus.draw(screen)
            horses_button_minus.with_text('-','Corbel', 50, (255, 255, 255), screen, bold=True)
            horses_button_minus.update()
        
            #drawing it out - clothing
            clothing_button_plus.draw(screen)
            clothing_button_plus.with_text('+','Corbel', 50, (255, 255, 255), screen, bold=True)
            clothing_button_plus.update()
        
            clothing_button_minus.draw(screen)
            clothing_button_minus.with_text('-','Corbel', 50, (255, 255, 255), screen, bold=True)
            clothing_button_minus.update()
        
            pygame.display.update()
                             
#screen = pygame.display.set_mode(size=(720, 720))
#width = screen.get_width()
#height = screen.get_height()
#shop(screen, width, height, money)
#recent marker###_--####
#recent marker$$$$$$$