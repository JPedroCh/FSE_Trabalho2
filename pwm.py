import RPi.GPIO as gpio
from time import sleep
import valores

pwm_resistor = 0
pwm_ventoinha = 0

def init():
  global pwm_resistor, pwm_ventoinha
  # Configurações gerais 
  gpio.setwarnings(False)
  gpio.setmode(gpio.BCM)

  # resistor
  gpio.setup(23,gpio.OUT)

  #ventoinha
  gpio.setup(24,gpio.OUT)

  pwm_resistor = gpio.PWM(23, 500)
  pwm_resistor.start(0)

  pwm_ventoinha = gpio.PWM(24, 500)
  pwm_ventoinha.start(100)
  valores.acionamento_ventoinha = 100

def atualiza_duty_cycle():
    if(valores.sinal_controle <= 0 and valores.sinal_controle > -41):
        valores.acionamento_resistor = 0
        pwm_resistor.ChangeDutyCycle(0)
        valores.acionamento_ventoinha = 40
        pwm_ventoinha.ChangeDutyCycle(40)
    elif(valores.sinal_controle < -40):
        valores.acionamento_resistor = 0
        pwm_resistor.ChangeDutyCycle(0)
        if(valores.sinal_controle < -100):
          valores.acionamento_ventoinha = 100
          pwm_ventoinha.ChangeDutyCycle(100)
        else:
          valores.acionamento_ventoinha = abs(valores.sinal_controle)
          pwm_ventoinha.ChangeDutyCycle(abs(valores.sinal_controle))
    elif(valores.sinal_controle > 0):
        valores.acionamento_ventoinha = 0
        pwm_ventoinha.ChangeDutyCycle(0)
        if(valores.sinal_controle > 100):
          valores.acionamento_resistor = 100
          pwm_resistor.ChangeDutyCycle(100)
        else:
          valores.acionamento_resistor = valores.sinal_controle
          pwm_resistor.ChangeDutyCycle(valores.sinal_controle)

def resfriar():
    pwm_ventoinha.ChangeDutyCycle(100)
    pwm_resistor.ChangeDutyCycle(0)
    valores.acionamento_resistor = 0
    valores.acionamento_ventoinha = 100
 
def finalizar_pwm():
    pwm_resistor.stop()
    valores.acionamento_resistor = 0
    pwm_ventoinha.stop()
    gpio.cleanup()
