# Blur no Rosto

Programa que faz o famoso blur no rosto da(s) pessoa(s).

# Descrição

Esse programa foi escrito em Python e usou a biblioteca <a href="https://opencv.org/">OpenCV</a> como base. Ele faz o famoso blur no rosto de uma pessoa, uma coisa que vemos em entrevistas onde o entrevistado não quer mostrar o rosto. Enfim, ele basicamente só tem a necessidade de entrada de um dado por parte do usuário, que é o caminho da imagem que deseja aplicar o blur (em vídeo não há necessidade). Além disso, você pode fazer a alteração dos cascades para o que melhor se encaixar para o seu uso. Esses cascades se encontram na pasta do próprio projeto. Fora isso é só usar e fazer os ajustes que julgar necessário.

# Como funciona?

O programa faz a detecção do rosto da(s) pessoa(s) e aplica o blur no local onde foi localizado o rosto.

# Instalação

É preciso ter o Python instalado no seu computador (<a href="https://www.python.org/downloads/">Python</a>, recomendado baixar a última versão). Para importar algumas funções usadas nesse projeto é preciso fazer a instalação de algumas bibliotecas, são elas:

* opencv-python - Forma de instalação: <b>pip install opencv-python</b>
* imutils - Forma de instalação: <b>pip install imutils</b>

<b>Obs.:</b> Essas instalações podem ser feitas pelo terminal do seu computador (necessário que já tenha o python instalado) ou pelo terminal do <a href="https://www.jetbrains.com/pt-br/pycharm/download/">PyCharm</a>, se preferir.

# Uso

Após as instalações, para começar a usar basta clonar esse repositório e digitar o comando <b>python blur-rosto.py</b> no terminal ou rodar pelo PyCharm.

# Exemplos

Aqui estão alguns exemplos que fiz ao longo do processo.

* Fazendo o blur em vídeo.

![video-blur](https://user-images.githubusercontent.com/60857927/82528125-77cd1d80-9b0e-11ea-8da7-56a41ccd3d8b.gif)

* Fazendo o blur na imagem da Pablo Vittar.

![pablo-vittar-blur](https://user-images.githubusercontent.com/60857927/82528715-c9c27300-9b0f-11ea-83cd-a13f999b9110.png)

* Fazendo o blur na imagem da Beyonce.

![beyonce-blur](https://user-images.githubusercontent.com/60857927/82528728-d050ea80-9b0f-11ea-8f40-afa2c6f2e55d.png)

* Fazendo o blur na imagem do Obama.

![obama-blur](https://user-images.githubusercontent.com/60857927/82528738-d3e47180-9b0f-11ea-824f-f65a52887e1e.png)

* Fazendo o blur na imagem da Bianca Bin.

![bianca-bin-blur](https://user-images.githubusercontent.com/60857927/82528739-d646cb80-9b0f-11ea-914c-54a91fcc1770.png)
