# Python3 program to find minimum number 
# of dice throws required to reach last 
# cell from first cell of a given 
# snake and ladder board 

# An entry in queue used in BFS 
class QueueEntry(object): 
	def __init__(self, v = 0, dist = 0): 
		self.v = v 
		self.dist = dist 

'''This function returns minimum number of 
dice throws required to. Reach last cell 
from 0'th cell in a snake and ladder game. 
move[] is an array of size N where N is 
no. of cells on board. If there is no 
snake or ladder from cell i, then move[i] 
is -1. Otherwise move[i] contains cell to 
which snake or ladder at i takes to.'''
def getMinDiceThrows(move, N): 
	
	# The graph has N vertices. Mark all 
	# the vertices as not visited 
	visited = [False] * N 

	# Create a queue for BFS 
	queue = [] 

	# Mark the node 0 as visited and enqueue it 
	visited[0] = True

	
	queue.append(QueueEntry(0, 0)) 

	
	qe = QueueEntry() 
	while queue: 
		qe = queue.pop(0) 
		v = qe.v
		
		if v == N - 1: 
			break

		
		j = v + 1
		while j <= v + 6 and j < N: 
		
			
			if visited[j] is False: 
				
				
				a = QueueEntry() 
				a.dist = qe.dist + 1
				visited[j] = True

				
				a.v = move[j] if move[j] != -1 else j 

				queue.append(a) 

			j += 1

	
	return qe.dist 

 
N = 30
moves = [-1] * N 


moves[2] = 21
moves[4] = 7
moves[10] = 25
moves[19] = 28


moves[26] = 0
moves[20] = 8
moves[16] = 3
moves[18] = 6

print("Min Dice throws required is {0}". 
	format(getMinDiceThrows(moves, N))) 


