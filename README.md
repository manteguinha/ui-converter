# Conversor de .UI em .PY

Este script converte arquivos QtDesigner UI (`.ui`) em arquivos Python (`.py`) usando a biblioteca PySimpleGUI e o comando `pyside2-uic`.

## Requisitos

- Python 3
- PySimpleGUI
- PySide2

Instale as dependências usando:

```
pip install PySimpleGUI PySide2
```

## Uso

1. Execute o script.
2. Digite um novo nome para o arquivo Python no campo "Novo nome:".
3. Clique em "Procurar" para selecionar o arquivo `.ui` que você deseja converter.
4. Clique em "Converter" para iniciar a conversão.
5. Após a conversão, uma mensagem "Conversão concluída!" será exibida.

## Observações

- Este script usa o comando `pyside2-uic` para converter arquivos `.ui` em `.py`. Certifique-se de que você tenha o PySide2 instalado e o comando esteja disponível no seu sistema.
