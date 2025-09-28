#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random
import time



tk = Tk()
tk.title("Pong!")
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg = "black")
canvas.pack()
tk.update()

score_text_p1 = canvas.create_text(125,40, font=("Arial", 60), fill="white")
score_text_p2 = canvas.create_text(375,40, font=("Arial", 60), fill="white")

counter = 0
counter1 = 0

class Ball:
    def __init__(self,canvas,color,paddle,paddle1):
      self.canvas = canvas
      self.paddle = paddle
      self.paddle1 = paddle1
      self.id = canvas.create_oval(10,10,25,25, fill = color)
      self.canvas.move(self.id, 233,200)
      starts = [-3,3]
      random.shuffle(starts)  
      self.x = starts[0]
      self.y = -3
      self.canvas_height = self.canvas.winfo_height()
      self.canvas_width = self.canvas.winfo_width()
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0]<=0:
            self.x = 3
            self.score(True)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)
       
        if self.hit_paddle(pos) == True:
            self.x = 3
        if self.hit_paddle1(pos) == True:
            self.x = -3


            
    def hit_paddle(self,pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                
                 
                # Check if ball is hitting top or bottom of paddle
                if pos[2] <= paddle_pos[0] or pos[0] >= paddle_pos[2]:
                # Ball is hitting the side — do not change vertical direction
                    pass
                else:
                # Ball is hitting top or bottom — bounce vertically
                    if self.y > 0:
                        self.y = -3
                    elif self.y < 0:
                        self.y = 3
                return True

    
    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] <= paddle_pos[2] and pos[2] >= paddle_pos[0]:
                
               
                if pos[2] >= paddle_pos[0] or pos[0] >= paddle_pos[2]:
                    pass  # Side hit — no vertical bounce
                else:
                    if self.y > 0:
                        self.y = -3
                    elif self.y < 0:
                        self.y = 3
                return True
        return False

    
    def score(self,val):
      global counter
      global counter1
      global score_text_p1
      global score_text_p2
        
      if val == True:
        counter += 1
        self.canvas.itemconfig(score_text_p1, text=str(counter))
        
        
      if val == False:
        counter1 += 1
        a = self.canvas.itemconfig(score_text_p2, text=str(counter1))
        
          
    
class Paddle:
    def __init__(self,canvas,color):
      self.canvas = canvas
      self.id = canvas.create_rectangle(0,150,30,250, fill = color)
      self.y = 0
      self.canvas_height = self.canvas.winfo_height()
      self.canvas_width = self.canvas.winfo_width()
      self.canvas.bind_all('<KeyPress-a>', self.move_up) #Renamed 'a' & 'd' to <Keypress...also renamed the self.BINDINGS
      self.canvas.bind_all('<KeyPress-d>', self.move_down)
    
    def draw(self):
        pos = self.canvas.coords(self.id) # put self.canvas.move(self.id,0, self.y) later on in the code & replaced if pos[1] <= 0: self.y = 0 if pos[3] >= 400: self.y = 0 to avoid digging in to the walls.
        if (pos[1] + self.y >=0) and (pos[3] + self.y <= self.canvas_height):
            self.canvas.move(self.id,0,self.y)
        else:
            self.y = 0 #Stop moving when hitting boundary
            
    def move_up(self,evt): #Renamed turn_left to move_up
        self.y = -3
    
    def move_down(self,evt): #Renamed turn_right to move_down
        self.y = 3
     
class Paddle1:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250, fill = color)  
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        self.canvas.bind_all('<KeyPress-Left>', self.move_up)
        self.canvas.bind_all('<KeyPress-Right>', self.move_down)  
      
    def draw(self):
        pos = self.canvas.coords(self.id) # put self.canvas.move(self.id,0, self.y) later on in the code & replaced if pos[1] <= 0: self.y = 0 if pos[3] >= 400: self.y = 0 to avoid digging in to the walls.
        if (pos[1] + self.y >=0) and (pos[3] + self.y <= self.canvas_height):
            self.canvas.move(self.id,0,self.y)
        else:
            self.y = 0 #Stop moving when hitting boundary
     
            
    def move_down(self,evt): #Renamed turn_right to move_down
        self.y = 3

    def move_up(self,evt): #Renamed turn_left to move_up
        self.y = -3

game_running = True

#Define variables inside the function
paddle = Paddle(canvas,"blue")
paddle1 = Paddle1(canvas,"blue")
ball = Ball(canvas, "orange", paddle, paddle1)
    
def restart_game():
    global counter, counter1, score_text_p1, score_text_p2
    global paddle, paddle1, ball
    
    # Clear everything from canvas
    canvas.delete("all")
    
    #Define variables inside the function
    paddle = Paddle(canvas,"blue")
    paddle1 = Paddle1(canvas,"blue")
    ball = Ball(canvas, "orange", paddle, paddle1)
    
    # Reset scores
    counter = 0
    counter1 = 0
    
    # Recreate score text
    score_text_p1 = canvas.create_text(125, 40, font=("Arial", 60), fill="white", text="0")
    score_text_p2 = canvas.create_text(375, 40, font=("Arial", 60), fill="white", text="0")

    
    global game_running
    
    game_running = True
    

        
    run_game_loop()    
    
        
def run_game_loop():
    
    
    
    global counter, counter1, score_text_p1, score_text_p2
    
    global game_running
    
    if not game_running:
            return
        
    ball.draw()
    paddle.draw()
    paddle1.draw()
    tk.update_idletasks()
    tk.update()
    
    
    if counter == 10 or counter1 == 10:
        game_running = False #Stop the loop
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
            
        if counter == 10:
            canvas.create_text(250,150, text = "Congrats Player 1! You Win!", font =("Arial",24), fill = "red")
            canvas.create_text(250,215, text = "Score:" + str(counter) + "-" + str(counter1), font =("Arial",24), fill = "red")
            
        else:
             canvas.create_text(250,150, text = "Congrats Player 2! You Win!", font =("Arial",24), fill = "red")
             canvas.create_text(250,215, text = "Score:" + str(counter) + "-" + str(counter1), font =("Arial",24), fill = "red")  
        tk.update()
        
        
        
        restart_button = Button(tk, text="Restart", font=("Arial",14), command=restart_game)
        exit_button = Button(tk, text="Exit", font=("Arial",14), command=tk.destroy)
        
        canvas.create_window(200,300, window = restart_button)
        canvas.create_window(300,300, window = exit_button)
        tk.update()
    
    else:
        tk.after(10,run_game_loop)
        
run_game_loop()
            
tk.mainloop()  

