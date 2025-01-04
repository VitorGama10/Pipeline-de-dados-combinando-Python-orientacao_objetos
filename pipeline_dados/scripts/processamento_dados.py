import json
import csv

class  Dados: # A classe Dados é criada para representar um conjunto de dados.
    def __init__(self, path, tipo_dados):
        # aqui são os atributos
        self.path = path 
        self.tipo_dados = tipo_dados 
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()
        self.qtd_linhas = self.size_data()
        
        
 # Aqui serão os metodos              
# Leitura dos json
         
    def leitura_json(self):
        
        dados_json = []
        with open(self.path, 'r') as file: 
            dados_json = json.load(file)

        return dados_json

# Lendo o arquivo csv

    def leitura_csv(self):
        
        dados_csv = [] 
        with open(self.path, 'r') as file: 
            spamreader = csv.DictReader(file, delimiter= ',') 
            for row in spamreader: 
                dados_csv.append(row)
                
        return dados_csv

# Lendo os dois dados 

    def  leitura_dados(self):
        dados = []
        
        if self.tipo_dados == 'csv':
            dados = self.leitura_csv()
            
        elif self.tipo_dados == 'json':
            dados = self.leitura_json()
            
        elif self.tipo_dados == 'list':
            dados = self.path
            self.path = 'lista em memoria'
        
        return dados
    
    def get_columns(self): # agora virou um metodo recebe o self
        return list(self.dados[-1].keys())
    
    def rename_columns(self, key_mapping):
        
        new_dados  = []

        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping[old_key]] = value
            new_dados.append(dict_temp)
            
        self.dados =  new_dados # corregiu os nomes 
        self.nome_colunas =  self.get_columns() # atualiza o nome das colunas
        
        
    def size_data(self):
        return len(self.dados) 
    
    def join(dadosA, dadosB):
        
        combined_list = []
        combined_list.extend(dadosA.dados)
        combined_list.extend(dadosB.dados)
        
        return Dados(combined_list, 'list')
    
    # Load e Save
    
    def transformacao_dados_tabela(self): # nosso classe ja sabe o nome das coluna e os dados 
        
        dados_combinados_tabela = [self.nome_colunas] 

        for row in self.dados: # vai percorrer cada uma das linhas
            linha = [] 

            for coluna in self.nome_colunas:   # pega o nome das colunas
                linha.append(row.get(coluna, 'Indisponivel')) # vai tentar pegar caso n encontre vai colocar como indisponivel
            dados_combinados_tabela.append(linha)        
        
        return dados_combinados_tabela
    
    def salvando_dados(self, path):
        
        dados_combindados_tabela = self.transformacao_dados_tabela()
        
        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(dados_combindados_tabela)
            