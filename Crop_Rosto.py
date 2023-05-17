"""
Módulo de pré-processamento de imagens para extração de faces.

Este módulo contém um código para pré-processar imagens, detectar e extrair faces utilizando a biblioteca MTCNN.

Requisitos:
- mtcnn
- PIL
- os
- numpy

"""

from mtcnn import MTCNN
from PIL import Image
from os import listdir
from os.path import isdir
from numpy import asarray


def extrair_face(arquivo_imagem, tamanho=(160, 160)):
    """
    Extrai o rosto de uma imagem.

    Parâmetros:
    - arquivo_imagem (str): Caminho para o arquivo da imagem.
    - tamanho (tuple): Tamanho desejado para o rosto extraído.

    Retorna:
    - imagem (PIL.Image): Imagem do rosto extraído.
    """
    # Carrega a imagem
    imagem = Image.open(arquivo_imagem)
    imagem = imagem.convert('RGB')
    array = asarray(imagem)

    # Detecta os rostos na imagem
    detector = MTCNN()
    resultados = detector.detect_faces(array)

    # Extrai o primeiro rosto encontrado
    x1, y1, largura, altura = resultados[0]['box']
    x2, y2 = x1 + largura, y1 + altura
    rosto = array[y1:y2, x1:x2]

    # Redimensiona o rosto para o tamanho desejado
    imagem = Image.fromarray(rosto)
    imagem = imagem.resize(tamanho)

    return imagem


def carregar_fotos(diretorio_origem, diretorio_destino):
    """
    Pré-processa e salva as fotos com os rostos extraídos.

    Parâmetros:
    - diretorio_origem (str): Diretório de origem das fotos.
    - diretorio_destino (str): Diretório de destino das fotos com os rostos extraídos.
    """
    for nome_arquivo in listdir(diretorio_origem):
        arquivo_imagem = diretorio_origem + nome_arquivo
        arquivo_destino = diretorio_destino + nome_arquivo
        arquivo_destino_virado = diretorio_destino + "flip_" + nome_arquivo
        try:
            # Extrai o rosto da foto
            rosto = extrair_face(arquivo_imagem)

            # Gera uma versão espelhada do rosto
            rosto_virado = imagem_virada(rosto)

            # Salva os rostos nos diretórios de destino
            rosto.save(arquivo_destino, "JPEG", quality=100, optimize=True, progressive=True)
            rosto_virado.save(arquivo_destino_virado, "JPEG", quality=100, optimize=True, progressive=True)
        except:
            print("Erro na imagem {}".format(arquivo_imagem))


def carregar_diretorio(diretorio_origem, diretorio_destino):
    """
    Pré-processa e salva as fotos com os rostos extraídos de um diretório e seus subdiretórios.

    Parâmetros:
    - diretorio_origem (str): Diretório de origem das fotos.
    - diretorio_destino (str): Diretório de destino das fotos com os rostos extraídos.
    """
    for subdir in listdir(diretorio_origem):
        caminho = diretorio_origem + subdir + "\\"
        caminho_destino = diretorio_destino + subdir + "\\"
        if not isdir(caminho):
            continue
        carregar_fotos(caminho, caminho_destino)


def imagem_virada(imagem):
    """
    Gira a imagem horizontalmente (espelha).

    Parâmetros:
    - imagem (PIL.Image): Imagem a ser espelhada.

    Retorna:
    - imagem_espelhada (PIL.Image): Imagem espelhada.
    """
    imagem_espelhada = imagem.transpose(Image.FLIP_LEFT_RIGHT)
    return imagem_espelhada


if __name__ == '__main__':
    diretorio_origem = ""  # Colocar o caminho até as fotos originais
    diretorio_destino = ""  # Colocar o caminho para salvar os rostos extraídos
    carregar_diretorio(diretorio_origem, diretorio_destino)
