from random import choice

def backtracking(n = 8) -> list: #Incio da função utilizando backtracking, a quantidade de rainhas será 8 por padrão para resolução do problema das 8 rainhas
    colunas = set() # Set contendo as colunas ocupadas
    diagonais_positivas = set() # Set contendo as diagonais positivas ocupadas
    diagonais_negativas = set() # Set contendo as diagonais negativas ocupadas
 
    resultados = [] # Lista de resultados
    casos = [] # Lista de casos encontrados

    def backtrack(linha): # Função de backtracking

        if linha == n: # Se chegou na ultima rainha
            resultados.append(casos.copy()) # Adiciona como um resultado válido
            return
        
        for coluna in range(n): # Verifica as colunas
            if coluna in colunas or (linha + coluna) in diagonais_positivas or (linha - coluna) in diagonais_negativas: # Se não for uma coluna válida
                continue # Vai pra próxima iteração

            colunas.add(coluna) # Adiciona a coluna na lista de colunas
            diagonais_positivas.add(linha + coluna) # Adiciona a diagonal positiva na lista
            diagonais_negativas.add(linha - coluna) # Adiciona a diagonal negativa na lista
            casos.append((linha, coluna)) # Adiciona a posição na lista de casos

            backtrack(linha + 1) # Verifica para a próxima linha

            colunas.remove(coluna) # Remove a coluna da lista de colunas
            diagonais_positivas.remove(linha + coluna) # Remove a diagonal positiva da lista
            diagonais_negativas.remove(linha - coluna) # Remove a diagonal negativa da lista
            casos.remove((linha, coluna)) # Remove a posição da lista de casos
    
    backtrack(0) # Inicia a chamada do backtracking
    return resultados # Retorna a lista de resultados

def heuristica_agoritmo_guloso(n = 8): # Função usando o algorimo guloso para resolver o problema das rainhas, a quantidade de rainhas será 8 por padrão para resolução do problema das 8 rainhas
    resultados = [] # Lista com as possíveis soluções

    def conflitos(estado): # Função para verficar o número de conflitos
        num_conflitos = 0 # Inicialmente sem nenhum conflito
        linha = len(estado) # Analisando a quantidade de linhas já obtidas
        for i in range(linha):
            for j in range(i + 1, linha):
                if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j): # Analisando se exite conflito nas colunas ou diagonais
                    num_conflitos += 1 # Se conflitou, adiciona ao número de conflitos
        return num_conflitos # Retorna o número de conflitos

    def gerar_sucessores(estado): # Função para gerar sucessores
        linha = len(estado) # Verifica a quantidade de posições
        if linha >= n: # Se já estamos an última posição
            return [] # Não temos mais sucessores
        sucessores = [] # Se não, inicia a lista de sucessores
        for coluna in range(n):
            novo_estado = estado + [coluna] # Adiciona a coluna atual na lista de colunas do estado
            sucessores.append(novo_estado) # Adiciona o novo estado à lista de sucessores
        return sucessores # Devolve a lista de sucessores

    def algortimo_guloso(posicao_inicial = 0): # Função pro algortimo guloso
        fronteira = [] # Iniciando a fronteira
        estado_inicial = [posicao_inicial] # Criando o estado inicial usando a posição inicial
        fronteira.append([0, estado_inicial]) # Adiciona o estado inicial à fronteira

        while fronteira: # Enquanto tiver algum estado na fronteira

            heuristica, estado = fronteira.pop(0) # Pega o valor da função heurística e o estado atual
            if len(estado) == n and heuristica == 0: # Verifica se o estado contem uma solução com heurística = 0 e possuir um posicionamento para todas as rainhas
                resolucoes = [estado] # Criamos o uma lista de resoluções
                while (fronteira[0][0] == 0 and len(fronteira[0][1]) == n): # Verificamos se existe mais alguma resposta 
                        _, resolucao = fronteira.pop(0) # Se tiver, tiramos da lista
                        resolucoes.append(resolucao) # Adicionamos na lista de resoluções

                for resolucao in resolucoes: # Pegaremos cada solução encontrada
                    resolucao_formatada = list(enumerate(resolucao)) # Formataremos
                    resultados.append(resolucao_formatada) # Adicionaremos à lista de resultados
                
                return # Retornaremos para terminar a execução do algoritmo
            
            else: # Se ainda não tivermos resposta
                for sucessor in gerar_sucessores(estado): # Geraremos os sucessores
                    heuristica = conflitos(sucessor) # Calcuaremos sua heurística com o número de conflitos que possui
                    fronteira.append((heuristica, sucessor)) # Adicionaremos à fronteira
                fronteira.sort(key = lambda x: x[0]) # Reorganizaremos a lista para ordenar com base na heurística

        return None # Não retornaremos n
    
    for i in range(n): # Para cada posição possivel
        algortimo_guloso(i) # Realizaremos uma busca para ele

    return resultados # Devolveremos as resoluções encontradas

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

if __name__ == "__main__":
    tabuleiro_backtracking = tabuleiro()
    tabuleiro_ganancioso = tabuleiro()
    print()

    # Solução Backtracking
    solucoes_backtracking = backtracking()
    exemplo_solucao_backtracking = choice(solucoes_backtracking)
    print("Solução usando backtracking:")
    print(exemplo_solucao_backtracking)
    print()

    # Solução Ganancioso
    solucoes_ganancioso = heuristica_agoritmo_guloso()
    exemplo_solucao_ganancioso = choice(solucoes_ganancioso)
    print("Solução usando algoritmo ganacioso:")
    print(exemplo_solucao_ganancioso)
    print()

    # Visualização Tabuleiros
    tabuleiro_backtracking.imprimir_tabuleiro(exemplo_solucao_backtracking)
    print()
    tabuleiro_ganancioso.imprimir_tabuleiro(exemplo_solucao_ganancioso)
    print()

    # Comparação de Soluções
    print("Quantidade de soluções encontradas pelo backtracking:", len(solucoes_backtracking))
    print("Quantidade de soluções encontradas pelo algoritmo ganacioso:", len(solucoes_ganancioso))
    if(solucoes_backtracking == solucoes_ganancioso):
        print("Possuem as mesmas soluções!")