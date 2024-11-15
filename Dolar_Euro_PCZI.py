from datetime import datetime
import pyautogui as py
import csv
import os
from tkinter import messagebox, Tk
import time


def dolar_diario():
    try:
        # Caminho para o arquivo CSV e para o arquivo HTML
        caminho_csv = 'C:\\Users\\zisil\\Downloads\\CotacoesMoedasPeriodo.csv'
        caminho_html = 'C:\\Users\\zisil\\OneDrive\\Documentos\\025 ATUALIZAÇÕES AUTOMATICAS YAHII\\Dolar_Euro\\dolardiario24.html'

        # Função para iniciar o download usando pyautogui
        def iniciar_download():
            py.PAUSE = 1.5
            py.press('win')
            py.write('google chrome')
            py.press('enter')
            py.hotkey('win', 'up')
            py.write('https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes')
            py.press('enter')
            py.sleep(11)
            py.click(-1141, 961, duration=0.3)
            py.sleep(5)
            py.click(-964, 722, duration=0.3)
            py.sleep(2)

        # Iniciar o download na primeira tentativa
        iniciar_download()

        # Verificar se o download foi feito, tentar até 3 vezes
        tentativa = 0
        while not os.path.exists(caminho_csv) and tentativa < 3:
            print("Aguardando download do arquivo CSV...")
            time.sleep(5)
            tentativa += 1
            print("Realizando uma nova tentativa...")
            if not os.path.exists(caminho_csv):
                iniciar_download()

        if not os.path.exists(caminho_csv):
            print("Erro: O arquivo CSV não foi baixado após 3 tentativas.")
            return

        # Inicializar variáveis para armazenar as colunas extraídas
        coluna_5 = None
        coluna_6 = None

        # Abrir e ler o arquivo CSV
        with open(caminho_csv, newline='') as csvfile:
            leitor_csv = csv.reader(csvfile, delimiter=';')
            for row in leitor_csv:
                ultima_linha = row

        # Verificar se a última linha foi lida corretamente e tem pelo menos 6 colunas
        if ultima_linha and len(ultima_linha) >= 6:
            coluna_5 = ultima_linha[4]
            coluna_6 = ultima_linha[5]

            # Excluir o arquivo CSV
            os.remove(caminho_csv)

        # Obter a data atual formatada
        data_atual = datetime.now().strftime('%d/%m/%Y')

        # Preparar a nova linha com a data e valores extraídos
        nova_linha = f'''                <TD><FONT face=verdana size=2>{data_atual}</FONT></TD>
                <TD align=right><FONT face=verdana size=2>{coluna_5}</FONT></TD>
                <TD align=right><FONT face=verdana size=2>{coluna_6}</FONT></TD></TR>
        '''

        # Abrir o arquivo HTML e procurar a próxima linha vazia com '&nbsp;'
        with open(caminho_html, 'r') as file:
            linhas = file.readlines()

        # Procurar a linha com '&nbsp;' e substituir pelo novo conteúdo
        for i, linha in enumerate(linhas):
            if '                <TD><FONT face=verdana size=2>&nbsp;</FONT></TD>' in linha:
                linhas[i:i+3] = [nova_linha]
                break

        # Escrever as alterações de volta no arquivo HTML
        with open(caminho_html, 'w') as file:
            file.writelines(linhas)

        print(f'Dados adicionados ao arquivo {caminho_html}')
    except Exception as e:
        print(f'Erro no Arquivo {e}')

        
def euro_diario():
    try:
        # Caminho para o arquivo CSV e para o arquivo HTML
        caminho_csv = 'C:\\Users\\zisil\\Downloads\\CotacoesMoedasPeriodo.csv'
        caminho_html = 'C:\\Users\\zisil\\OneDrive\\Documentos\\025 ATUALIZAÇÕES AUTOMATICAS YAHII\\Dolar_Euro\\eurodiario24.html'  

        # Função para iniciar o download usando pyautogui
        def iniciar_download():
            py.PAUSE = 1.5
            py.hotkey('ctrl', 't')
            py.write('https://www.bcb.gov.br/estabilidadefinanceira/historicocotacoes')
            py.press('enter')
            py.sleep(11)
            py.click (-976, 892, duration=0.3)
            py.press('down', presses=29)
            py.click (-976, 892, duration=0.3)
            py.click(-1138, 968, duration=0.3)
            py.sleep(5)
            py.click (-964, 722, duration=0.3)
            py.sleep(2)
            py.hotkey('alt', 'F4')

        # Iniciar o download na primeira tentativa
        iniciar_download()

        # Verificar se o download foi feito, tentar até 3 vezes
        tentativa = 0
        while not os.path.exists(caminho_csv) and tentativa < 3:
            print("Aguardando download do arquivo CSV...")
            time.sleep(5)
            tentativa += 1
            print("Realizando uma nova tentativa...")
            if not os.path.exists(caminho_csv):
                iniciar_download()

        if not os.path.exists(caminho_csv):
            print("Erro: O arquivo CSV não foi baixado após 3 tentativas.")
            return

        # Inicializar variáveis para armazenar as colunas extraídas
        coluna_5 = None
        coluna_6 = None

        # Abrir e ler o arquivo CSV
        with open(caminho_csv, newline='') as csvfile:
            leitor_csv = csv.reader(csvfile, delimiter=';')
            for row in leitor_csv:
                ultima_linha = row

        # Verificar se a última linha foi lida corretamente e tem pelo menos 6 colunas
        if ultima_linha and len(ultima_linha) >= 6:
            coluna_5 = ultima_linha[4]
            coluna_6 = ultima_linha[5]

            # Excluir o arquivo CSV
            os.remove(caminho_csv)

        # Obter a data atual formatada
        data_atual = datetime.now().strftime('%d/%m/%Y')

        # Preparar a nova linha com a data e valores extraídos
        nova_linha = f'''                <TD><FONT face=verdana size=2>{data_atual}</FONT></TD>
                <TD align=right><FONT face=verdana size=2>{coluna_5}</FONT></TD>
                <TD align=right><FONT face=verdana size=2>{coluna_6}</FONT></TD></TR>
        '''

        # Abrir o arquivo HTML e procurar a próxima linha vazia com '&nbsp;'
        with open(caminho_html, 'r') as file:
            linhas = file.readlines()

        # Procurar a linha com '&nbsp;' e substituir pelo novo conteúdo
        for i, linha in enumerate(linhas):
            if '                <TD><FONT face=verdana size=2>&nbsp;</FONT></TD>' in linha:
                linhas[i:i+3] = [nova_linha]
                break

        # Escrever as alterações de volta no arquivo HTML
        with open(caminho_html, 'w') as file:
            file.writelines(linhas)

        print(f'Dados adicionados ao arquivo {caminho_html}')
    except Exception as e:
        print(f'Erro no Arquivo {e}')

def executar_ambas():
    dolar_diario()
    euro_diario()

# Criar uma janela oculta para exibir a mensagem
root = Tk()
root.withdraw()

# Executar as funções
executar_ambas()

# Exibir a mensagem de conclusão
messagebox.showinfo("Concluído", "Os dados foram adicionados aos arquivos HTML com sucesso!")
