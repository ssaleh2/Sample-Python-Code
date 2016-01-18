#-------------------------------------------------------------------------------
# Sameh_Saleh_205_PP2_CLASS.py
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
from tkMessageBox import *
class GomokuGame(object):
	#parameters of the logic class reference the GUI file for the arguments 
	#passed for checking the winner
	def __init__(self, coordinates, played_black, played_white, moves):
		#initializing instance variables
		self.coordinates=coordinates
		self.played_black=played_black
		self.played_white=played_white
		self.moves=moves
		#initializing class level variable
		self.winner=False
	def check_vertical(self):
		"""checks if there is a winner vertically by checking if the game-
		pidces above and below the gamepiece last clicked have also been 
		clicked by the same color"""
		self.five_vertical=[]
		index=1
		self.checking=True
		while self.checking==True:
			#executes if coordinates of the last gamepiece chosen are in list
			#of gamepieces played are black
			if self.coordinates in self.played_black:
				self.five_vertical.append(self.coordinates)
				try:
					#checks each button directly above the one before it to
					#see if it's black by updating index
					while (self.coordinates[0],self.coordinates[1]+\
					(30*index)) in self.played_black:
						#if it is, it appends it to the list
						self.five_vertical.append((self.coordinates\
						[0], self.coordinates[1]+(30*index)))
						index+=1
						#if the length of the list is 5, then there is 
						#five in a row and there is a winner
						if len(self.five_vertical)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass
				try:
					#checks each gamepiece directly below the one before it 
					#to see if it's black
					index=-1
					while (self.coordinates[0],self.coordinates[1]+\
					(30*index)) in self.played_black:
						self.five_vertical.append((self.coordinates[0], \
						self.coordinates[1]+(30*index)))
						index-=1
						if len(self.five_vertical)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass
				#if there is no five in a row, then the list to determine 
				#winner vertically is returned to empty 
				self.five_vertical=[]
			#same procedure as black gamepiece, but with white instead
			elif self.coordinates in self.played_white:
				self.five_vertical.append(self.coordinates)
				try:
					#increasing y
					index=1
					while (self.coordinates[0], self.coordinates[1]+(30*\
					index)) in self.played_white:
						self.five_vertical.append((self.coordinates[0], \
						self.coordinates[1]+(30*index)))
						index+=1
						if len(self.five_vertical)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass
				try:
					#decreasing y
					index=-1
					while (self.coordinates[0], self.coordinates[1]+(30*\
					index)) in self.played_white:
						self.five_vertical.append((self.coordinates[0], \
						self.coordinates[1]+(30*index)))
						index-=1
						if len(self.five_vertical)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass
				self.five_vertical=[]
			#exits checking vertically
			self.checking=False
	def check_horizontal(self):
		"""does the same procedure as vertically but checks horizontally"""
		self.five_horizontal=[]
		index=1
		self.checking=True
		while self.checking==True:
			if self.coordinates in self.played_black:
				self.five_horizontal.append(self.coordinates)
				try:
					#increasing x (checks each gamepiece to the right)
					while (self.coordinates[0]+(30*index), \
					self.coordinates[1]) in self.played_black:
						self.five_horizontal.append((self.coordinates[0]+\
						(30*index), self.coordinates[1]))
						index+=1
						if len(self.five_horizontal)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass
				try:
					#decreasing x (checkes each gamepiece to the left)
					index=-1
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]) in self.played_black:
						self.five_horizontal.append((self.coordinates[0]+\
						(30*index), self.coordinates[1]))
						index-=1
						if len(self.five_horizontal)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass
				self.five_horizontal=[]
			elif self.coordinates in self.played_white:
				self.five_horizontal.append(self.coordinates)
				try:
					index=1
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]) in self.played_white:
						self.five_horizontal.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]))
						index+=1
						if len(self.five_horizontal)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass
				try:
					index=-1
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]) in self.played_white:
						self.five_horizontal.append((self.coordinates[0]+\
						(30*index), self.coordinates[1]))
						index-=1
						if len(self.five_horizontal)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass	
				self.five_horizontal=[]
			self.checking=False
	def check_diagonal(self):
		"""does the same process as vertical but checks diagonally both
		ways"""
		self.five_diagonal_1=[]
		self.five_diagonal_2=[]
		index=1
		self.checking=True
		while self.checking==True:
			if self.coordinates in self.played_black:
				self.five_diagonal_1.append(self.coordinates)
				self.five_diagonal_2.append(self.coordinates)
				try:
					#increasing x and increasing y (checking northeast)
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]+(30*index)) in self.played_black:
						self.five_diagonal_1.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]+(30*index)))
						index+=1
						if len(self.five_diagonal_1)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass
				try:
					index=-1
					#decreasing x and decreasing y (checking southwest)
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]+(30*index)) in self.played_black:
						self.five_diagonal_1.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]+(30*index)))
						index-=1
						if len(self.five_diagonal_1)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass	
				try:
					index=1
					#increasing x and decreasing y (checking southeast)
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]-(30*index)) in self.played_black:
						self.five_diagonal_2.append((self.coordinates[0]+\
						(30*index), self.coordinates[1]-(30*index)))
						index+=1
						if len(self.five_diagonal_2)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass
				try:
					index=-1
					#decreasing x and increasing y (checking southwest)
					while (self.coordinates[0]+(30*index)\
					,self.coordinates[1]-(30*index)) in self.played_black:
						self.five_diagonal_2.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]-(30*index)))
						index-=1
						if len(self.five_diagonal_2)==5:
							self.win_message="Black wins!"
							self.win()
				except:
					pass	
				self.five_diagonal_1=[]
				self.five_diagonal_2=[]
			if self.coordinates in self.played_white:
				self.five_diagonal_1.append(self.coordinates)
				self.five_diagonal_2.append(self.coordinates)
				try:
					index=1
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]+(30*index)) in self.played_white:
						self.five_diagonal_1.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]+(30*index)))
						index+=1
						if len(self.five_diagonal_1)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass
				try:
					index=-1
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]+(30*index)) in self.played_white:
						self.five_diagonal_1.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]+(30*index)))
						index-=1
						if len(self.five_diagonal_1)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass	
				try:
					index=1
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]-(30*index)) in self.played_white:
						self.five_diagonal_2.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]-(30*index)))
						index+=1
						if len(self.five_diagonal_2)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass
				try:
					index=-1
					while (self.coordinates[0]+(30*index)\
					, self.coordinates[1]-(30*index)) in self.played_white:
						self.five_diagonal_2.append((self.coordinates[0]\
						+(30*index), self.coordinates[1]-(30*index)))
						index-=1
						if len(self.five_diagonal_2)==5:
							self.win_message="White wins!"
							self.win()
				except:
					pass	
				self.five_diagonal_1=[]
				self.five_diagonal_2=[]
			self.checking=False
		if self.moves==225 and self.winner!=True:
			self.draw()
	def win(self):
		"""once the length of one of the checking lists above equals 5, this 
		method is called and a message box appears indicating the winner"""
		self.checking=False
		self.win_box=showinfo("Winner!", self.win_message)
		if self.win_box:
			#winner is set to true
			self.winner=True
			#method restart is called to return value of the winner(i.e.true)
			self.restart()
	def restart(self):
		"""returns if there is a winner (True or False)"""
		return self.winner
	def draw(self):
		"""if no winner is determined, this method is called as 225 gamepieces
		have been pressed"""
		#message box indicating the draw is shows and the winner is set 
		#to true
		draw_box=showinfo("Draw!", "Draw, get ready for a rematch!")
		if draw_box:
			self.winner=True
			self.restart()
				
			
