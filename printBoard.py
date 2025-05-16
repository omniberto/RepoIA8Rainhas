class board():
    def __init__(self, local = list, m = 8, n = None):
        if not n:
            n = m
        self.local = local
        self.local.sort()
        self.col = m
        self.lin = n
    def printBoard(self):
        indexLoc = 0
        for i in range(self.col):
            for k in range(self.lin):
                if (indexLoc < len(self.local) and self.local[indexLoc] == (i, k)):
                    print('♛ ', end='')
                    indexLoc += 1
                elif ((i + k)%2):
                    print('██',end='')
                else:
                    print('░░', end='')
            print()
            
if __name__ == '__main__':
    local = [(0, 0), (7, 7), (2, 3), (3, 2), (8, 8)]
    newBoard = board(local, 8, 8)
    newBoard.printBoard()
