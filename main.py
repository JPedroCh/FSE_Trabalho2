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
import menu


# acontece a cada 1s e só roda se estiver em funcionamento
def controle_temperatura():
  #lê temperatura ambiente e envia
  sensor.leitura_sensor()
  time.sleep(0.1)
  modbus.envia(comandos.send_external_temp())

  # de acordo com o modo de controle de temperatura:
  # solicita ou envia a temperatura de referência
  if(valores.modo_controle_temperatura == 0):
    curva.stop()
    modbus.envia(comandos.ask_reference_temp())
  else:
    modbus.envia(comandos.send_reference_signal())
  time.sleep(0.1)
  modbus.ler()

  # lê a temperatura interna
  modbus.envia(comandos.ask_intern_temp())
  time.sleep(0.1)
  modbus.ler()

  # calcula o sinal de controle e atualiza pwm
  pid.pid_controle()
  pwm.atualiza_duty_cycle()

  # envia sinal de controle
  modbus.envia(comandos.send_control_signal())
  time.sleep(0.1)
  modbus.ler()


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

  menu.config_params()

  menu.modo()
  

  #loop principal
  try:
    while(1):
      # leitura de comandos a cada 0.5s
      modbus.envia(comandos.read_user_command()) 
      time.sleep(0.1)
      modbus.ler()

      if(valores.estado_sistema == 1 and valores.estado_funcionamento == 1):
        controle_temperatura()
      else:
        time.sleep(0.4)

      modbus.envia(comandos.read_user_command()) 
      time.sleep(0.1)
      modbus.ler()

      time.sleep(0.4)


      
  
  except KeyboardInterrupt:
    print("\n[INFO] Finalizando...")
    log.stop()
    curva.stop()
    pwm.finalizar_pwm()

    modbus.envia(comandos.send_func_status(0))
    modbus.envia(comandos.send_system_status(0))

    time.sleep(0.2)
    modbus.ler()
    print("\n[INFO] Finalizado.")

main()