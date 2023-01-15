import crc
import valores
import modbus
from commands import comandos
import time
import struct
from curva import curva

def decodifica_rx(rx_buffer, rx_length):

    if rx_length < 0:
        print("[ERRO] Erro de leitura.")
    elif rx_length == 0:
        print("[ERRO] Não existem dados disponíveis.")
    else:

        for idx in range(rx_length):
          if(rx_buffer[idx] == int('0x00', 16)):
            if(rx_buffer[idx+1] == int('0x23', 16)):
              if(rx_buffer[idx+2] == int('0xC1', 16)):
                print(' - 0xC1')
                crc_validado = crc.verifica_CRC(rx_buffer[idx:idx+9], 9)
                if(crc_validado):
                  valores.temp_interna = struct.unpack('<f', rx_buffer[idx+3:idx+7])[0]
              elif(rx_buffer[idx+2] == int('0xC2', 16)):
                print(' - 0xC2')
                crc_validado = crc.verifica_CRC(rx_buffer[idx:idx+9], 9)
                if(crc_validado):
                  valores.temp_referencia = struct.unpack('<f', rx_buffer[idx+3:idx+7])[0]
              elif(rx_buffer[idx+2] == int('0xC3', 16)):
                print(' - 0xC3')
                crc_validado = crc.verifica_CRC(rx_buffer[idx:idx+9], 9)
                if(crc_validado):
                  decodifica_comando_usuario(rx_buffer[idx+3:idx+7])
            elif(rx_buffer[idx+1] == int('0x16', 16)):
              if(rx_buffer[idx+2] == int('0xD3', 16)):
                print(' - 0xD3')
                crc_validado = crc.verifica_CRC(rx_buffer[idx:idx+9], 9)
                if(crc_validado):
                  valores.estado_sistema = struct.unpack('<I', rx_buffer[idx+3:idx+7])[0]
              elif(rx_buffer[idx+2] == int('0xD4', 16)):
                print(' - 0xD4')
                crc_validado = crc.verifica_CRC(rx_buffer[idx:idx+9], 9)
                if(crc_validado):
                  valores.modo_controle_temperatura = struct.unpack('<I', rx_buffer[idx+3:idx+7])[0]
              elif(rx_buffer[idx+2] == int('0xD5', 16)):
                print(' - 0xD5')
                crc_validado = crc.verifica_CRC(rx_buffer[idx:idx+9], 9)
                if(crc_validado):
                  valores.estado_funcionamento = struct.unpack('<I', rx_buffer[idx+3:idx+7])[0]
              elif(rx_buffer[idx+2] == int('0xD6', 16)):
                print(' - 0xD6')
                crc_validado = crc.verifica_CRC(rx_buffer[idx:idx+9], 9)
                if(crc_validado):
                  print(struct.unpack('<f', rx_buffer[idx+3:idx+7])[0])
        


def decodifica_comando_usuario(comando):
    for i in comando:
      # Liga o forno
      if(i == int('0xA1', 16)):
        print(' - 0xA1')
        print('>>>> LIGA O FORNOOOOOO')
        if(valores.estado_sistema == 0):
          valores.estado_sistema = 1
          modbus.envia(comandos.send_system_status(1))

      # Desliga o forno
      elif(i == int('0xA2', 16)):
        print(' - 0xA2')
        if(valores.estado_sistema == 1):
          valores.estado_sistema = 0
          modbus.envia(comandos.send_system_status(0))

      # Inicia aquecimento
      elif(i == int('0xA3', 16)):
        print(' - 0xA3')
        if(valores.estado_sistema == 1):
          valores.estado_funcionamento = 1
          modbus.envia(comandos.send_func_status(1))
          if(valores.modo_controle_temperatura == 1):
            curva.stop()
            curva.start()
      
      # Para aquecimento
      elif(i == int('0xA4', 16)):
        print(' - 0xA4')
        if(valores.estado_funcionamento == 1 and valores.estado_sistema == 1):
          valores.estado_funcionamento = 0
          modbus.envia(comandos.send_func_status(0))

      # Altera modo de controle de temperatura
      elif(i == int('0xA5', 16)):
        print(' - 0xA5')
        print('MODO DE CONTROLE MUDOU')
        if(valores.modo_controle_temperatura == 0):
          valores.modo_controle_temperatura = 1
          modbus.envia(comandos.send_control_mode(1))
          if(valores.estado_sistema == 1 and valores.estado_funcionamento == 1):
            print('TÁ NA CONDIÇÀO')
            curva.stop()
            curva.start()
        else: 
          valores.modo_controle_temperatura = 0
          modbus.envia(comandos.send_control_mode(0))
          modbus.envia(comandos.ask_reference_temp())
          curva.stop()