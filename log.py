import threading
from datetime import datetime
import time

class Log:
    # val_ac_res = Valor de Acionamento do Resistor
    # val_ac_vent = Valor de Acionamento da Ventoinha
    def __init__(self):
        self.path = 'log.csv'
        self.running = False
        self.temp_interna = 0
        self.temp_externa = 0
        self.temp_ref = 0
        self.val_ac_res = 0
        self.val_ac_vent = 0
    
    def write(self):
          while(1):
            if(self.running == False):
              break
            log = open(self.path, 'a')
            log.write(f"{datetime.now()}, Temp. Interna = {self.temp_interna} C, Temp. Externa = {self.temp_externa} C, Temp. Referência = {self.temp_ref} C, Val. Acionamento do Resistor = {self.val_ac_res} %, Val. Acionamento da Ventoinha = {self.val_ac_vent} % \n")
            log.close()
            time.sleep(1)
  
    def start(self):
        self.running = True

        thread = threading.Thread(target=self.write, args=())
        thread.start()
    
    def atualiza_args(self, temp_interna: int, temp_externa: int, temp_ref: int, val_ac_res: int, val_ac_vent: int):
        self.temp_interna = temp_interna
        self.temp_externa = temp_externa
        self.temp_ref = temp_ref
        self.val_ac_res = val_ac_res
        self.val_ac_vent = val_ac_vent

    def stop(self):
        self.running = False