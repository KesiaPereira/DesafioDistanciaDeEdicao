def distancia_edicao_gulosa(a, b):
    m = len(a)
    n = len(b)
    distancia = 0
    index_a = 0
    index_b = 0
    operacoes = []

    while index_a < m and index_b < n:
        if a[index_a] != b[index_b]:
            # Calcula o custo de cada operação
            custo_insercao = 1 if (index_a + 1 < m and a[index_a + 1] == b[index_b]) else float('inf')
            custo_remocao = 1 if (index_b + 1 < n and a[index_a] == b[index_b + 1]) else float('inf')
            custo_substituicao = 1

            # Escolhe a operação que minimiza a distância
            if custo_insercao <= custo_remocao and custo_insercao <= custo_substituicao:
                operacoes.append(f"Inserir '{b[index_b]}'")
                index_b += 1
            elif custo_remocao <= custo_insercao and custo_remocao <= custo_substituicao:
                operacoes.append(f"Remover '{a[index_a]}'")
                index_a += 1
            else:
                operacoes.append(f"Substituir '{a[index_a]}' por '{b[index_b]}'")
                index_a += 1
                index_b += 1

            distancia += 1
        else:
            operacoes.append(f"Manter '{a[index_a]}'")
            index_a += 1
            index_b += 1

    while index_a < m:
        distancia += 1
        operacoes.append(f"Remover '{a[index_a]}'")
        index_a += 1

    while index_b < n:
        distancia += 1
        operacoes.append(f"Inserir '{b[index_b]}'")
        index_b += 1

    print("Passo-a-passo das operações:")
    for i, op in enumerate(operacoes, start=1):
        print(f"Passo {i}: {op}")

    return distancia

# Exemplos
print("Distância de edição:", distancia_edicao_gulosa("asar", "casa"))       
print("Distância de edição:", distancia_edicao_gulosa("inserir", "inserção"))
