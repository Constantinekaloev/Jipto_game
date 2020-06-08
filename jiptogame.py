import pygame
import time


TileWidth = 20                                #pixel sizes for grid squares
TileHeight = 20
TileMargin = 2

MapSizeRow = 25                               #how many tiles in either direction of grid
MapSizeColumn = 45
end_of_the_game = 0
pygame.init()                                

number_hero_points_0 = 0
number_hero_points_1 = 0
number_hero_points_2 = 0
number_hero_points_3 = 0
number_hero_points_4 = 0

first_round_points = 0
second_round_points = 0
winner = ""

BLACK = (0, 0, 0)                             
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE_GREEN = (0, 150, 150)
BlUE_WHITE = (215, 215, 255)
COLOR_FIRST_LINE = (100, 50, 100)
COLOR_SECOND_LINE = (50, 100, 100)
COLOR_THIRD_LINE =  (100, 100, 50)



Done = False                                  #track if window is open
clock = pygame.time.Clock()                   

Screen = pygame.display.set_mode([(TileWidth+TileMargin)*MapSizeColumn,
                                  (TileWidth+TileMargin+5)*MapSizeRow])  #making the window
                                  

        
class MapTile(object):                       
    def __init__(self, Name, Row, Column):
        self.Name = Name
        self.Column = Column
        self.Row = Row


