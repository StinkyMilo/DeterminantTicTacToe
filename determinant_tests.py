import itertools as it
# In case it's not mentioned in the video, I used this to generate and print all possible terminal game states.
# This doesn't tell me much about strategy, though, since there are many different ways to make each of these states,
# depending on the order of play. I used this primarily to confirm that my explanation of 
# "a 1 in each column and each row and no identical rows" was sufficient for linear independence.
items = [1]*5+[0]*4
# Takes a list of 9 items and prints it as a 3x3 matrix
def print_as_matrix(item):
    print(item[0],item[1],item[2])
    print(item[3],item[4],item[5])
    print(item[6],item[7],item[8])

def determinant(board):
    # I know, very long line. Bad practice, but I'm tryna get this done quick.
    return (board[0]*board[4]*board[8]+board[1]*board[5]*board[6]+board[2]*board[3]*board[7])-(board[6]*board[4]*board[2]+board[7]*board[5]*board[0]+board[8]*board[3]*board[1])

def rows_equal(row1,row2):
    return row1[0]==row2[0] and row1[1]==row2[1] and row1[2]==row2[2]

# returns True if 1 in every column, 1 in every row, and no duplicate rows
def verify_board(board):
    if 1 not in board[0:3] or 1 not in board[3:6] or 1 not in board[6:9]:
        return False
    if 1 not in [board[0],board[3],board[6]] or 1 not in [board[1],board[4],board[7]] or 1 not in [board[2],board[5],board[8]]:
        return False
    if rows_equal(board[0:3],board[3:6]) or rows_equal(board[0:3],board[6:9]) or rows_equal(board[3:6],board[6:9]):
        return False
    return True

disproven = False
for i in it.permutations(items,9):
    # This will actually generate a bunch of identical boards, but it will reach all of them, and it proved me right.
    if not verify_board(i):
        continue
    det = determinant(i)
    if det == 0:
        print_as_matrix(i)
        print("You've been disproven! Counterexample is above.")
        disproven=True
        break
if not disproven:
    print("You were right! All boards had non-zero determinants.")
    