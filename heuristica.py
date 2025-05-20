def heuristica_agoritmo_guloso(n = 8): # Função usando o algorimo guloso para resolver o problema das rainhas
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