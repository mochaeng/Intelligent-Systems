import csv
from knn import *
from normalize import *
from utils import z_score, min_max

base_dados = []
with open('./spam/BaseSpam.csv', newline='') as csvFile:
    spam_reader = csv.reader(csvFile, delimiter=',')
    _ = next(spam_reader)
    
    base_dados = [[int(row[1]), int(row[2]), int(row[3]), row[4]] for row in spam_reader if row]

base_normalizada_zscore, closures_zscore = normalizar_base(3, base_dados, z_score)
base_normalizada_minmax, closures_minmax = normalizar_base(3, base_dados, min_max)

descobrir = [100, 5, 0]
descobrir_zscore = normalizar_exemplo(descobrir, closures_zscore)
descobrir_minmax = normalizar_exemplo(descobrir, closures_minmax)

results_zscore = knn(base_normalizada_zscore, descobrir_zscore, 5)
results_min_max = knn(base_normalizada_minmax, descobrir_minmax, 5)


print_exemplo(results_zscore)
print()
print_exemplo(results_min_max)

