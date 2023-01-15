import os
import termios
import time
import struct
import commands
from decodificadores import decodifica_rx

uart0_filestream = os.open("/dev/serial0", os.O_RDWR | os.O_NOCTTY | os.O_NDELAY)

def init():
    if uart0_filestream == -1:
        print("[ERRO] Não foi possível inicializar UART.")
    
    # definição das flags da UART
    attrs = termios.tcgetattr(uart0_filestream)
    attrs[2] = attrs[2] & ~termios.HUPCL
    attrs[4] = termios.B9600
    attrs[5] = termios.B9600
    attrs[6][termios.VMIN] = 0
    attrs[6][termios.VTIME] = 0
    termios.tcsetattr(uart0_filestream, termios.TCSAFLUSH, attrs)

def envia(command):
    tx_buffer = command

    if uart0_filestream != -1:
        count = os.write(uart0_filestream, tx_buffer)
        if count < 0:
            print("[ERRO] Erro no TX da UART")

def ler():
    if uart0_filestream != -1:
        rx_buffer = os.read(uart0_filestream, 255)
        rx_length = len(rx_buffer)
        decodifica_rx(rx_buffer, rx_length)

def fechar():
    os.close(uart0_filestream)