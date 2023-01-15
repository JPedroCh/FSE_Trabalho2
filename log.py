import threading
from datetime import datetime
import time
import valores

class Log:
    # val_ac_res = Valor de Acionamento do Resistor
    # val_ac_vent = Valor de Acionamento da Ventoinha
    def __init__(self):
        self.path = 'log.csv'
        self.running = False
    
    def write(self):
          while(1):
            if(self.running == False):
              break
            log = open(self.path, 'a')
            log.write(f"{datetime.now()}, Temp. Interna = {valores.temp_interna} C, Temp. Externa = {valores.temperatura_ambiente} C, Temp. Referência = {valores.temp_referencia} C, Val. Acionamento do Resistor = {valores.sinal_controle} %, Val. Acionamento da Ventoinha = {valores.sinal_controle} % \n")
            log.close()
            time.sleep(1)
  
    def start(self):
        self.running = True

        thread = threading.Thread(target=self.write, args=())
        thread.start()

    def stop(self):
        self.running = False

log = Log()