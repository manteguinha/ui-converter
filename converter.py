import PySimpleGUI as sg
import os

class Converter:
    def __init__(self):
        sg.theme('DarkPurple 1')
        layout = [
            [sg.Text('Novo nome:'), sg.Input(size=(30,1), key='-NOVO-')],
            [sg.FileBrowse('Procurar', button_color='gray', key='-ARQUIVO-', file_types=(("Arquivos do QtDesigner", "*.ui"),)), sg.Text(size=(28,1))],
            [sg.Button('Converter')],
        ]

        self.janela = sg.Window('Conversor de .UI em .PY', layout)

    def iniciar(self):
        while True:
            event, values = self.janela.read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Converter':
                if values['-ARQUIVO-'] == '':
                    sg.popup('Selecione um arquivo!')
                elif values['-NOVO-'] == '':
                    sg.popup('Digite um nome para o arquivo!')
                else:
                    nome = values['-NOVO-']
                    arquivo = values['-ARQUIVO-']
                    comando = 'pyside2-uic "' + arquivo + '" -o ' + nome + '.py ' 
                    os.system(comando)
                    sg.popup('Conversão concluída!')



start = Converter()
start.iniciar()