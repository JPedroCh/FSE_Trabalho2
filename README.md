# FSE_Trabalho_2

Repositório para o [Trabalho 2](https://gitlab.com/fse_fga/trabalhos-2022_2/trabalho-2-2022-2) da disciplina de Fundamentos de Sistemas Embarcados (FGA-UnB).

## Dependências

* python3 (versão utilizada: 3.7.3)

* RPi.GPIO


  Para instalar:`pip3 install RPi.GPIO`

* smbus2


  Para instalar:`pip3 install smbus2`
  
* RPi.bme280 


  Para instalar: `pip3 install RPi.bme280`

## Como executar

Para executar o código:

```bash
python3 main.py
```

## Funcionamento

Após executar o arquivo `main.py`:

* Selecione se deseja alterar parâmetros do PID:
  * **1** - Se desejar alterar: É solicitado para o usuário inserir os novos valores Kp, Ki, Kd.
  * **2** - Se não desejar alterar: os valores padrões são mantidos

* Selecione o modo como deseja controlar a temperatura de referência:
  * **1** - Dashboard
  * **2** - Curva pré-definida no arquivo **[curva_reflow.json](/curva_reflow.json)**
  * **3** - Via terminal [Modo Debug]: é solicitado para o usuário inserir o valor de temperatura de referência que será utilizado.
* Para sair pressione  **'Ctrl+C'**.
* Uma linha de log é gerada no arquivo **log.csv** a cada segundo de execução. 

## Gráficos 

![Gráfico da Curva](images/grafico_curva.jpg)

![Gráfico de Modo Dashboard](images/grafico_dashboard.jpg)