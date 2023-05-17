"""
Módulo de captura de imagens usando webcam.

Este módulo contém um código para capturar imagens usando a webcam e salvá-las em um diretório específico.

Requisitos:
- cv2 (OpenCV)
- os
- time
- keras

"""

import cv2
import os
import time

from keras.models import load_model


def captura_imagens(directory, capture_time, wait_time):
    """
    Captura imagens usando a webcam e as salva em um diretório específico.

    Parâmetros:
    - directory (str): Nome do diretório onde as imagens serão salvas.
    - capture_time (int): Tempo de captura em segundos.
    - wait_time (int): Tempo de espera antes de fechar a janela em segundos.
    """
    # Diretório onde as capturas serão salvas
    diretorio = 'Caminho até o diretório' + directory + "\\"

    # Cria o diretório se ele não existir
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    # Inicia a captura de vídeo
    captura = cv2.VideoCapture(0)

    # Define a taxa de quadros por segundo
    captura.set(cv2.CAP_PROP_FPS, 30)

    # Define a resolução da imagem
    captura.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    captura.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Tempo inicial de captura
    tempo_inicial = time.time()

    # Contador de imagens capturadas
    contador = 0

    # Loop de captura
    while (time.time() - tempo_inicial) < capture_time:
        # Captura um frame
        ret, frame = captura.read()

        # Exibe o frame na tela
        cv2.imshow('Captura', frame)

        # Salva o frame em um arquivo
        arquivo = os.path.join(diretorio, 'captura_{}.jpg'.format(contador))
        cv2.imwrite(arquivo, frame)

        # Incrementa o contador
        contador += 1

    # Encerra a captura de vídeo e fecha a janela
    captura.release()
    cv2.destroyAllWindows()

    # Aguarda o tempo de espera antes de fechar o programa
    time.sleep(wait_time)


# Nome do diretório onde as imagens serão salvas
nome = input("Digite o nome do diretório : ")

# Tempo de captura em segundos
tempo_captura = 3

# Tempo de espera antes de fechar a janela em segundos
tempo_espera = 5

# Captura as imagens e salva no diretório especificado
captura_imagens(nome, tempo_captura, tempo_espera)