class Character(object):                    
    def __init__(self, Name, HP, Row, Column, Type):
        self.Name = Name
        self.HP = HP
        self.Row = Row
        self.Column = Column
        self.Type = Type
        self.Points = 0
        self.First_Line = False
        self.Second_Line = False
        self.Third_Line = False
        
    
    def AddPoint(self):
        global number_hero_points_0
        global number_hero_points_1
        global number_hero_points_2
        global number_hero_points_3
        global number_hero_points_4
        if self.Name == "Hero0":
            number_hero_points_0 += 1
        elif self.Name == "Hero1":
            number_hero_points_1 += 1
        elif self.Name == "Hero2":
            number_hero_points_2 += 1
        elif self.Name == "Hero3":
            number_hero_points_3 += 1
        elif self.Name == "Hero4":
            number_hero_points_4 += 1
        
    def CheckLine(self, LineNumber):
        if LineNumber == 1:
            self.First_Line = True
        elif LineNumber == 2:
            self.Second_Line = True
        elif LineNumber == 3:
            self.Third_Line = True
            
    def Move(self, Direction):              

        if Direction == "UP":
            if self.Row > 0:                                 #If within boundaries of grid
                if self.CollisionCheck("UP") == False:       #And nothing in the way
                    self.Row -= 1                            #Go ahead and move
                   
        elif Direction == "LEFT":
            if self.Column > 0:
                if self.CollisionCheck("LEFT") == False:
                    self.Column -= 1
                    
        elif Direction == "RIGHT":
            if self.Column < MapSizeColumn-1:
                if self.CollisionCheck("RIGHT") == False:
                    self.Column += 1
                    
        elif Direction == "DOWN":
            if self.Row < MapSizeRow-1:
                if self.CollisionCheck("DOWN") == False:
                    self.Row += 1
                    
        Map.update()
                
    def DeleteEntity(self, array, del_object):
        for object in array:
            if object ==  del_object:
                array.remove(object)
    
    def CollisionCheck(self, Direction):       
        if Direction == "UP":
            if self.Type == 0:
                if len(Map.Grid[(self.Row)-1][self.Column][1]) > 0: #if villain ahead than delete hero
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[(self.Row)][self.Column][0][0])
                    del Map.Grid[(self.Row)][self.Column][0][0]
                    return True
                if len(Map.Grid[(self.Row)-1][self.Column][0]) > 0: #if hero ahead than block init hero
                    return True
            if self.Type == 1:
            
            
                if len(Map.Grid[(self.Row)-1][self.Column][0]) > 0: #if hero ahead than delete that hero 
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[(self.Row)-1][self.Column][0][0])
                    del Map.Grid[(self.Row)-1][self.Column][0][0]
                    return True
                if len(Map.Grid[(self.Row)-1][self.Column][1]) > 0: #if villain ahead than block init villain
                    return True    
                    
            if len(Map.Grid[(self.Row)-1][self.Column][2]) > 0:
                return True
                
                
        elif Direction == "LEFT":
            if self.Type == 0:
                if len(Map.Grid[self.Row][(self.Column)-1][1]) > 0: #if villain ahead than delete hero
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[self.Row][(self.Column)][0][0])
                    del Map.Grid[self.Row][(self.Column)][0][0]
                    return True                
                if len(Map.Grid[self.Row][(self.Column)-1][0]) > 0: #if hero ahead than block init hero
                    return True
            if self.Type == 1:
            
            
                if len(Map.Grid[self.Row][(self.Column)-1][0]) > 0: #if hero ahead than delete that hero 
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[self.Row][(self.Column)-1][0][0])
                    del Map.Grid[self.Row][(self.Column)-1][0][0]
                    return True
                if len(Map.Grid[self.Row][(self.Column)-1][1]) > 0: #if villain ahead than block init villain
                    return True    
        
            if len(Map.Grid[self.Row][(self.Column)-1][2]) > 0:
                return True
                
                
        elif Direction == "RIGHT":
            if self.Type == 0:
                if len(Map.Grid[self.Row][(self.Column)+1][1]) > 0: #if villain ahead than delete hero
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[self.Row][(self.Column)][0][0])
                    del Map.Grid[self.Row][(self.Column)][0][0]
                    return True
                if len(Map.Grid[self.Row][(self.Column)+1][0]) > 0: #if hero ahead than block init hero
                    return True
            if self.Type == 1:
            
            
                if len(Map.Grid[self.Row][(self.Column)+1][0]) > 0: #if hero ahead than delete that hero 
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[self.Row][(self.Column)+1][0][0])
                    del Map.Grid[self.Row][(self.Column)+1][0][0]
                    return True
                if len(Map.Grid[self.Row][(self.Column)+1][1]) > 0: #if villain ahead than block init villain
                    return True    
            
            if len(Map.Grid[self.Row][(self.Column)+1][2]) > 0:
                return True
                
                
        elif Direction == "DOWN":
            if self.Type == 0:
                if len(Map.Grid[(self.Row)+1][self.Column][1]) > 0: #if villain ahead than delete hero
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[(self.Row)][self.Column][0][0])
                    del Map.Grid[(self.Row)][self.Column][0][0]
                    return True
                if len(Map.Grid[(self.Row)+1][self.Column][0]) > 0: #if hero ahead than block init hero
                    return True
            if self.Type == 1:
            
            
                if len(Map.Grid[(self.Row)+1][self.Column][0]) > 0: #if hero ahead than delete that hero 
                    self.DeleteEntity(Map.array_of_heros, Map.Grid[(self.Row)+1][self.Column][0][0])
                    del Map.Grid[(self.Row)+1][self.Column][0][0]
                    return True
                if len(Map.Grid[(self.Row)+1][self.Column][1]) > 0: #if villain ahead than block init villain
                    return True    
            
            if len(Map.Grid[(self.Row)+1][self.Column][2]) > 0:
                return True
        return False

    def Location(self):
        print("Coordinates: " + str(self.Row) + ", " + str(self.Column))


