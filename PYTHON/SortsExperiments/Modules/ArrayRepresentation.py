# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 07:45:20 2020
@author:HTS
"""

import tkinter as tk


class Arrayrepresentation(tk.Canvas):
    
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="ivory2")
        self.pack(fill=tk.BOTH, expand=1, padx=9, pady=5)
        
        
    def addComponents(self, inputarray):
       
        self.pack(fill=tk.BOTH, expand=0, padx=9, pady=5)
        self.vbar=tk.Scrollbar(self,orient=tk.VERTICAL)
        self.vbar.pack(side=tk.RIGHT,fill=tk.Y)
        self.vbar.config(command=self.yview)
        self.config(yscrollcommand=self.vbar.set)  
        self.hbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.hbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.hbar.config(command=self.xview)
        self.config(xscrollcommand=self.hbar.set)  
        self.colors =["gray89", "gray64", "black"]
        
        
        START_POINT_X_INITIAL = 5
        START_POINT_X = START_POINT_X_INITIAL    
        START_POINT_Y_INITIAL = 5         
        START_POINT_Y = START_POINT_Y_INITIAL
        COUNT_ROW = 0
        width_rectangle =20
        height_rectangle =20        
        count = 1
        ROW_SPACE = 12
        COL_SPACE = 3      
        for number in inputarray:
           
            if number >=0 :
                self.create_rectangle(START_POINT_X, START_POINT_Y,START_POINT_X+width_rectangle, START_POINT_Y+height_rectangle, fill=self.colors[0])
                self.create_text(START_POINT_X+width_rectangle/2, START_POINT_Y+height_rectangle/2, text=str(number),font=("Arial 7 bold"), fill=self.colors[2])
                START_POINT_X =START_POINT_X+width_rectangle+ROW_SPACE
            else:
                self.create_rectangle(START_POINT_X, START_POINT_Y,START_POINT_X+width_rectangle, START_POINT_Y+height_rectangle, fill=self.colors[1])
                self.canvasArray.create_text(START_POINT_X, START_POINT_Y, text=str(number),fill="gray64")
                START_POINT_X += ROW_SPACE       
            count+=1
            
            if count == 10:
                COUNT_ROW+= 1
                START_POINT_X = START_POINT_X_INITIAL
                START_POINT_Y =START_POINT_Y_INITIAL + COUNT_ROW *(COL_SPACE+height_rectangle)
                count = 0
        self.update()