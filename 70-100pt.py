#########################################
#
#         70-100pt - Making a game
#
#########################################


# 70pt - Add buttons for left, right and down that move the player circle
# 100pt - using lab 11 as an example, add in three horizontally scrolling "enemies"
# Make them scroll at different speeds and directions.

from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
player = drawpad.create_oval(390,580,410,600, fill="red")

# Create your "enemies" here, before the class
enemy1 = drawpad.create_rectangle(50,50,75,75, fill='blue')
enemy2 = drawpad.create_rectangle(100,400,125,425, fill='blue')
enemy3 = drawpad.create_rectangle(150,250,175,275, fill='blue')
class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="down", background= "blue")
       	    self.down.grid(row=0,column=1)
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "red")
       	    self.right.grid(row=0,column=2)
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "yellow")
       	    self.left.grid(row=0,column=3)
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=RIGHT)
       	    # call the animate function to start our recursion
       	    self.animate()
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    global enemy1
	    
	    x1, y1, x2, y2 = drawpad.coords(enemy1)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(enemy1,-800,0)
            elif x1 < 0:
                direction = 10
            drawpad.move(enemy1,10,0)
	    global enemy2
	    x1, y1, x2, y2 = drawpad.coords(enemy2)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(enemy2,-800,0)
            elif x1 < 0:
                direction = 10
            drawpad.move(enemy2,30,0)
	    global enemy3
	    x1, y1, x2, y2 = drawpad.coords(enemy3)
            if x2 > drawpad.winfo_width(): 
                drawpad.move(enemy3,-800,0)
            elif x1 < 0:
                direction = 10
            drawpad.move(enemy3,15,0)

	    # Uncomment this when you're ready to test out your animation!
	    drawpad.after(10,self.animate)
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)
	   
        def downClicked(self, event):
            global oval
            global player
            drawpad.move(player,0,20)

        def rightClicked(self, event):
            global oval
            global player
            drawpad.move(player,20,0)

        def leftClicked(self, event):
            global oval
            global player
            drawpad.move(player,-20,0)
            
app = MyApp(root)
root.mainloop()