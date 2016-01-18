#-------------------------------------------------------------------------------
# Sameh_Saleh_205_PP2_GUI.py
# Student Name: Sameh Saleh
# Assignment: Project #2
# Submission Date: 5/7/2010
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: (1. Python Programming for the Absolute Beginner-2nd edition
#	       2. Python Library and Language Reference
#	       3. Blackboard slides)
#-------------------------------------------------------------------------------
# Comments: (a note to the grader as to any problems or uncompleted aspects of
# of the assignment)
#-------------------------------------------------------------------------------
# Pseudocode: none needed as indicated by specifications
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
from Tkinter import *
from tkMessageBox import *
from tkFont import *
from Sameh_Saleh_205_PP2_CLASS import *
class GUIFrame(Frame):
	def __init__(self, master):
		Frame.__init__(self,master)
		#setting up the left and right frames
		self.layout=Frame(master)
		self.layout.grid()
		self.leftframe = Frame(self.layout, relief=RIDGE, height=512,\
		width=225)
		self.leftframe.grid(column=0,row=0)
		self.rightframe = Frame(self.layout, background="white", \
			relief=RIDGE, height = 512, width = 512)
		self.rightframe.grid(column=1,row=0)
		#setting up font used in the title
		self.bold=Font(weight=BOLD,size=16)
		self.size=Font(size=11)
		#initializing class level variables 
		self.coordinates=()
		self.coordinate_list=[]
		self.played_black=[]
		self.played_white=[]
		self.reverse_dict={}
		self.gamepiece_dict={}
		self.turn=0
		self.moves=0
		#creating board based on GUI interface in methods below
		self.set_widgets()
		self.gamepieces()
			
	def set_widgets(self):
		"""set up the widgets for the game board (the right frame) and the 
		labels and buttons introducing gameplay in the left frame"""
		#title label
		self.game_title = Label(self.leftframe, text = "Welcome to Gomoku!",\
		font=self.bold).place(y= 0, x= 0)
		#canvas for board
		self.draw_board=Canvas(self.rightframe,bg='#997745',width=512,\
		height=512)
		self.draw_board.place(x=0, y=0, height=512, width=512)
		#creating lines to form grid and numbers for each line
		for (column_range) in range(15):
			column_range+=1
			number_column=self.draw_board.create_text(((column_range)*30+23)\
			,23,fill="white")
			self.draw_board.itemconfig(number_column,text=str(column_range))
			self.draw_board.create_line(((column_range)*30),0,((column_range\
			)*30),512,fill="white")
			self.draw_board.create_line(480,0,480,512,fill="white")
		for row_range in range(15):
			row_range+=1
			number_row=self.draw_board.create_text(23,((row_range)*30+23),\
			fill="white")
			self.draw_board.itemconfig(number_row,text=str(row_range))
			self.draw_board.create_line(0,((row_range)*30),512,((row_range)*\
			30),fill="white")
			self.draw_board.create_line(0,480,512,480,fill="white")
		#creating/placing buttons for new game, undo, and quit
		self.new_game= Button(self.leftframe, text="New Game", font=self.size\
		, bg= "black", fg="white", padx=32, pady=15, bd=5)
		self.new_game.place(x=35, y=200)
		self.new_game.configure(command=self.reset)
		self.undo_button= Button(self.leftframe,text="Undo", font=self.size, \
		padx=50, bg= "black", fg="white", pady=15, bd=5)
		self.undo_button.place(x=35, y=275)
		self.undo_button.configure(command=self.undo)
		self.quit_button=Button(self.leftframe,text="Quit", font=self.size, \
		padx=53, bg= "black", fg="white", pady=15, bd=5)
		self.quit_button.configure(command=self.quit)
		self.quit_button.place(x=35, y=350)
	def gamepieces(self):
		"""creating the actual 225 gamepieces used in gameplay by using labels
		and and providing a base color the same as the background (canvas)"""
		counter=0
		for column_range in range(15):
			button_x=((column_range+2)*30)
			for row_range in range(15):
				button_y=((row_range+2)*30)
				#appending each of the 225 coordinates to a coordinate list 
				# to then use as key-value pairs in a dictionary with the 
				#tkinter reference for the labels (the gamepieces)
				self.coordinate_list.append((button_x,button_y))
				#create and place labels (gamepieces)
				self.gamepiece=Label(self.rightframe, bg='#997745', \
				height=1, width=2, relief=RIDGE, padx=3, pady=3)
				self.gamepiece.place(x=button_x, y=button_y, anchor=\
				CENTER)
				#two dictionaries are created: one to access through the 
				#tkinter reference to produce the coordinates and one to 
				#access the tkinter reference from the coordinates
				self.gamepiece_dict[self.gamepiece]=\
				self.coordinate_list[counter]
				self.reverse_dict[self.coordinate_list[counter]]=\
				self.gamepiece
				counter+=1
		#binding each of the 225 buttons to the method button_press below
		for piece in self.gamepiece_dict:
			piece.bind("<ButtonRelease-1>",self.button_press)		
	def button_press(self, event):
		"""switches turns so that when label is pressed color switches to 
		black or white depending on the turn, then it is disabled by
		unbinding and finally checks to see who wons by instantiating an 
		object of the logic class to then use the methods in the logic 
		class"""
		if self.turn==0:
			#changes gamepiece to black
			event.widget.configure(bg="black",height=1, width=2, \
			padx=5, pady=5)
			event.widget.unbind("<ButtonRelease-1>")
			self.coordinates=self.gamepiece_dict[event.widget]
			#appends coordinates clicked to list of gampieces played by the 
			#black stone
			self.played_black.append(self.coordinates)
			self.turn=1
			self.moves+=1
			#passes arguments: coordinates, two lists that hold what each 
			#player has already played, and number of moves
			self.gameplay=GomokuGame(self.coordinates, self.played_black,
			self.played_white, self.moves)
			self.gameplay.check_vertical()
			self.gameplay.check_horizontal()
			self.gameplay.check_diagonal()
			#if winner has been determined (i.e. True), then the GUI will
			#reset according to the reset method below
			if self.gameplay.restart():
				self.reset()
		elif self.turn==1:
			#changes gamepiece to white (same as above)
			event.widget.configure(bg="white",height=1, width=2,\
			padx=5, pady=5)
			event.widget.unbind("<ButtonRelease-1>")
			self.coordinates=self.gamepiece_dict[event.widget]
			self.played_white.append(self.coordinates)
			self.turn=0
			self.moves+=1
			self.gameplay_white=GomokuGame(self.coordinates, \
			self.played_black, self.played_white, self.moves)
			self.gameplay_white.check_vertical()
			self.gameplay_white.check_horizontal()
			self.gameplay_white.check_diagonal()
			if self.gameplay_white.restart():
				self.reset()
	def undo(self):
		"""when undo button is clicked, the moves are decreased by 1, the turn
		is reverted, and the label linked with the last coordinates in the 
		buttons played list is changed back to the neutral color and bound to
		the button press method"""
		if self.turn==1 and self.played_black!=[]:
			self.moves-=1
			self.turn=0
			self.reverse_dict[self.played_black[-1]].bind(\
			"<ButtonRelease-1>", self.button_press)
			self.reverse_dict[self.played_black[-1]].configure(\
			bg='#997745', height=1, width=2, relief=RIDGE, padx=3, pady=3)
			#the last coordinate in the buttons played list is removed each 
			#time
			self.played_black=self.played_black[0:-1]
		elif self.turn==0 and self.played_white!=[]:
			self.moves-=1
			self.turn=1
			self.reverse_dict[self.played_white[-1]].bind(\
			"<ButtonRelease-1>", self.button_press)
			self.reverse_dict[self.played_white[-1]].configure(\
			bg='#997745', height=1, width=2, relief=RIDGE, padx=3, pady=3)
			#the last coordinate in the buttons played list is removed each 
			#time
			self.played_white=self.played_white[0:-1]
	def reset(self):
		"""the state of the game is returned to the original by returning 
		moves and turn to 0 and rebinding all the labels to button press and 
		#changing the background color to neutral"""
		self.turn=0
		self.moves=0
		for piece in self.gamepiece_dict:
			piece.configure(bg='#997745', height=1, \
			width=2, relief=RIDGE, padx=3, pady=3)
			piece.bind("<ButtonRelease-1>",self.button_press)	
		self.played_black=[]
		self.played_white=[]
	def quit(self):
		"""when the quit button is clicked, a message box pops up to confirm
		quitting and if 'ok' is pressed, the application ends"""
		quitting = askokcancel("Quitting Program", "Do you really want to "\
		"exit the game?")
		if quitting:
			self.layout.quit()
	
