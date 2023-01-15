import csv
import valores
import threading
import time

class Curva:
    def __init__(self):
        self.tempo = []
        self.temperatura = []
        self.running = False
        self.timer = 0
        self.idx = 0
    
    def leitura_arquivo(self):
        try:
          with open('curva_reflow.csv', 'r') as file:
              reader = csv.DictReader(file)
      
              for row in reader:
                self.tempo.append(int(row['Tempo (s)']))
                self.temperatura.append(int(row[' Temperatura']))
        except:
            print("[ERRO] Arquivo configuração da curva pré-definida (curva_reflow.csv) não encontrado.")
    
    def run(self):
          while(1):
            if(self.running == False):
              self.timer = 0
              self.idx = 0
              break
            #verifica se é o tempo determinado no arquivo para definir temperatura
            if(self.timer == self.tempo[self.idx]):
              valores.temp_referencia = self.temperatura[self.idx]
              self.idx += 1
            time.sleep(1)
            self.timer += 1
  
    def start(self):
        self.running = True
        thread = threading.Thread(target=self.run, args=())
        thread.start()

    def stop(self):
        self.running = False

curva = Curva()
curva.leitura_arquivo()
