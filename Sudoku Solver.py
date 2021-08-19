# Declare the board as a 2D matrix
# printBoard( Board 2D array ) - void
# findEmpty( Board 2D array ) - tuple [xInd,yInd]
# checkValid( Board 2D array , number to place, position[xInd, yInd]) - boolean
# solve( Board 2D array ) - recursive function --> boolean
# Print result

#Board 2D array
board =     [ [6, 0, 7, 1, 0, 5, 0, 9, 0],
              [5, 9, 4, 0, 2, 0, 1, 6, 0],
              [8, 0, 3, 9, 4, 0, 0, 0, 0],
              [0, 0, 0, 6, 0, 4, 0, 0, 0],
              [3, 6, 0, 0, 0, 0, 4, 0, 0],
              [2, 4, 8, 0, 0, 7, 0, 0, 0],
              [0, 0, 0, 0, 6, 9, 0, 3, 0],
              [7, 0, 0, 5, 0, 1, 2, 0, 0],
              [9, 8, 2, 4, 0, 3, 6, 5, 0]
]

#Print function
def printBoard(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print(" | ",end="")

            if j==8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#Function to return position of empty box in board
def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j) #return row,col indices as a tuple

    #if no empty positions
    return None

#Function to check if the curr number will be valid at the given position in board
def checkValid(bo,num,pos):

    #check if num is in that row
    for i in range(len(bo[0])):
        if bo[pos[0]][i]==num and i!=pos[1]:
            return False

    # check if num is in that col
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and i != pos[0]:
            return False

    # Find in which 3x3 box that pos lies in
    posX = pos[0]//3 #integer division
    posY = pos[1]//3

    # check if num is in that 3x3 box
    for i in range(posX*3 , posX*3 + 3):
        for j in range(posY * 3, posY * 3 + 3):
            if bo[i][j]==num and (i,j)!= pos:
                return False
    return True



# Recursive Function to Solve the board
def solve(bo):
    #get indices of empty position
    position = findEmpty(board)
    #if no empty positions
    if not position:
        return True
    else:
        row,col = position

    #try filling 1 to 10 in that position
    for i in range(1,10):

        # if the number is valid at that pos, update the position
        if checkValid(bo,i,(row,col)) :
            bo[row][col] = i

            # Again recursively call the solve function to check for other empty pos
            if solve(bo):
                return True # if there exists a solution for that pos

            # if no solution for that pos, revert that position to "0"
            # and try putting other numbers there
            bo[row][col] = 0

    # return false to say that that pos dont have any solution from 1 to 10 in current format
    return False



printBoard(board)
solve(board)
print(" ")
print(" ")
printBoard(board)

