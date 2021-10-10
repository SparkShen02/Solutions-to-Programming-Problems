class Solution:
    def surroundedRegions(self,board):
        def find(a):
            if board[a]==-1:
                return True
            else:
                return False
        def to(a):
            board[a]=-1
        def rightOne(a,b):
            if b+1<column and board[a][b+1]=="O":
                board[a][b+1]=-1
        def leftOne(a,b):
            if b>0 and board[a][b-1]=="O":
                board[a][b-1]=-1
        def upOne(a,b):
            if a>0 and board[a-1][b]=="O":
                board[a-1][b]=-1
        def downOne(a,b):
            if a+1<row and board[a+1][b]=="O":
                board[a+1][b]=-1
        def ableRight(a,b):
            return b<column-1 and board[a][b+1]=="O"
        def ableLeft(a,b):
            return b>0 and board[a][b-1]=="O"
        def ableUp(a,b):
            return a>0 and board[a-1][b]=="O"
        def ableDown(a,b):
            return a<row-1 and board[a+1][b]=="O"
        def left(a,b):
            while ableLeft(a,b):
                leftOne(a,b)
                up(a,b-1)
                down(a,b-1)
                b-=1
        def right(a,b):
            while ableRight(a,b):
                rightOne(a,b)
                up(a,b+1)
                down(a,b+1)
                b+=1
        def up(a,b):
            while ableUp(a,b):
                upOne(a,b)
                left(a-1,b)
                right(a-1,b)
                a-=1
        def down(a,b):
            while ableDown(a,b):
                downOne(a,b)
                left(a+1,b)
                right(a+1,b)
                a+=1
        if len(board)==0:
            return
        column=len(board[0])
        row=len(board)
        for a in range(row):
            if board[a][0]=="O":##first column
                board[a][0]=-1
                x=a
                y=0
                while ableRight(x,y):
                    rightOne(x,y)
                    up(x,y+1)
                    down(x,y+1)
                    y+=1
            if board[a][column-1]=="O":##last column
                board[a][column-1]=-1
                x=a
                y=column-1
                while ableLeft(x,y):
                    leftOne(x,y)
                    up(x,y-1)
                    down(x,y-1)
                    y-=1
        for b in range(column):
            if board[0][b]=="O":##first row
                board[0][b]=-1
                x=0
                y=b
                while ableDown(x,y):
                    downOne(x,y)
                    left(x+1,y)
                    right(x+1,y)
                    x+=1
            if board[row-1][b]=="O":##last row
                board[row-1][b]=-1
                x=row-1
                y=b
                while ableUp(x,y):
                    upOne(x,y)
                    right(x-1,y)
                    left(x-1,y)
                    x-=1
        for a in range(row):
            for b in range(column):
                if board[a][b]=="O":
                    board[a][b]="X"
                if board[a][b]==-1:
                    board[a][b]="O"
        return board