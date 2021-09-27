import os
import requests
from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('URL:'), sg.Input(key=(url, endereco), size=(30, 1))],
    [sg.Button('Entrar')]
]

# Janela
Janela = sg.Window('Filminho bebê', layout)
# Ler eventos
while True:
    eventos, valores = Janela.read()  # Função de fechamento de janela
    if eventos == sg.WINDOW_CLOSED:  # Função de fechamento de janela
        break  # Função de fechamento de janela
    if eventos == 'Enter':  # se eu apertar o enter fazer a ação
        def baixar_arquivo(url, endereco):
            # faz requisição ao servidor
            resposta = requests.get(url)
            if resposta.status_code == requests.codes.OK:
                with open(endereco, 'wb') as novo_arquivo:
                    novo_arquivo.write(resposta.content)
                print("Download finalizado. Salvo em: {}".format(endereco))
            else:
                resposta.raise_for_status()
                print('Não encontrado!')


if __name__ == "__main__":
    BASE_URL = 'https://math.mit.edu/classes/18.745/Notes/Lecture_{}_Notes.pdf'
    OUTPUT_DIR = 'output'
    for i in range(1, 26):
        nome_arquivo = os.path.join(OUTPUT_DIR, 'nota_de_aula_{}.pdf'.format(i))
        baixar_arquivo(BASE_URL.format(i), nome_arquivo)
