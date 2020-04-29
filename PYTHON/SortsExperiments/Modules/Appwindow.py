# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 07:45:20 2020
@author:HTS
"""

import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
import time as ti
import sys as s
import copy as cp
import threading as thd
from Start.setup_mod import COLORS
from Start.setup_mod import ALGORITHMS
from Start.setup_mod import LAST_PIXEL
from Start.setup_mod import FIRST_PIXEL
from Start.setup_mod import ROW_SPACE_DISPLAY_ARRAY
from Start.setup_mod import COL_SPACE_DISPLAY_ARRAY
import Modules.Sortinglibrary as std
import Modules.Bar as Bar



class Appwindow(tk.Tk):
    
    def __init__(self,titre, width, height):
        print("Setting up the application window")
        super().__init__()
        self.numbers = 0 
        self.tags= []
        self.listBars =[]
        self.rectangles = []
        self.createcomponents(titre, width, height)
               
        
    def deleteRectangle(self, i):
        self.canvas.delete(self.rectangles[i])
        self.canvas.delete(self.tags[i])
        
        
    def setAttributes(self, aux_bars, k, i):
        self.listBars[i].setAttributes(aux_bars[k].x1, aux_bars[k].y1, aux_bars[k].x2, aux_bars[k].y2, aux_bars[k].data)
        
    def swapNumber(self, i, j):  
        if i != j :
            temp1_bar = cp.deepcopy(self.listBars[i])
            temp2_bar = cp.deepcopy(self.listBars[j])              
            self.deleteRectangle(i)        
            self.deleteRectangle(j)
            self.tags[i] = None        
            self.tags[j] = None        
            self.listBars[i].setAttributes(temp1_bar.x1, temp2_bar.y1, temp1_bar.x2, temp2_bar.y2, temp2_bar.data)
            self.listBars[j].setAttributes(temp2_bar.x1, temp1_bar.y1, temp2_bar.x2, temp1_bar.y2, temp1_bar.data)
            self.listBars[i].setColor(temp2_bar.getColor())
            self.listBars[j].setColor(temp1_bar.getColor())
            color_i = self.listBars[i].getColor()
            color_j = self.listBars[j].getColor()          
            self.rectangles[j] = self.createRectanglefrombar(self.listBars[j], color_j,j)
            self.rectangles[i] = self.createRectanglefrombar(self.listBars[i], color_i,i)
             
            
      
        
    def setColor(self,i,color):
        self.canvas.itemconfig(self.rectangles[i], fill = COLORS[color])
        
        

    def createRectanglefrombar(self, mybar, color=None,i=None):
        color = mybar.color
        if color is None:
            color = COLORS[0]        
       
        if mybar.data == 0 :
            r = self.canvas.create_line(mybar.x1, mybar.y1, mybar.x2, mybar.y2, width=3, fill=color, tag=str(mybar.y2))
            handle_tag=self.canvas.create_text(mybar.x1+1, mybar.y1-2 ,font=("Arial",9, 'bold'),text=str(mybar.data), anchor="w", angle=90,  fill=COLORS[1], justify="center",tags=(str(mybar.x1),))        
        else:
            if mybar.data > 0 :
                r= self.canvas.create_rectangle(mybar.x1, mybar.y1, mybar.x2, mybar.y2,fill=color,tag=str(mybar.y2)) 
                handle_tag =self.canvas.create_text(mybar.x1+3, mybar.y2-10 ,font=("Arial",9, 'bold'),text=str(mybar.data), anchor="w", angle=90,  fill=COLORS[1], justify="center", tags=(str(mybar.x1),))
            else:
                r= self.canvas.create_rectangle(mybar.x1, mybar.y1, mybar.x2, mybar.y2,fill=color ,tag=str(mybar.y2)) 
                handle_tag = self.canvas.create_text(mybar.x1+3, mybar.y1+30 ,font=("Arial",9, 'bold'),text=str(mybar.data), anchor="w", angle=90,  fill=COLORS[1], justify="center", tags=(str(mybar.x1),))                
        
        if i < len(self.tags):
            self.tags[i] = handle_tag
        else:
            self.tags.append(handle_tag)
        return r

      
    def validateArraySize(self):
        maxNumber = s.maxsize
        _value = int(self.size_Entry.get())
        _min = int(self.min_Entry.get())
        _max = int(self.max_Entry.get())
        check_values = (_min >= -maxNumber and _min <= maxNumber) and _max>=-maxNumber and _max <= maxNumber and _value > 0 and _value< maxNumber
        try:
            if check_values:
                return _value             
        except TypeError:
            return None
        
    
    def launch(self):
        self.tags.clear()
        self.canvas.delete("all")
        self.arrayCanvas.delete("all")       
        check_size = self.validateArraySize()
        if check_size == None:
            msg.showerror("Input error", "Please enter an integer for min, max and array size!")
            return None        
        self.numbers = check_size
        self.algorithm = str(self.algo_ComboList.get())        
        if self.algorithm == "Insertion"or self.algorithm == "Insertionimproved":
            self.arguments = range(1, self.numbers)
        else:
            self.arguments = range(0, self.numbers)
        self.inputarray = std.generateRandomArray(self.numbers, int(self.min_Entry.get()), int(self.max_Entry.get()))                
        self.listBars = Bar.Bar.createBars_scaled(self.width, self.height, self.inputarray)  
        self.canvas.create_line(0,self.height/2,LAST_PIXEL,self.height/2, fill=COLORS[1] ,dash=(4,1), width=2)
        self.addComponents(self.inputarray)       
        self.rectangles = [self.createRectanglefrombar(rect,None,i) for i,rect in enumerate(self.listBars, start=0)]        
 
   
 
        # # thread_swap = thd.Thread(target=self.swapNumber, args=(self.numbers-1, self.numbers-2))  ##JUST TO TEST
               
        
        
        thread_swap = thd.Thread(target=self.applySelectedAlgorithm)       
        thread_swap.start()    
        
        
        
        # print("Secondary thread is over")            
              
        
        
    def applySelectedAlgorithm(self):
        check_sorted = all(self.listBars[i+1].data >= self.listBars[i].data  for i in range(0, self.numbers-1, 1))
        if check_sorted == False:
            if self.algorithm ==  "Quicksort" or self.algorithm =="Quick3waySort":
                std.switcherFunction[self.algorithm](self,0,self.numbers-1)             
            elif self.algorithm == "MergeSortTD" or self.algorithm == "MergesortBU":
                std.switcherFunction[self.algorithm](self, 0,self.numbers-1)    
            else:
                [std.switcherFunction[self.algorithm](current, self) for current in self.arguments]      
        else:
            msg.showwarning("Sorting animations","Your array is already sorted")
                
        
    def createcomponents(self, titre, width, height):
        self.title(titre)
        self.width = width
        self.height = height
        self.configure(bg=COLORS[6])
        dim = (str(width), str(height))
        dimension = "x".join(dim)
        self.geometry(dimension)        
        self.labelAnimations = tk.LabelFrame(self, text="Animations",  relief="raised", fg=COLORS[7], bg=COLORS[6])
        self.labelAnimations.pack(fill=tk.BOTH,expand=1)
        self.canvas = tk.Canvas(self.labelAnimations, width=self.width, height=500, bg=COLORS[13], scrollregion = (FIRST_PIXEL,FIRST_PIXEL,LAST_PIXEL, LAST_PIXEL))
        hbar=tk.Scrollbar(self.canvas,orient=tk.HORIZONTAL)
        hbar.pack(side=tk.BOTTOM,fill=tk.X)
        hbar.config(command=self.canvas.xview)
        self.canvas.config(xscrollcommand=hbar.set)  
        self.canvas.pack(fill=tk.BOTH, expand=1)
        self.labelArray = tk.LabelFrame(self, text ="Original array",relief="raised", fg=COLORS[7], bg =COLORS[6])
        self.labelArray.pack(fill=tk.BOTH, expand=0, padx= 4,pady=24)        
        self.arrayCanvas = tk.Canvas(self.labelArray, width=self.width/2, height=90, bg=COLORS[10], scrollregion = (FIRST_PIXEL,FIRST_PIXEL,LAST_PIXEL, LAST_PIXEL))
        self.arrayCanvas.pack(fill=tk.BOTH, expand=10, padx=10, pady=5)
        vbararrayCanvas=tk.Scrollbar(self.arrayCanvas,orient=tk.VERTICAL)
        vbararrayCanvas.pack(side=tk.RIGHT,fill=tk.Y)
        vbararrayCanvas.config(command=self.arrayCanvas.yview)
        self.arrayCanvas.config(yscrollcommand=vbararrayCanvas.set)  
        hbararrayCanvas = tk.Scrollbar(self.arrayCanvas, orient=tk.HORIZONTAL)
        hbararrayCanvas.pack(side=tk.BOTTOM, fill=tk.X)
        hbararrayCanvas.config(command=self.arrayCanvas.xview)
        self.arrayCanvas.config(xscrollcommand=hbararrayCanvas.set)             
        self.secondary_container = tk.LabelFrame(self, text ="Input Board", fg=COLORS[7], relief="raised", bg=COLORS[6])
        self.secondary_container.pack(expand=0, fill=tk.BOTH, pady=4) 
        self.rangeFrame= tk.Frame(self.secondary_container,bg=COLORS[6])
        self.rangeFrame.pack()
        self.min_Label =tk.Label(self.rangeFrame, text="Min number : ",  bg=COLORS[6], font=("Arial 10 bold"))
        self.min_Label.pack(side=tk.LEFT)
        self.min_Entry=ttk.Entry(self.rangeFrame, width=8)
        self.min_Entry.pack(side=tk.LEFT, padx =(5,5))
        self.max_Label =tk.Label(self.rangeFrame, text=" : number Max",  bg=COLORS[6], font=("Arial 10 bold"))
        self.max_Label.pack(side=tk.RIGHT)
        self.max_Entry=ttk.Entry(self.rangeFrame, width=8)
        self.max_Entry.pack(side=tk.RIGHT)
        self.size_Label =tk.Label(self.secondary_container, text="Enter array size:",  bg=COLORS[6], font=("Arial 10 bold"))
        self.size_Label.pack(side=tk.LEFT, padx=10)
        name = tk.StringVar()
        self.size_Entry=ttk.Entry(self.secondary_container, width=8, textvariable=name)
        self.size_Entry.pack(side=tk.LEFT)
        algos = ALGORITHMS
        self.algo_ComboList =ttk.Combobox(self.secondary_container, values=algos, state="readonly")
        self.algo_ComboList.current(5)
        self.algo_ComboList.pack(side=tk.RIGHT, padx=30)
        self.algo_Label =tk.Label(self.secondary_container, text="Algorithms:", bg=COLORS[6], font=("Arial 10 bold"))
        self.algo_Label.pack(side=tk.RIGHT, padx=3)
        self.button_launch = tk.Button(self.secondary_container, bg=COLORS[1], fg=COLORS[5],text="Launch", width=8, command= lambda : self.launch())
        self.button_launch.pack(side=tk.TOP, pady=(70,10))
        self.size_Entry.focus()        
        
        
        
    def addComponents(self, inputarray):
            START_POINT_X_INITIAL =25
            START_POINT_X = START_POINT_X_INITIAL    
            START_POINT_Y_INITIAL = 5         
            START_POINT_Y = START_POINT_Y_INITIAL
            COUNT_ROW = 0
            width_rectangle = 50
            height_rectangle =50        
            count = 0
            for number in inputarray:
                if number >=0 :
                    self.arrayCanvas.create_rectangle(START_POINT_X, START_POINT_Y,START_POINT_X+width_rectangle, START_POINT_Y+height_rectangle, fill=COLORS[8])
                    self.arrayCanvas.create_text(START_POINT_X+width_rectangle/2, START_POINT_Y+height_rectangle/2, text=str(number),font=("Arial 9 bold"), fill=COLORS[1])
                    START_POINT_X =START_POINT_X+width_rectangle+ROW_SPACE_DISPLAY_ARRAY
                else:
                    self.arrayCanvas.create_rectangle(START_POINT_X, START_POINT_Y,START_POINT_X+width_rectangle, START_POINT_Y+height_rectangle, fill=COLORS[9])
                    self.arrayCanvas.create_text(START_POINT_X+width_rectangle/2, START_POINT_Y+height_rectangle/2, text=str(number),fill=COLORS[1], font=("Arial 9 bold"))
                    START_POINT_X =START_POINT_X+width_rectangle+ROW_SPACE_DISPLAY_ARRAY
                count+=1
                if count == 10:
                  COUNT_ROW+= 1
                  START_POINT_X = START_POINT_X_INITIAL
                  START_POINT_Y =START_POINT_Y_INITIAL + COUNT_ROW *(COL_SPACE_DISPLAY_ARRAY+height_rectangle)
                  count = 0
                