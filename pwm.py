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

  pwm_resistor = gpio.PWM(23, 50)
  pwm_resistor.start(0)

  # pwm_ventoinha = gpio.PWM(24, 100)
  pwm_ventoinha = gpio.PWM(24, 50)
  pwm_ventoinha.start(100)

def atualiza_duty_cycle():
    if(valores.sinal_controle < 0 and valores.sinal_controle > -40):
        pwm_resistor.ChangeDutyCycle(0)
        pwm_ventoinha.ChangeDutyCycle(40)
    elif(valores.sinal_controle < -40):
        pwm_resistor.ChangeDutyCycle(0)
        if(valores.sinal_controle < -100):
          pwm_ventoinha.ChangeDutyCycle(100)
        else:
          pwm_ventoinha.ChangeDutyCycle(abs(valores.sinal_controle))
    elif(valores.sinal_controle == 0):
        pwm_resistor.ChangeDutyCycle(0)
        pwm_ventoinha.ChangeDutyCycle(0)
    elif(valores.sinal_controle > 0):
        pwm_ventoinha.ChangeDutyCycle(0)
        if(valores.sinal_controle > 100):
          pwm_resistor.ChangeDutyCycle(100)
        else:
          pwm_resistor.ChangeDutyCycle(valores.sinal_controle)
 
def finalizar_pwm():
    pwm_resistor.stop()
    pwm_ventoinha.stop()
    gpio.cleanup()