class Map(object):              #The main class
    global MapSizeRow
    global MapSizeColumn
    
   
    array_of_heros = []
    array_of_villains = []
    array_of_buttons = []
    Grid = []
    

    for Row in range(MapSizeRow):     # Creating grid
        Grid.append([])
        for Column in range(MapSizeColumn):
            Grid[Row].append([])
            for i in range(3):
                Grid[Row][Column].append([])
            
    
    for Row in range(MapSizeRow):     
        for Column in range(MapSizeColumn):
            TempTile = MapTile("Rock", Row, Column)
            if Row == 0:
                Grid[int(Row)][int(Column)][2].append(TempTile)
            if Row == MapSizeRow-1:
                Grid[int(Row)][int(Column)][2].append(TempTile)
            if Column == 0:
                Grid[int(Row)][int(Column)][2].append(TempTile)
            if Column == MapSizeColumn-1:
                Grid[int(Row)][int(Column)][2].append(TempTile)
    
    
    for i in range(5):
       array_of_heros.append(Character("Hero" + str(i), 1, (i*4)+4, 35, 0))
    array_of_villains.append(Character("Villain0", 1, 4, 5, 1))
    array_of_villains.append(Character("Villain1", 1, 20, 5, 1))
    
    
    for Hero in array_of_heros:
        Grid[int(Hero.Row)][int(Hero.Column)][0].append(Hero)    
    for Villain in array_of_villains:
        Grid[int(Villain.Row)][int(Villain.Column)][1].append(Villain)
        
        
    def update(self):        
        for Row in range(MapSizeRow):      
            for Column in range(MapSizeColumn):
                for i in range(len(Map.Grid[Row][Column])):
                    for j in range(len(Map.Grid[Row][Column][i])):
                        for Hero in Map.array_of_heros:
                            if Map.Grid[Row][Column][i][j].Name == Hero.Name:
                                Map.Grid[Row][Column][i].remove(Map.Grid[Row][Column][i][j])
                                break
                        else:
                            continue
                        break
                    for j in range(len(Map.Grid[Row][Column][i])):    
                        for Villain in Map.array_of_villains:
                            if Map.Grid[Row][Column][i][j].Name == Villain.Name:
                                Map.Grid[Row][Column][i].remove(Map.Grid[Row][Column][i][j])
                                break
                        else:
                            continue
                        break
              
        for Hero in Map.array_of_heros:
            Map.Grid[int(Hero.Row)][int(Hero.Column)][0].append(Hero)       
        for Villain in Map.array_of_villains:
            Map.Grid[int(Villain.Row)][int(Villain.Column)][1].append(Villain)
        
        for Hero in Map.array_of_heros:
            if Hero.Column == 25 and Hero.First_Line == False:       #Первая лин
                Hero.AddPoint()
                Hero.CheckLine(1)
            elif Hero.Column == 20 and Hero.Second_Line == False:    #Вторая лин
                Hero.AddPoint()
                Hero.CheckLine(2)
            elif Hero.Column == 15 and Hero.Third_Line == False:     #Третья лин
                Hero.AddPoint()
                Hero.CheckLine(3)        
        
    
Map = Map()
iter_heros = 0
iter_villains = 0

global plus_on_iter_villains
plus_on_iter_villains = 0

rule_spawn = False

