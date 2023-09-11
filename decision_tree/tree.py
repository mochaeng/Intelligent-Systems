from math import log2
from numpy import sort
import pandas as pd

class Node:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.children: list[Node] = []
        self.entropy: float
        self.count: int
        self.probability: float


class DecisionTree:
    def __init__(self, data_frame: pd.pandas.DataFrame, target_name, decision_column: str, numeric_columns=[]) -> None:
        self.root: Node | None = None
        self.data_frame = data_frame
        self.target_name = target_name
        self.decision_node: dict = {}
        self.columns = data_frame.columns.values.tolist()[1:-1]
        self.decision_column = decision_column
        self.numeric_columns = numeric_columns
    

        self.create_decision_node(data_frame[target_name], self.decision_column)

    def add_parent(self, parent: Node):
        self.root = parent

    def create_node(self, column, name):
        node = {}
        node['class_name'] = name
        node['items'] = {}
            
        for item in column:
            node['items'][item] = {'count': 0}
        
        total = 0
        for item in column:
            node['items'][item]['count'] += 1
            total += 1

        node['total'] = total

        for key in node['items']:
            node['items'][key]['probability'] = node['items'][key]['count'] / node['total']
        
        node['entropy'] = self.calc_entropy(node)

        return node

    def create_decision_node(self, column, name):
        self.decision_node = self.create_node(column, name)
    
    def calc_entropy(self, node):
        entropy = 0
        for key in node['items']:
            prob = node['items'][key]['probability']
            entropy += -prob * log2(prob)

        return entropy
    
    
    def calc_numeric_features(self, columns, column_to_check, target):
        sorted_values = sort(columns[column_to_check])
        parent = self.create_node(columns[target], 'Parent|' + target)

        print()
        print('#' * 30)
        print('Cálculo de valor numérico')
        print(parent)
        all_gains = []

        for value in sorted_values:
            left_column = columns[columns[column_to_check] <= value]
            right_column = columns[columns[column_to_check] > value]
            
            left_node = self.create_node(left_column[target], str(value) + '|left')
            right_node = self.create_node(right_column[target], str(value) + '|right')
            
            nodes = [left_node, right_node]
            summation = 0
            for node in nodes:
                summation += (node['total'] / parent['total']) * node['entropy']
            gain = parent['entropy'] - summation

            all_gains.append((value, gain))

            print()
            print(left_node)
            print(right_node)
            print(f'ganho: {gain}')
        
        all_gains.sort(key=lambda x: x[1])
        greater = all_gains[-1][0]

        filtered = filter(lambda value: value <= greater, all_gains)

        print(f'\ntodos os ganhos: {all_gains}')
        print(f'valores filtrados: {list(filtered)}')
    

    def make_level(self, columns, column_to_remove=None, values=[], filter=False):
        print()
        print('#' * 50)
        print('Criando nó')
        
        if column_to_remove != None and len(values) > 0:
            for value in values:
                if filter:
                    columns = columns[columns[column_to_remove] != value]
                else:
                    columns = columns[columns[column_to_remove] == value]

            columns = columns.drop(column_to_remove, axis=1)

        print(columns)
        print()
    
        parent = self.create_node(columns[self.target_name], self.target_name)
        print('Nó pai: ')
        print(parent)
        gains = []
        for column in columns:
            if column == self.target_name:
                continue
            
            if column in self.numeric_columns:
                dt.calc_numeric_features(columns, column, self.target_name)

                

            unique_values = columns[column].unique()
    

            print(f'\nunique values: {unique_values}')
            weight_summation = 0
            weight_calc = []
            print(f'\n$$$Coluna: {column}')
            for unique_value in unique_values:
                print(f'\n>>> Valor: {unique_value}')
                partialy_column = columns[columns[column] == unique_value][self.target_name]
                name = column + '|' + str(unique_value)
                node = self.create_node(partialy_column, name)
                print(node)
                
                weight = node['total'] / parent['total']
                calc_str = f"({node['total']} / {parent['total']}) * {node['entropy']}"

                weight_summation += weight * node['entropy']
                weight_calc.append(calc_str)
                weight_calc.append('+')

            gain = parent['entropy'] - weight_summation
            gains.append((column, gain))

            print(f'Cálculo do ganho: {column}: {weight_calc}')
        
        gains.sort(key=lambda x: x[1])

        gains = sorted(gains)
        print()
        print(f'Os ganhos para este nível são: {gains}')

        return columns
        


target_name = 'Alvo'
data_frame = pd.read_csv("./data/questao_02.csv")
# y = data_frame[target_name]

dt = DecisionTree(data_frame, target_name, target_name, numeric_columns=['Idade', 'Renda_Mensal', 'Histórico_de_Compras'])

d = data_frame[['Idade', 'Renda_Mensal', 'Histórico_de_Compras' , 'Alvo']]

col = dt.make_level(d)

# dt.calc_numeric_features(d, 'Renda_Mensal', 'Alvo')


# col = dt.make_level(d)
# col = dt.make_level(col, column_to_remove='Idade', values=[20, 22], filter=True)

# dt.calc_numeric_features(col, 'Renda_Mensal', 'Alvo')

# col = dt.make_level(col, column_to_remove='Renda_Mensal', values=["3.000,00", "3.500,00", "4.000,00"], filter=True)


# col = dt.make_level(col, column_to_remove='Tem_Cauda', value='Sim')
# col = dt.make_level(col, column_to_remove='Tipo_Alimentacao', value='Onívoro')
# col = dt.make_level(col, column_to_remove='Tipo_Alimentacao', value='Onívoro')


