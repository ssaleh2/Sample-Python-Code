#-------------------------------------------------------------------------------
# Sameh_Saleh_205_PP2_DRIVER.py
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
from Sameh_Saleh_205_PP2_GUI import GUIFrame
#create root window and set title
root=Tk()
root.title("Gomoku")
#create GUI object to place in root window
app=GUIFrame(root)
#automatic loop that runs GUI and associated elements
root.mainloop()