while not Done:    
    for event in pygame.event.get():         

        if event.type == pygame.QUIT:
            Done = True       

        elif event.type == pygame.MOUSEBUTTONDOWN:
            Pos = pygame.mouse.get_pos()
            
            if 400 + 100 > Pos[0] > 400 and 600 + 100 > Pos[1] > 600:
                if rule_spawn == False:
                    rule_spawn = True
                else:
                    rule_spawn = False
                    
            Column = Pos[0] // (TileHeight + TileMargin)  #Translating the position of the mouse into rows and columns
            Row = Pos[1] // (TileWidth + TileMargin)
            print(str(Row) + ", " + str(Column))

        elif not iter_heros < len(Map.array_of_heros) and not iter_villains < len(Map.array_of_villains) + 4:
            iter_heros = 0
            iter_villains = 0
            plus_on_iter_villains = 0
            
        elif iter_heros < len(Map.array_of_heros):
            if event.type == pygame.KEYDOWN:           
                if event.key == pygame.K_LEFT:
                    Map.array_of_heros[iter_heros].Move("LEFT")
                    iter_heros += 1    
                elif event.key == pygame.K_RIGHT:
                    Map.array_of_heros[iter_heros].Move("RIGHT")
                    iter_heros += 1    
                elif event.key == pygame.K_UP:
                    Map.array_of_heros[iter_heros].Move("UP")                                
                    iter_heros += 1
                elif event.key == pygame.K_DOWN:
                    Map.array_of_heros[iter_heros].Move("DOWN")
                    iter_heros += 1                
                    
        elif iter_villains < len(Map.array_of_villains) + 4:
            if iter_villains > 1 and iter_villains < 3:
                plus_on_iter_villains = -2
            elif iter_villains > 3:
                plus_on_iter_villains = -4
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Map.array_of_villains[iter_villains + plus_on_iter_villains].Move("LEFT")
                    iter_villains += 1    
                elif event.key == pygame.K_RIGHT:
                    Map.array_of_villains[iter_villains + plus_on_iter_villains].Move("RIGHT")
                    iter_villains += 1    
                elif event.key == pygame.K_UP:
                    Map.array_of_villains[iter_villains + plus_on_iter_villains].Move("UP")                                
                    iter_villains += 1
                elif event.key == pygame.K_DOWN:
                    Map.array_of_villains[iter_villains + plus_on_iter_villains].Move("DOWN")
                    iter_villains += 1
    
                
    Screen.fill(BLACK)
    ########################### -GUI
    font = pygame.font.Font(None, 32)
    text = font.render("1:" + str(number_hero_points_0) + ' 2:' + str(number_hero_points_1) + ' 3:' + str(number_hero_points_2) + ' 4:' + str(number_hero_points_3) + ' 5:' + str(number_hero_points_4), 1, WHITE)
    place = text.get_rect(center=(200,590))
    Screen.blit(text,place)
    ###########################
       
        
    for Row in range(MapSizeRow):           #Drawing grid
        
        for Column in range(MapSizeColumn):
            Color = WHITE
            if Column == 25:                #Первая лин
                Color = COLOR_FIRST_LINE
            if Column == 20:                #Вторая лин
                Color = COLOR_SECOND_LINE 
            if Column == 15:                #Третья лин
                Color = COLOR_THIRD_LINE    
            
            for i in range(0, len(Map.Grid[Row][Column])):
                for j in range(0, len(Map.Grid[Row][Column][i])):
                    if Map.Grid[Row][Column][i][j].Name == "Rock":
                        Color = BLUE_GREEN
                        
                    for Hero in Map.array_of_heros:
                        if Map.Grid[Row][Column][i][j].Name == Hero.Name:
                            Color = GREEN
                            
                    if Map.Grid[Row][Column][i][j].Name == "Villain0" or Map.Grid[Row][Column][i][j].Name == "Villain1":
                        Color = RED
                            
            for i in range(0, len(Map.Grid[Row][Column])):
                for j in range(0, len(Map.Grid[Row][Column][i])):
                    if iter_heros < len(Map.array_of_heros):
                        if Map.Grid[Row][Column][i][j].Name == Map.array_of_heros[iter_heros].Name:
                            Color = BLACK        
                    elif iter_villains < len(Map.array_of_villains) + 4:
                        if iter_villains > 1 and iter_villains < 3:
                            plus_on_iter_villains = -2
                        elif iter_villains > 3:
                            plus_on_iter_villains = -4
                           
                        if Map.Grid[Row][Column][i][j].Name == Map.array_of_villains[iter_villains + plus_on_iter_villains].Name:
                            Color = BLACK
                        
            
            pygame.draw.rect(Screen, Color, [(TileMargin + TileHeight) * Column + TileMargin,
                                             (TileMargin + TileWidth) * Row + TileMargin,
                                             TileWidth,
                                             TileHeight])
                                             
    ###############################################################-GUI
    def blit_text(surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  
        space = font.size(' ')[0]  
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0] 
                    y += word_height  
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  
            y += word_height  

            
    mouse = pygame.mouse.get_pos()
    if 400 + 100 > mouse[0] > 400 and 600 + 100 > mouse[1] > 600:
        pygame.draw.rect(Screen, BLUE_GREEN, (400, 600, 100, 100))
    else:
        pygame.draw.rect(Screen, RED, (400, 600, 100, 100))    
    text = font.render("Правила", 1, WHITE)
    place = text.get_rect(center=(400+(100/2), 600+(100/2)))
    Screen.blit(text,place)
    
    
    if rule_spawn == True:
        pygame.draw.rect(Screen, WHITE, (0, 0, 1000, 500))
        text ="""
         В игре 7 фигур: 
         5 - зеленых "убегающих", и 2 - красных "преследователей" 
         Игра состоит из 2 раундов.
         
         Цель игры: 
         Пять "убегающих" пытаются перейти на противоположную сторону прямоугольного игрового поля
         до поимки их "преследователем". Тот находится в начале игры в середине противоположной к "убегающим"
         стороне и стремится их поймать как можно дальше от своей стороны.
            
         Ход фигуры:
         Шаг индивидуальной фигуры осуществляется нажатием стрелок.
         У каждой фигуры зеленых в запасе один шаг.
         У каждой фигуры красных в запасе три  шага.
         Игроки делают ходы своими фигурами поочередно, причем первыми ходят "убегающие".
         
         Поимка:
         "Убегающий", которого коснулся "преследователь", считается пойманным и убирается с игрового поля.
        
         Оценка результата игры:
         Для оценки результата используются линии начерченные на игровом поле.
         Каждая линия имеет по одному очку, "убегающий" достигший одной из линий получает по одному баллу.
         В конце партии суммируются очки набранные "убегающими".
         После одной партии игроки меняются фигурами, начинается вторая партия игры.
         После игры очки сравниваются, у кого больше очков тот является победителем.


         """
        font_rule = pygame.font.Font(None, 22)
        blit_text(Screen, text, (0,0), font_rule)
    ##############################################################



    if not Map.array_of_heros:   #Конец раунда 
        if end_of_the_game == 0:
            first_round_points = (number_hero_points_0 +
                                number_hero_points_1 +
                                number_hero_points_2 +
                                number_hero_points_3 +
                                number_hero_points_4)
        else:
            second_round_points = (number_hero_points_0 +
                                number_hero_points_1 +
                                number_hero_points_2 +
                                number_hero_points_3 +
                                number_hero_points_4)
        
        for i in range(5): # - Респавн
            Map.array_of_heros.append(Character("Hero" + str(i), 1, (i*4)+4, 35, 0))
        del Map.array_of_villains[0]
        del Map.array_of_villains[0]
        Map.array_of_villains.append(Character("Villain0", 1, 4, 5, 1))
        Map.array_of_villains.append(Character("Villain1", 1, 20, 5, 1))
        end_of_the_game += 1
        iter_heros -= 1
        number_hero_points_0 = 0
        number_hero_points_1 = 0
        number_hero_points_2 = 0
        number_hero_points_3 = 0
        number_hero_points_4 = 0  
        
        
    
    if end_of_the_game == 2: #два раунда - выход из игры
        ########################### -GUI
        text = font.render(str(first_round_points) + "- Первый раунд " + str(second_round_points) + "-Второй раунд ", 1, WHITE)
        if first_round_points > second_round_points:
            text_result = font.render("Победитель: " + str("1 игрок") , 1, WHITE)
        elif first_round_points < second_round_points:
            text_result = font.render("Победитель: " + str("2 игрок") , 1, WHITE)
        else:
            text_result = font.render("Победитель: " + str("Ничья") , 1, WHITE)
        place = text.get_rect(center=(600,590))
        place_result = text_result.get_rect(center=(600, 610))
        Screen.blit(text, place)
        Screen.blit(text_result, place_result)
        ###########################
        
        
        Done = True
        
    
    clock.tick(60)      
    
    pygame.display.flip()     
    
    Map.update()
    
   


time.sleep(5)
pygame.quit()
