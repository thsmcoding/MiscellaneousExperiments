# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 07:45:20 2020
@author:HTS
""" 
from Start.setup_mod import WINDOW_TITLE
from Start.setup_mod import WINDOW_HEIGHT
from Start.setup_mod import WINDOW_WIDTH
import Modules.Appwindow as appwin



def main():
    app = appwin.Appwindow(WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT)
    app.mainloop()
    app.quit()
    
    
if __name__ == "__main__":
    main()    