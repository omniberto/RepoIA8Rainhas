class tabuleiro():
    def __init__(self, colunas = 8, linhas = None): # O tabuleiro será 8x8 por padrão para resolução do problema das 8 rainhas
        if not linhas: # Se as linhas não foram determinadas
            linhas = colunas # Utilizar a mesma quantidade de colunas
        self.colunas = colunas # Adiciona a quantidade de colunas
        self.linhas = linhas # Adiciona a quantidade de colunas

    def imprimir_tabuleiro(self, locais, modo = True): # Função para visualizar o tabuleiro
        index_local = 0 # Index utilizado para percorrer a lista de posições das rainhas
        posicao_rainhas = sorted(list(filter(lambda x: x[0] < self.colunas and x[1] < self.linhas, locais))) # Organizando as rainhas e removendo quaisquer rainhas que não possam ser representadas no tabuleiro
        index_maximo = len(posicao_rainhas) # Index máximo da lista de rainhas
        if modo: # Modo controla como o tabuleiro é visualizado, se modo for False, ele mostrará um tabuleiro mais estilizado, porém com incerteza sobre sua visibilidade em todos os sistemas
            for i in range(self.colunas): # Navegando pelas colunas
                for k in range(self.linhas): # Navegando pelas linhas
                    if (index_local < index_maximo and posicao_rainhas[index_local] == (i, k)): # Se existir rainhas a serem visualizadas na posição atual
                        print('Q', end = ' ') # Mostrará um Q para representar a rainha
                        index_local += 1 # Aumentara o Index em 1
                    else:
                        print('.', end = ' ') # Mostrará um . para indicar um espaço vazio
                print() # Imprime uma quebra de linha
        else: # Se Modo for False
            for i in range(self.colunas):
                for k in range(self.linhas):
                    if (index_local < len(posicao_rainhas) and posicao_rainhas[index_local] == (i, k)):
                        if ((i + k) % 2): # Verificar qual seria a cor do espaço
                            print('♕', end = ' ') # Imprime uma rainha preta onde seria um espaço branco
                        else:
                            print('♛', end = ' ') # Imprime uma rainha branca onde seria um espaço preto
                        index_local += 1
                    elif ((i + k) % 2): # Verificar qual seria a cor do espaço
                        print('██', end = '') # Imprime o que seria correspondente à um espaço branco
                    else:
                        print('░░', end = '') # Imprime o que seria correspondente à um espaço preto
                print()