import random

def rand(r):
    return random.randrange(r)

def fill_random_board(diff, count = False):
# if supplied count = True, 'diff' much random numbers will be filled on board
    global board
    global fill_count
    if diff == 1:
        fill_count = 30
    elif diff == 2:
        fill_count = 20
    elif diff == 3:
        fill_count = 15
    if count:
        fill_count = diff
    for _ in range(fill_count):
        # this is how it workd
        # generate random a,b = pos
        # find empty block (i.e board[a][b] == 0), if a,b is already filled
        # move along x and y alternatively, while also considering 0 comes after 8 (round)
        a,b = [rand(9) for _ in range(2)]
        flag = True
#        print_board()
        while board[a][b] != 0:
            if flag:
                a = (a+1)%9
                flag = False
            else:
                b = (b+1)%9
                flag = True
        newnum = rand(10)
        print(a,b)
# is_legal_move(a,b,newnum) func will check if placing newnum at position a,b, is a valid move
# generate newnum till a valid move is found
        while not is_legal_move(a,b,newnum):
            newnum = (newnum+1)%9 + 1
        board[a][b] = newnum
        fill_count += 1

def is_legal_move(a,b,num):
    # Check if already in row
    if num in board[a]:
        return False
    # Check if in column
    for i in range(9):
        if num == board[i][b]:
            return False
    # Check if in mini-board
    i,j = mini_block_pos(a,b)
    i = (i)*3 
    j = (j)*3 
    for k in range(3):
        if num in board[i+k][j:j+3]:
            return False
    return True

def mini_block_pos(a,b):
    i = a//3
    j = b//3
    return i,j

def print_board():
    print('-------------------------')
    for i in range(3):
        for j in range(3):
            print('| ',end='')
            for k in range(3):
                for l in range(3):
                    if board[i*3+j][k*3+l] == 0:
                        print(' ',end =' ')
                    else:
                        print(board[i*3+j][k*3+l],end=' ')
                print('| ',end='')
            print()
        print('-------------------------')

def solve_board():
    global fill_count
    # step 1 is to find pos where only 1 number can be filled, if no such position is found it will return false
    flag = False
    for i in range(9):
        for j in range(9):
            if not board[i][j]:
            # this block will be exectued if board at i,j pos is empty (i.e 0)
            # find all valid moves for this pos
                legal_move = find_legal_moves(i,j)
                if len(legal_move) == 1:
                    board[i][j] = legal_move[0]
    #                print_board()
                    fill_count += 1
                    flag = True
    return flag

def find_legal_moves(a,b):
# this function will return list of all possible solution for i,j pos
# it will return empty list, in case i,j position is already filled
    if board[a][b]:
        return []
    else:
        li = []
        for i in range(1,10):
            if is_legal_move(a,b,i):
                li.append(i)
        return li


# here starts the main block

# create empty board
board = [[0 for _ in range(9)] for _ in range(9)]

diff = int(input("Enter difficulty level (1,2,3) - "))

fill_count = 0
# fill_random_board(diff)

print_board()

while fill_count < 82:
    if ( solve_board() ):
        continue
    else:
        print('solve_board returned false')
        fill_random_board(1, True)
        print_board()
       
