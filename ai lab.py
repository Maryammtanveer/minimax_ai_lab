import math
 
# Maximizing player can get
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
 # Base case: targetDepth reached
 
 
 if curDepth == targetDepth:
     
     return scores[nodeIndex]
 if maxTurn:
     return max(
 minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
 minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
 )
 else:
     return min(
 minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
 minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
 )
# Driver code
scores = [3, 5, 2, 9, 0, 7]
treeDepth = math.ceil(math.log2(len(scores)))
# Pad scores to make a complete binary tree
scores += [0] * (2**treeDepth - len(scores))
print("The optimal value is:", end=" ")
print (minimax(0, 0, True, scores, treeDepth))
 


# Reorder branches and observe how pruning changes while the Minimax value remains the same
import math
# add leaf counter
minmax_count =0
# Maximizing player can get
def minimax(curDepth, nodeIndex, maxTurn, scores, targetDepth):
 # Base case: targetDepth reached
# now we add global function to change the variable inside the function
 global minmax_count
 if curDepth == targetDepth:
     minmax_count += 1
     return scores[nodeIndex]
 if maxTurn:
     return max(
 minimax(curDepth + 1, nodeIndex * 2, False, scores, targetDepth),
 minimax(curDepth + 1, nodeIndex * 2 + 1, False, scores, targetDepth)
 )
 else:
     return min(
 minimax(curDepth + 1, nodeIndex * 2, True, scores, targetDepth),
 minimax(curDepth + 1, nodeIndex * 2 + 1, True, scores, targetDepth)
 )
# Driver code
scores = [7, 3, 5, 2, 9, 0]
treeDepth = math.ceil(math.log2(len(scores)))
# Pad scores to make a complete binary tree
scores += [0] * (2**treeDepth - len(scores))
print("The optimal value is:", end=" ")
result = minimax(0, 0, True, scores, treeDepth)
print("minmax value :", result)
print("leaved checked:", minmax_count)







# alpha-beta pruning
import math
 
def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    
    if depth == target:
         
        return scores[index]

    if maxTurn:
        value = float('-inf')

        for i in range(2):
            value = max(
                value,
                alphabeta(depth + 1, index * 2 + i, False,
                          scores, target, alpha, beta)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for i in range(2):
            value = min(
                value,
                alphabeta(depth + 1, index * 2 + i, True,
                          scores, target, alpha, beta)
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value


scores = [3, 5, 2, 9, 3, 5, 2, 9]
 
depth = int(math.log2(len(scores)))
print(alphabeta(
    0, 0, True, scores, depth,
    float('-inf'), float('inf')
))
 

# Reorder branches and observe how pruning changes while the Minimax value remains the same

#  for comparison 
import math
# add leaf counter
alphabeta_count = 0

def alphabeta(depth, index, maxTurn, scores, target, alpha, beta):
    global alphabeta_count
    if depth == target:
        alphabeta_count += 1
        return scores[index]

    if maxTurn:
        value = float('-inf')

        for i in range(2):
            value = max(
                value,
                alphabeta(depth + 1, index * 2 + i, False,
                          scores, target, alpha, beta)
            )

            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for i in range(2):
            value = min(
                value,
                alphabeta(depth + 1, index * 2 + i, True,
                          scores, target, alpha, beta)
            )

            beta = min(beta, value)

            if alpha >= beta:
                break

        return value
#we reverse values in scroes 
scores = [ 9, 2, 5, 3, 9, 2, 5, 3]
depth = int(math.log2(len(scores)))

result =(alphabeta(
    0, 0, True, scores, depth,
    float('-inf'), float('inf')
))
print("alpha-beta value :", result)
print("leaved checked:", alphabeta_count)