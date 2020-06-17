# Python Para Iniciantes | Live

## Introdução

Seja bem-vindo a live de Python Para Iniciantes, por aqui fazemos live semanalmente no canal da Twitch mostrando conceitos básicos de lógica de programação e Python para quem está começando neste mundo.

[As lives acontecem lá no meu canal da Twitch](https://www.twitch.tv/caveiradev)

## Setup Inicial

1. [Instale o Python](https://www.python.org/downloads/)
2. Escolha seu Ambiente de desenvolvimento
    - [Anaconda + Spyder](https://www.anaconda.com/)
    - [Visual Studio Code](https://code.visualstudio.com/)
    - [PyCharm](https://www.jetbrains.com/pycharm/)
    - [Online](https://repl.it/languages/python3) 

> ATENÇÃO:
> 
> Ao optar pela versão online, você não conseguirá instalar as bibliotecas que iremos utilizar em algumas lives, por isso, a recomendação é de fazer a instalação para aproveitar ao máximo.

3. Utilização de Ambiente Virtual ([Virtual Environment](https://docs.python.org/3/library/venv.html)) - Opcional porém recomendado

Você pode criar um ambiente virtual utilizando os seguintes comandos abaixo (Atenção, esses comandos não irão funcionar se você estiver em um ambiente Windows):

> ATENÇÃO: 
> 
> Verifique se seu sistema possui o python3 ou apenas o python (lembre-se de usar o Python na versão 3 - para verificar isso, utilize o comando: ```python --version```)

Para MacOs e Linux:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Para Windows:

```
python3 -m venv .venv
source .venv\Scripts\activate.bat
pip install -r requirements.txt
```