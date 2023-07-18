def min_max(values):
    min_ = min(values)
    max_ = max(values)

    new_values = []
    for value in values:
        result = (value - min_) / (max_ - min_)
        new_values.append(result)

    closure = lambda x: (x - min_) / (max_ - min_)

    return new_values, closure 

def z_score(values):

    def media(values):
        return sum(values) / len(values)
    
    def desvio(values):
        soma = 0
        for value in values:
            soma += (value - avg) ** 2
        result = soma / (len(values) - 1)
        return result ** (1/2)
    
    avg = media(values)
    std = desvio(values)
    
    new_values = []
    for value in values:
        norm = (value - avg) / std
        new_values.append(norm)
    
    closure = lambda x: (x - avg) / std

    return new_values, closure

