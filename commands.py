from crc import calcula_CRC
from pid import pid
import valores
import pwm
import struct

class Commands:

    def __init__(self):
        self.esp32_address = bytes([int('0x01', 16)])
        self.ask_code = bytes([int('0x23', 16)])
        self.send_code = bytes([int('0x16', 16)])
        self.matricula = bytes([int('3', 16), int('2', 16), int('0', 16), int('3', 16),])
        self.ask_i_temp_code = bytes([int('0xC1', 16)])
        self.ask_r_temp_code = bytes([int('0xC2', 16)])
        self.read_user_code = bytes([int('0xC3', 16)])
        self.send_int_code = bytes([int('0xD1', 16)])
        self.send_r_temp_code = bytes([int('0xD2', 16)])
        self.send_s_status_code = bytes([int('0xD3', 16)])
        self.send_mode_code = bytes([int('0xD4', 16)])
        self.send_f_status_code = bytes([int('0xD5', 16)])
        self.send_a_temp_code = bytes([int('0xD6', 16)])
    
    # Solicita Temperatura Interna
    def ask_intern_temp(self) -> bytes:
        commands = self.esp32_address + self.ask_code + self.ask_i_temp_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

    # Solicita Temperatura de Referência
    def ask_reference_temp(self) -> bytes:
        commands = self.esp32_address + self.ask_code + self.ask_r_temp_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)
    
    # Lê Comandos do Usuário
    def read_user_command(self) -> bytes:
        commands = self.esp32_address + self.ask_code + self.read_user_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

    # Envia Sinal de Controle 
    def send_control_signal(self) -> bytes:
        code = struct.pack("<i", int(valores.sinal_controle))
        commands = self.esp32_address + self.send_code + self.send_int_code + self.matricula + code
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

    # Envia Sinal de Referência
    def send_reference_signal(self) -> bytes:
        code = struct.pack("<f", float(valores.temp_referencia) )
        commands = self.esp32_address + self.send_code + self.send_r_temp_code + self.matricula + code
        crc = calcula_CRC(commands)
        return bytes(commands + crc)
    
    # Envia Estado de Sistema 
    def send_system_status(self, status) -> bytes:
        code = bytes([int(f'{status}', 16)])
        commands = self.esp32_address + self.send_code + self.send_s_status_code + self.matricula + code
        crc = calcula_CRC(commands)
        return bytes(commands + crc)
    
    # Envia Modo de Controle 
    def send_control_mode(self, mode) -> bytes:
        code = bytes([mode])
        commands = self.esp32_address + self.send_code + self.send_mode_code + self.matricula + code
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

    # Envia Estado de Funcionamento 
    def send_func_status(self, status) -> bytes:
        code = bytes([int(f'{status}', 16)])
        commands = self.esp32_address + self.send_code + self.send_f_status_code + self.matricula + code
        crc = calcula_CRC(commands)
        return bytes(commands + crc)
    
    # Envia Temperatura Ambiente
    def send_external_temp(self) -> bytes:
        code = struct.pack("<f", valores.temperatura_ambiente )
        commands = self.esp32_address + self.send_code + self.send_a_temp_code + self.matricula + code
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

comandos = Commands()