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