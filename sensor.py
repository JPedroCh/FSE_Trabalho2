import smbus2
import bme280
import valores

port = 0
sensor_address = 0
bus = 0
parametros_calibracao = 0

def init():
  global port, sensor_address, bus, parametros_calibracao
  port = 1
  sensor_address = 0x76
  bus = smbus2.SMBus(port)
  parametros_calibracao = bme280.load_calibration_params(bus, sensor_address)

def leitura_sensor():
  data = bme280.sample(bus, sensor_address, parametros_calibracao)
  valores.temperatura_ambiente = float(format(data.temperature, '.2f'))
  