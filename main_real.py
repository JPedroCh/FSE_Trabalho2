import modbus
import sensor
import pwm
from commands import comandos
import time
from pid import pid
from log import log
import valores
from datetime import datetime
from curva import curva

def controle_temperatura():
  sensor.leitura_sensor()
  if(valores.modo_controle_temperatura == 0):
    curva.stop()
    modbus.envia(comandos.ask_reference_temp())
  modbus.envia(comandos.ask_intern_temp())
  modbus.ler()
  pid.pid_controle()
  pwm.atualiza_duty_cycle()
  modbus.envia(comandos.send_control_signal())
  modbus.envia(comandos.send_reference_signal())
  modbus.envia(comandos.send_external_temp())




def main():

  modbus.init()
  sensor.init()
  pwm.init()

  # loop de gerar log
  log.start()

  #zerar comandos 
  modbus.envia(comandos.send_system_status(0))
  modbus.envia(comandos.send_func_status(0))
  modbus.envia(comandos.send_control_mode(0))
  
  time.sleep(0.2)

  modbus.ler()
  

  #loop principal
  try:
    while(1):
      modbus.envia(comandos.read_user_command()) 
      modbus.ler()
      controle_temperatura()
      # mudar para 0.5 depois
      time.sleep(1)
      print(datetime.now())


      
  
  except KeyboardInterrupt:
    log.stop()
    curva.stop()
    pwm.finalizar_pwm()

    modbus.envia(comandos.send_func_status(0))
    modbus.envia(comandos.send_system_status(0))

    time.sleep(0.2)
    modbus.ler()
    print("finalizando")

main()