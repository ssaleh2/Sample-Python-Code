def main():
	print "Welcome to Tic-Tac-Toe!"
	rowA=[(),(),()]
	rowB=[(),(),()]
	rowC=[(),(),()]
	rowall=[rowA,rowB,rowC]
	print rowA
	print rowB
	print rowC
	while rowA[0]==() or rowA[1]==() or rowA[2]==() or rowB[0]==() or rowB[1]==() or rowB[2]==() or rowC[0]==() or rowC[1]==() or rowC[2]==():
		playrowA=input("Please choose row to put X in:")
		playcolumnA=input("Please choose column to put X in:")
		rowall[playrowA-1][playcolumnA-1]="X"
		print rowA
		print rowB
		print rowC
		playrowB=input("Please choose row to put O in:")
		playcolumnB=input("Please choose column to put O in:")
		rowall[playrowB-1][playcolumnB-1]="O"
		print rowA
		print rowB
		print rowC
	if rowA[0]=="X" and rowA[1]=="X" and rowA[2]=="X" or rowB[0]=="X" and rowB[1]=="X" and rowB[2]=="X" or rowC[0]=="X" and rowC[1]=="X" and rowC[2]=="X":
		print "Player 1 wins!"
	elif rowA[0]=="O" and rowA[1]=="O" and rowA[2]=="O" or rowB[0]=="O" and rowB[1]=="O" and rowB[2]=="O" or rowC[0]=="O" and rowC[1]=="O" and rowC[2]=="O":
		print "Player 2 wins!"
	elif rowall[0][0]=="X" and rowall[1][0]=="X" and rowall[2][0]=="X" or rowall[0][1]=="X" and rowall[1][1]=="X" and rowall[2][1]=="X" or rowall[0][2]=="X" and rowall[1][2]=="X" and rowall[2][2]=="X":
		print "Player 1 wins!"
	elif rowall[0][0]=="O" and rowall[1][0]=="O" and rowall[2][0]=="O" or rowall[0][1]=="O" and rowall[1][1]=="O" and rowall[2][1]=="O" or rowall[0][2]=="O" and rowall[1][2]=="O" and rowall[2][2]=="O":
		print "Player 2 wins!"
	elif rowall[0][2]=="X" and rowall[1][1]=="X" and rowall[2][0]=="X" or rowall[0][0]=="X" and rowall[1][1]=="X" and rowall[2][2]=="X":
		print "Player 1 wins!"
	elif rowall[0][2]=="O" and rowall[1][1]=="O" and rowall[2][0]=="O" or rowall[0][0]=="O" and rowall[1][1]=="O" and rowall[2][2]=="O":
		print "Player 2 wins!"
	else:
		print "Draw!"
	print "Thank you for playing!"
main()
