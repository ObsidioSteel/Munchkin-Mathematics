#imports customtkinter library for GUI
import customtkinter

#imports UI libraries for GUI
from tkdial import *

#imports math libraries for question system
import math
import random
import time

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
        self.quiz = 0
        self.digits = 1
        self.num1 = 0
        self.num2 = 0
        self.operations = ["+", "-", "x", "÷"]
        self.eval_operations = ["+", "-", "*", "/"]
        self.num_correct = 0
        self.average_time = 0.0
        self.question = ""
        self.quiz_length = 10
        self.questions_left = self.quiz_length
        self.finished = False
        self.seconds = 0

        #=================================================================     FRAMES     =============================================================================
        
        self.title_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.title_frame.place(x=0, y=0)
        
        self.quiz_select_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.quiz_select_frame.place(x=1920, y=0)
        
        self.digit_select_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.digit_select_frame.place(x=1920, y=0)
        
        self.game_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.game_frame.place(x=1920, y=0)
        
        self.results_frame = customtkinter.CTkFrame(self, width=1920, height=1080)
        self.results_frame.place(x=1920, y=0)
        
        self.create_title_screen()
        self.create_quiz_select_screen()
        self.create_digit_select_screen()
        
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
        
    def create_quiz_select_screen(self):
        #quiz select screen
        self.select_label = customtkinter.CTkLabel(self.quiz_select_frame, text="Select a quiz!", font=("Leafy", 150))
        self.select_label.place(relx=0.5, rely=0.2, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.quiz_select_frame, text="Addition", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_addition)
        self.select_button.place(relx=0.4, rely=0.40, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.quiz_select_frame, text="Subtraction", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_subtraction)
        self.select_button.place(relx=0.6, rely=0.40, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.quiz_select_frame, text="Multiplication", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_multiplication)
        self.select_button.place(relx=0.4, rely=0.60, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.quiz_select_frame, text="Division", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_division)
        self.select_button.place(relx=0.6, rely=0.60, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.quiz_select_frame, text="Back", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_back)
        self.select_button.place(relx=0.5, rely=0.80, anchor="center")
        
    def create_digit_select_screen(self):
        #digit select screen
        self.select_label = customtkinter.CTkLabel(self.digit_select_frame, text="How many digits?", font=("Leafy", 150))
        self.select_label.place(relx=0.5, rely=0.2, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.digit_select_frame, text="One", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_onedigit_start)
        self.select_button.place(relx=0.3, rely=0.50, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.digit_select_frame, text="Two", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_twodigit_start)
        self.select_button.place(relx=0.5, rely=0.50, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.digit_select_frame, text="Three", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_threedigit_start)
        self.select_button.place(relx=0.7, rely=0.50, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.digit_select_frame, text="Back", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_back)
        self.select_button.place(relx=0.5, rely=0.80, anchor="center")   
         
    def create_game_screen(self):
        #digit select screen
        self.select_label = customtkinter.CTkLabel(self.game_frame, text="QUIZ TIME", font=("Leafy", 150))
        self.select_label.place(relx=0.5, rely=0.2, anchor="center")
        
        self.select_label = customtkinter.CTkLabel(self.game_frame, text = self.question, font=("Leafy", 150))
        self.select_label.place(relx=0.5, rely=0.4, anchor="center")
        
        self.answer_entry = customtkinter.CTkEntry(self.game_frame, placeholder_text="Answer", width=250, height=70, font=("Leafy", 50))
        self.answer_entry.place(relx=0.5, rely=0.650, anchor="center")
        self.answer_entry.bind("<Return>", self.answer_entered)
        
        self.select_button = customtkinter.CTkButton(self.game_frame, text="Quit Quiz", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_back)
        self.select_button.place(relx=0.5, rely=0.80, anchor="center")
        
    def create_results_screen(self):
        #digit select screen
        self.select_label = customtkinter.CTkLabel(self.results_frame, text="Results:", font=("Leafy", 150))
        self.select_label.place(relx=0.5, rely=0.2, anchor="center")
        
        self.select_label = customtkinter.CTkLabel(self.results_frame, text="You answered " + str(self.num_correct) + "/" + str(self.quiz_length) + " questions right!", font=("Leafy", 100))
        self.select_label.place(relx=0.5, rely=0.35, anchor="center")
        
        self.select_label = customtkinter.CTkLabel(self.results_frame, text="You answered them in " + str(round(self.seconds, 2)) + " seconds!", font=("Leafy", 100))
        self.select_label.place(relx=0.5, rely=0.5, anchor="center")
        
        self.select_label = customtkinter.CTkLabel(self.results_frame, text="Your brain size: " + str(250 + (self.num_correct/self.quiz_length * ((self.quiz_length * (5 * self.digits)) - self.seconds) * 20)) + " cm^3!", font=("Leafy", 100))
        self.select_label.place(relx=0.5, rely=0.65, anchor="center")
        
        self.select_button = customtkinter.CTkButton(self.results_frame, text="Return to Title", width=250, height=70, font=("Leafy", 50), anchor="center", command=self.button_back)
        self.select_button.place(relx=0.5, rely=0.80, anchor="center")
        
    #==============================================================    BUTTON FUNCTIONS     ============================================================================
        
    def button_start(self):
        self.swap_windows_right()
    
    def button_back(self):
        self.swap_windows_left()

    def button_addition(self):
        self.quiz = 0
        self.swap_windows_right()
        
    def button_subtraction(self):
        self.quiz = 1
        self.swap_windows_right()
        
    def button_multiplication(self):
        self.quiz = 2
        self.swap_windows_right()
        
    def button_division(self):
        self.quiz = 3
        self.swap_windows_right()
    
    def button_quit(self):
        self.destroy()
        
    def button_onedigit_start(self):
        self.digits = 1
        self.swap_windows_right()
        
    def button_twodigit_start(self):
        self.digits = 2
        self.swap_windows_right()
        
    def button_threedigit_start(self):
        self.digits = 3
        self.swap_windows_right()

    def start_quiz_timer(self):
        if self.finished == False:   
            self.seconds += 0.05
            app.after(50, self.start_quiz_timer)
        

    #=============================================================    FUNCTIONS     ===========================================================================
    
    def swap_windows_right(self):
        if self.mode == "title":
            self.title_frame.place(x=-1920)
            self.quiz_select_frame.place(x=0)
            self.mode = "quiz select"
            
        elif self.mode == "quiz select":
            self.quiz_select_frame.place(x=1920)
            self.digit_select_frame.place(x=0)
            self.mode = "digit select"
        
        elif self.mode == "digit select":                
            self.quiz_length = 10
            self.questions_left = self.quiz_length
            self.next_question()
            self.game_frame.place(x=0)
            self.digit_select_frame.place(x=1920)
            self.mode = "game"
            self.finished = False
            self.seconds = 0
            self.start_quiz_timer()
            
        elif self.mode == "game":  
            self.game_frame.place(x=1920)
            self.create_results_screen()
            self.results_frame.place(x=0)
            self.finished = True
            self.mode = "results"
    
    def swap_windows_left(self):            
        if self.mode == "quiz select":
            self.title_frame.place(x=0)
            self.quiz_select_frame.place(x=1920)
            self.mode = "title"
            
        elif self.mode == "digit select":
            self.quiz_select_frame.place(x=0)
            self.digit_select_frame.place(x=1920)
            self.mode = "quiz select"
        
        elif self.mode == "game":
            self.title_frame.place(x=0)
            self.game_frame.place(x=1920)
            self.mode = "title"
        
        elif self.mode == "results":
            self.title_frame.place(x=0)
            self.results_frame.place(x=1920)
            self.mode = "title"
           
    def answer_entered(self, event):
        self.check_answer(self.answer_entry.get())
        self.next_question()
        
    def check_answer(self, answer):
        if int(answer) == round(eval(str(str(self.num1) + self.eval_operations[self.quiz] + str(self.num2)))):
            self.num_correct += 1
        else:
            pass
    
    def next_question(self):
        if self.questions_left > 0:
            for widget in self.game_frame.winfo_children():
                widget.destroy()
            self.num1 = random.randint(10 ** (self.digits - 1), 10 ** (self.digits) - 1)
            self.num2 = random.randint(10 ** (self.digits - 1), 10 ** (self.digits) - 1)
            self.question = str(self.num1) + " " + self.operations[self.quiz] + " " + str(self.num2) + " = ?"
            self.create_game_screen()
            self.answer_entry.focus()
        else:
            self.finish_quiz()
        self.questions_left -= 1
        
    def finish_quiz(self):
        self.swap_windows_right()
            
    
#app loop
app = App()
app.resizable(False, False)
app.mainloop()