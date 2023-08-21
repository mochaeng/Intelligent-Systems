from math import log2
import pandas as pd


class Node:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.sons: list[Node] = []
        self.entropy: float
        self.count: int
        self.probability: float


class DecisionTree:
    def __init__(self, data_frame: pd.pandas.DataFrame, target_name, decision_column: str) -> None:
        self.root: Node | None = None
        self.data_frame = data_frame
        self.target_name = target_name
        self.decision_node: dict = {}
        self.columns = data_frame.columns.values.tolist()[1:-1]
        self.decision_column = decision_column

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

    def make_level(self, columns, column_to_remove=None, value=None):
        print()
        print('#####################')
        print('Criando nó')
        
        if column_to_remove != None and value != None:
            columns = columns[columns[column_to_remove] == value]
            columns = columns.drop(column_to_remove, axis=1)

        print(columns)
    
        parent = self.create_node(columns[self.target_name], self.target_name)
        print('ich bin der Vater')
        print(parent)
        gains = []
        for column in columns:
            if column == self.target_name:
                continue

            unique_values = columns[column].unique()
            weight_summation = 0
            for unique_value in unique_values:
                print()
                print(unique_value)
                partialy_column = columns[columns[column] == unique_value][self.target_name]
                name = column + '|' + str(unique_value)
                node = self.create_node(partialy_column, name)
                print(node)
                weight_summation += (node['total'] / parent['total']) * node['entropy']

            gain = parent['entropy'] - weight_summation
            gains.append((column, gain))
        
        gains = sorted(gains)
        print()
        print(f'Os ganhos para este nível são: {gains}')

        return columns
        


target_name = 'Tipo de Transporte'

data_frame = pd.read_csv("./data/table_aula.csv")
y = data_frame[target_name]
dt = DecisionTree(data_frame, target_name, target_name)
print(data_frame.columns)

# dt.make_level(data_frame[['Genero', 'Carro Proprio?', 'Custo por km', 'Tipo de Transporte']])
# dt.make_level(data_frame[['Genero', 'Carro Proprio?', 'Custo por km', 'Tipo de Transporte']], column_to_remove='Custo por km', value='Barato')
# dt.make_level(data_frame[['Genero', 'Carro Proprio?', 'Tipo de Transporte']], column_to_remove='Genero', value='Feminino')

col = dt.make_level(data_frame[['Genero', 'Carro Proprio?', 'Custo por km', 'Tipo de Transporte']])
col = dt.make_level(col, column_to_remove='Custo por km', value='Barato')
col = dt.make_level(col, column_to_remove='Genero', value='Feminino')

