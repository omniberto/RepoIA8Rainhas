class tabuleiro():
    def __init__(self, colunas = 8, linhas = None):
        if not linhas:
            linhas = colunas
        self.colunas = colunas
        self.linhas = linhas
    def printBoard(self, locais):
        index_local = 0
        posicao_rainhas = sorted(list(filter(lambda x: x[0] < self.colunas and x[1] < self.linhas, locais)))
        for i in range(self.colunas):
            for k in range(self.linhas):
                if (index_local < len(posicao_rainhas) and posicao_rainhas[index_local] == (i, k)):
                    if ((i + k)%2):
                        print('♕', end = ' ')
                    else:
                        print('♛', end = ' ')
                    index_local += 1
                elif ((i + k)%2):
                    print('██', end = '')
                else:
                    print('░░', end = '')
            print()

if __name__ == '__main__':
    local = [(0, 0), (2, 6), (3, 2), (2, 7)]
    newBoard = tabuleiro(8)
    newBoard.printBoard(local)
