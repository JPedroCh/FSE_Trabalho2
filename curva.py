import csv

class Curva:
    def __init__(self):
        self.tempo = []
        self.temperatura = []
    
    def leitura_arquivo(self):
        try:
          with open('curva_reflow.csv', 'r') as file:
              reader = csv.DictReader(file)
      
              for row in reader:
                self.tempo.append(int(row['Tempo (s)']))
                self.temperatura.append(int(row[' Temperatura']))
        except:
            print("[ERRO] Arquivo configuração da curva pré-definida (curva_reflow.csv) não encontrado.")