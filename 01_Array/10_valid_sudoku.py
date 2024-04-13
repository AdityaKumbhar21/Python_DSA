import collections


def isValidSudoku(board):
        cols = collections.defaultdict(set) # hashset for storing all the column values
        rows = collections.defaultdict(set) # hashset for storing all the row values 
        inner_vals = collections.defaultdict(set) #hashset for storing all the inner squares (r // 3 and c // 3)

        for r in range(9):
            for c in range(9):
                if(board[r][c] == "."):   # for checkinh empty values if there are then continue
                    continue
                # checking for duplicate value if any
                if (board[r][c] in rows[r] or
                   board[r][c] in cols[c] or
                   board[r][c] in inner_vals[(r//3,c//3)]):
                    return False
                
                #adding all the value in the hashmaps of hashset as value
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                inner_vals[(r//3,c//3)].add(board[r][c])
        
        return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))