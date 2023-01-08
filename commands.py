from crc import calcula_CRC

class Commands:
    # Endereço da ESP32
    esp32_address = bytes([int('0x01', 16)])

    # Código de Leitura
    ask_code = bytes([int('0x23', 16)])

    # Código de Envio
    send_code = bytes([int('0x16', 16)])

    # 4 Últimos Dígitos da Matrícula
    matricula = bytes([int('3', 16), int('2', 16), int('0', 16), int('3', 16),])

    # Código de Solicitação de Temperatura Interna
    ask_i_temp_code = bytes([int('0xC1', 16)])

    # Código de Solicitação de Temperatura de Referência
    ask_r_temp_code = bytes([int('0xC2', 16)])

    # Código de Leitura de Comandos do Usuário
    read_user_code = bytes([int('0xC3', 16)])

    # Código de Envio de Sinal de Controle Int (4 bytes)
    send_int_code = bytes([int('0xD1', 16)])

    # Código de Envio de Sinal de Referência Float (4 bytes)
    send_float_code = bytes([int('0xD2', 16)])

    # Código de Envio de Estado do Sistema Int (4 bytes)
    send_s_status_code = bytes([int('0xD3', 16)])

    # Código de Envio de Modo de Controle de Temperatura de Referência (1 byte)
    send_mode_code = bytes([int('0xD4', 16)])

    # Código de Envio de Estado de Funcionamento 
    send_f_status_code = bytes([int('0xD5', 16)])

    def __init__(self):
        self.esp32_address = esp32_address
        self.ask_code = ask_code
        self.send_code = send_code
        self.matricula = matricula
        self.ask_i_temp_code = ask_i_temp_code
        self.ask_r_temp_code = ask_r_temp_code
        self.read_user_code = read_user_code
        self.send_int_code = send_int_code
        self.send_float_code = send_float_code
        self.send_s_status_code = send_s_status_code
        self.send_mode_code = send_mode_code
        self.send_f_status_code = send_f_status_code
    
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
        commands = self.esp32_address + self.send_code + self.send_int_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

    # Envia Sinal de Referência
    def send_reference_signal(self) -> bytes:
        commands = self.esp32_address + self.send_code + self.send_float_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)
    
    # Envia Estado de Sistema 
    def send_system_status(self) -> bytes:
        commands = self.esp32_address + self.send_code + self.send_s_status_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)
    
    # Envia Modo de Controle 
    def send_control_mode(self) -> bytes:
        commands = self.esp32_address + self.send_code + self.send_mode_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

    # Envia Estado de Funcionamento 
    def send_control_mode(self) -> bytes:
        commands = self.esp32_address + self.send_code + self.send_f_status_code + self.matricula
        crc = calcula_CRC(commands)
        return bytes(commands + crc)

