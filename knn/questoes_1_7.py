from utils import z_score, min_max

values_temp = [20, 25, 15, 30]
values_imoveis = [100.000, 200.000, 150.000, 300.000]
values_height = [160, 170, 155, 180]
values_prova = [70, 80, 60, 90]
values_milisegundos = [120, 150, 130, 200]
values_segundos = [20, 25, 18, 30, 22]

print(f'Temperaturas normalizadas: {min_max(values_temp)[0]}')
print(f'Valor imóvel normalizados: {min_max(values_imoveis)[0]}')
print(f'Alturas normalizadas: {min_max(values_height)[0]}')
print(f'Pontuaçao prova: {z_score(values_prova)[0]}')
print(f'Valores milisegundos: {z_score(values_milisegundos)[0]}')
print(f'Valores segundos (z-score): {z_score(values_segundos)[0]}')
print(f'Valores segundos (min-max): {min_max(values_segundos)[0]}')
 
