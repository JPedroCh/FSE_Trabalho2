from pid import pid
import modbus
import time
import valores
from commands import comandos

novo_Kp = 0.0, 
novo_Ki = 0.0
novo_Kd = 0.0

def modo():
    print("\n*********************************************")
    print("Selecione o modo de Temperatura de Referência:")
    print("**********************************************")
    print("1 - Dashboard")
    print("2 - Curva pré-definida em arquivo")
    print("3 - Via terminal [Modo Debug]")
    opcao = int(input("Insira sua opção:"))

    if(opcao == 1):
        modbus.envia(comandos.send_control_mode(0))
        time.sleep(0.2)
        valores.modo_controle_temperatura = 0
        modbus.ler()

        print("Modo de controle pela Dashboard selecionado.")
    elif(opcao == 2):
        modbus.envia(comandos.send_control_mode(1))
        time.sleep(0.2)
        valores.modo_controle_temperatura = 1
        modbus.ler()
        print("Modo de controle pela curva selecionado.")
    elif(opcao == 3):
        modbus.envia(comandos.send_control_mode(1))
        valores.modo_controle_temperatura = 1
        print("Modo de controle pelo terminal selecionado.")
        leitor_temp_terminal()

def leitor_temp_terminal():
    temp_ref = float(input("\nInsira o valor da temperatura de referência:"))
    valores.temp_referencia = temp_ref
    print("Temperatura de referência definida.")


    
def campos_params():

    novo_Kp = float(input("\nInsira o novo valor de Kp:"))
    novo_Ki = float(input("Insira o novo valor de Ki:"))
    novo_Kd = float(input("Insira o novo valor de Kd:"))
    pid.pid_configura_constantes(novo_Kp, novo_Ki, novo_Kd)




def config_params():

    global novo_Kp, novo_Ki, novo_Kd
    print("\n**********************")
    print("Configuração de PID")
    print("**********************")
    print("\nValores padrões:")
    print("Kp = 30.0")
    print("Ki = 0.2")
    print("Kd = 400.0")
    print("\nDeseja alterar valores?")
    print("1 - Sim")
    print("2 - Não")
    opcao_param = int(input("Insira sua opção:"))

    if(opcao_param == 1):
        campos_params()
    else:
        print("\nValores foram mantidos.") 
