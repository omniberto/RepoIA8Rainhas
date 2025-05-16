class board():
    def __init__(self, m = 8, n = None):
        if not n:
            n = m
        self.col = m
        self.lin = n
    def printBoard(self, locals):
        indexLoc = 0
        queens = sorted(list(filter(lambda x: x[0] < self.col and x[1] < self.lin, locals)))
        print(queens)
        for i in range(self.col):
            for k in range(self.lin):
                if (indexLoc < len(queens) and queens[indexLoc] == (i, k)):
                    if ((i + k)%2):
                        print('♕', end=' ')
                    else:
                        print('♛', end=' ')
                    indexLoc += 1
                elif ((i + k)%2):
                    print('██',end='')
                else:
                    print('░░', end='')
            print()

if __name__ == '__main__':
    local = [(0, 0), (2, 6), (3, 2), (2, 7)]
    newBoard = board(8)
    newBoard.printBoard(local)
