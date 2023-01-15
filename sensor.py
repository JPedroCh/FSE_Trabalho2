import smbus2
import bme280
import valores

def init():
  # port = 1
  # sensor_address = 0x76
  # bus = smbus2.SMBus(port)
  print('init sensor')
  # parametros_calibracao = bme280.load_calibration_params(bus, sensor_address)

def leitura_sensor():
  # data = bme280.sample(bus, sensor_address, parametros_calibracao)
  # valores.temperatura_ambiente = format(data.temperature, '.2f')
  valores.temperatura_ambiente = 20.0
  