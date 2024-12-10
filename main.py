#imports customtkinter library for GUI
import customtkinter

#imports UI libraries for GUI
from tkdial import *

#imports math libraries for question system
import math
import random

#app init
class App(customtkinter.CTk):
    
    def __init__(self):
        #=========================================================     WINDOW INITIALIZATION     =====================================================================
        super().__init__()
        self.geometry("1920x1080")   
        self.title("Munchkin Mathematics")

        #init themes
        customtkinter.set_default_color_theme("dark-blue")
        
        self.mode = "title"

        #=================================================================     FRAMES     =============================================================================
        
        self.title_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.title_frame.place(x=0, y=0)
        
        self.select_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.select_frame.place(x=1920, y=0)
        
        self.game_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.game_frame.place(x=1920*2, y=0)
        
        self.create_title_screen()
        self.create_select_screen()
        #self.create_game_screen()
        
    #=============================================================     FRAME INITIALIZATION     =======================================================================
        
    def create_title_screen(self):
        #title screen
        self.title_label = customtkinter.CTkLabel(self.title_frame, text="Munchkin Mathematics", font=("Leafy", 130), anchor="center")
        self.title_label.place(relx=0.5, rely=0.35, anchor="center")
        
        self.start_button = customtkinter.CTkButton(self.title_frame, text="Start", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_start)
        self.start_button.place(relx=0.5, rely=0.50, anchor="center")
        
        self.quit_button = customtkinter.CTkButton(self.title_frame, text="Quit", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_quit)
        self.quit_button.place(relx=0.5, rely=0.6, anchor="center")
        
        self.author_label = customtkinter.CTkLabel(self.title_frame, text="by the pokrok lad himself, obsidio", font=("Leafy", 50))
        self.author_label.place(relx=0.5, rely=0.8, anchor="center")
        
    def create_select_screen(self):
        #title screen
        self.select_label = customtkinter.CTkLabel(self.select_frame, text="this is the select screen", font=("Leafy", 150))
        self.select_label.place(relx=0.5, rely=0.4, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.select_frame, text="Back", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_back)
        self.select_button.place(relx=0.5, rely=0.60, anchor="center")
        
    #==============================================================    BUTTON FUNCTIONS     ============================================================================
        
    def button_start(self):
        print("started!")
        self.swap_windows_right()
    
    def button_back(self):
        print("returning!")
        self.swap_windows_left()

    
    def button_quit(self):
        self.destroy()

    #=============================================================    ANIMATION FUNCTIONS     ===========================================================================
    
    def swap_windows_right(self):
        if self.mode == "title":
            print("TITLE MODE")
            self.title_frame.place(x=-1920)
            self.select_frame.place(x=0)
            #add game frame here
            self.mode = "select"
            
        elif self.mode == "select":
            pass
        
        #game mode implementation
    
    def swap_windows_left(self):
        if self.mode == "title":
            pass
            
        elif self.mode == "select":
            self.title_frame.place(x=0)
            self.select_frame.place(x=1920)
            #add game frame here
            self.mode = "title"
        
        #game mode implementation
    
#app loop
app = App()
app.mainloop()