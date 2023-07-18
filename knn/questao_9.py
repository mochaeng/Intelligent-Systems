import csv
from knn import *
from normalize import *
from utils import z_score, min_max


base_dados = []
with open('./transacao/baseTransacaoEletronica.csv', newline='') as csvFile:
    reader = csv.reader(csvFile, delimiter=',')
    _ = next(reader)
    
    base_dados = [[float(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]),
                   int(row[6]), int(row[7]), row[8]] for row in reader if row]


base_normalizada_zscore, closures_zscore = normalizar_base(7, base_dados, z_score)
base_normalizada_minmax, closures_minmax = normalizar_base(7, base_dados, min_max)

descobrir = [2500, 0, 0, 1, 1, 0, 2]
descobrir_zscore = normalizar_exemplo(descobrir, closures_zscore)
descobrir_minmax = normalizar_exemplo(descobrir, closures_minmax)


results_zscore = knn(base_normalizada_zscore, descobrir_zscore, 5)
results_min_max = knn(base_normalizada_minmax, descobrir_minmax, 5)

print('KNN (K=5, Z-Score)')
print_exemplo(results_zscore)
print()
print('KNN (K=5, MinMax)')
print_exemplo(results_min_max)

