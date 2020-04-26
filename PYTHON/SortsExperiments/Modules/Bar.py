# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 07:45:20 2020
@author:HTS
"""

from Start.setup_mod import COLORS
from Start.setup_mod import BAR_MIN__Y_PIXEL



previous_x1,previous_y1, previous_x2, previous_y2 = 0,0,0,0
count = 0


class Bar():

    def __init__(self, _x1, _y1, _x2, _y2, data, color=COLORS[0]):
        self.x1 = _x1
        self.y1 = _y1
        self.x2 = _x2
        self.y2 = _y2
        self.data = data
        self.color = color       
        
    def setAttributes(self, x1 =None,y1 =None, x2=None, y2 =None, data=None):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.data = data
        
    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color
        
    def createBars_scaled(width, height, inputarray):
        listBars = []        
        START_POINT_X = 15
        count = 0
        width_bar = 6
        space_between_bars = 6
        Y_MIN_LIMIT = 2
        Y_MAX_LIMIT = height-2
        
        for count, number in enumerate(inputarray, start=0):
            if count == 0:                
                if number > 0:
                    A =   int(height/2) - 2*number-0.8*number  #  (int(height/2) - (number/N * height_item))
                    START_POINT_Y = A if A > Y_MIN_LIMIT-1 else Y_MIN_LIMIT
                    y2 = int(height/2)
                    b = Bar(START_POINT_X, START_POINT_Y,START_POINT_X + width_bar,y2,number)
                    previous_x2 = START_POINT_X + width_bar
    
                elif number < 0:
                    START_POINT_Y = int (height/2)
                    A =  START_POINT_Y + 2*abs(number)+0.8*abs(number)     #START_POINT_Y + (abs(number) * height_item)
                    y2 = A if A < Y_MAX_LIMIT + 1 else Y_MAX_LIMIT
                    b = Bar(START_POINT_X, START_POINT_Y,START_POINT_X + width_bar,y2,number)
                    previous_x2 = START_POINT_X + width_bar
    
                else:
                    START_POINT_Y = int(height/2)
                    b = Bar(START_POINT_X, START_POINT_Y,START_POINT_X + width_bar,START_POINT_Y,number)
                    previous_x2 = START_POINT_X + width_bar
                    
            else:
                if number > 0:
                    START_POINT_X = previous_x2 + space_between_bars
                    A =  int(height/2) - 2*number-0.8*number  # (int (height/2) - (number /N * height_item))
                    START_POINT_Y = A if A > Y_MIN_LIMIT-1 else Y_MIN_LIMIT
                    y2 = int(height/2) 
                    b = Bar(START_POINT_X, START_POINT_Y,START_POINT_X + width_bar,y2,number)
                    previous_x2 = START_POINT_X + width_bar
    
                elif number < 0:
                    START_POINT_X = previous_x2 + space_between_bars
                    START_POINT_Y = (int (height/2))
                    A = int (height/2) + 2*abs(number)+0.8*abs(number)      #(int(height/2) + (abs(number) * height_item))
                    y2 =  A if A < Y_MAX_LIMIT+1 else Y_MAX_LIMIT 
                    b = Bar(START_POINT_X, START_POINT_Y,START_POINT_X + width_bar,y2,number)
                    previous_x2 = START_POINT_X + width_bar
                    
                else:
                    START_POINT_X = previous_x2 + space_between_bars
                    START_POINT_Y = int(height/2)
                    y2 = START_POINT_Y
                    b = Bar(START_POINT_X, START_POINT_Y,START_POINT_X + width_bar,START_POINT_Y,number)
                    previous_x2 = START_POINT_X + width_bar                    
                    b = Bar(START_POINT_X, START_POINT_Y,START_POINT_X + width_bar,y2,number)                    
            listBars.append(b)
        return listBars
            
            
    def createBars(width, height, number):
        global previous_x2, previous_y1, previous_y2, count
        START_POINT_X = 10
        START_POINT_Y = 0
        x2,y2 =0,0        
        w_item = 6 
        if count == 0:
            if number >=0:
                B = int(height/2  -  number%(height))
                START_POINT_Y  = B if B >= 0 else BAR_MIN__Y_PIXEL
                x2 = START_POINT_X + w_item
                y2 = height/2
                count += 1
            
            elif number < 0:
                START_POINT_Y = int(height/2)
                x2 = START_POINT_X + w_item
                A = START_POINT_Y + int(abs(number)%(height))
                y2 = A if A < height else height-2
                b = Bar(START_POINT_X, START_POINT_Y,x2,y2, number)
                count += 1           
            
        else:
            if number < 0:

                if previous_y2 == int(height/2):
                    START_POINT_X = previous_x2 + w_item
                    START_POINT_Y = previous_y2
                    x2 = START_POINT_X + w_item
                    A = START_POINT_Y + int(abs(number)%(height))
                    y2 = A if A  < height else height-2   
                   
                elif previous_y2 > height/2:
                    START_POINT_X = previous_x2+w_item
                    START_POINT_Y = previous_y1
                    x2 = START_POINT_X + w_item
                    A = previous_y1 +  int(abs(number)%(height))
                    y2 = A if A  < height else height-2 
                    
            elif number > 0:
                    if previous_y2 == int(height/2):
                        START_POINT_X = previous_x2 + w_item
                        B = previous_y2 - int(abs(number)%(height))
                        START_POINT_Y = B if B >=0 else BAR_MIN__Y_PIXEL   
                        x2 = START_POINT_X + w_item
                        y2 = previous_y2
                        
                    elif previous_y2 > int(height/2):
                        START_POINT_X = previous_x2 + w_item
                        B = previous_y1 - int(abs(number)%(height))
                        START_POINT_Y = B if B >=0 else  BAR_MIN__Y_PIXEL 
                        x2 = START_POINT_X + w_item
                        y2 = previous_y1
            else:
                START_POINT_Y=int(height/2)
                x2 = START_POINT_X + w_item
                y2 = previous_y1     
        
        b = Bar(START_POINT_X, START_POINT_Y,x2,y2,number)
        previous_y1, previous_x2, previous_y2 = START_POINT_Y,x2, y2     
        return b