def print_exemplo(values):
    for value in values:
        print(value)

def distancia_euclidiana(d1, d2):
    if len(d1) != len(d2):
        raise Exception('impossivel encontrar distância')        

    soma = 0
    for idx, _ in enumerate(d1):
        soma += (d1[idx] - d2[idx]) ** 2
    
    return soma ** (1/2)

def knn(base_dados, descobrir, k=0):
    results = []

    for example in base_dados:
        distancia = distancia_euclidiana(descobrir, example[:-1])
        results.append((distancia, example[-1]))

    results_sorted = sorted(results)

    return results_sorted[:k]


