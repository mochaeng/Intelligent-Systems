from copy import deepcopy

def array_to_csv(base_dados):
    string = ''
    for linha in base_dados:
        for value in linha:
            string += str(value) + ','
        string = string[:-1]
        string += '\n'
    return string

def normalizar_base(num_colunas, base_dados, algo_norm):
    closures = []
    new_base_dados = deepcopy(base_dados)

    for i in range(0, num_colunas):
        coluna = []
        for example in new_base_dados:
            coluna.append(example[i])
        
        coluna_normalizada, closure  = algo_norm(coluna)
        closures.append(closure)
        
        for idx in range(0, len(new_base_dados)):
            new_base_dados[idx][i] = coluna_normalizada[idx]
    
    return new_base_dados, closures

def normalizar_exemplo(example, closures):
    new_example = deepcopy(example)

    for idx, value in enumerate(new_example):
        new_example[idx] = closures[idx](value)

    return new_example

