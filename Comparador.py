"""
Módulo de geração de embeddings usando o modelo FaceNet.

Este módulo contém funções para carregar imagens, gerar embeddings usando o modelo FaceNet
e salvar os embeddings em um arquivo Excel.

Requisitos:
- PIL (Python Imaging Library)
- numpy
- keras
- keras_facenet
- pandas

"""

from PIL import Image
from os import listdir
from os.path import isdir
from numpy import asarray, expand_dims
import numpy as np
from keras.models import load_model
from keras_facenet import FaceNet
import pandas as pd


def carregar_imagens(filename):
    """
    Carrega uma imagem e converte para array numpy.

    Parâmetros:
    - filename (str): Caminho do arquivo da imagem.

    Retorno:
    - numpy.ndarray: Array numpy representando a imagem.
    """
    imagem = Image.open(filename)
    imagem = imagem.convert("RGB")
    return asarray(imagem)


def carregar_rostos(diretorio_src, nome_diretorio):
    """
    Carrega os rostos de um diretório.

    Parâmetros:
    - diretorio_src (str): Caminho do diretório contendo as imagens dos rostos.
    - nome_diretorio (str): Nome do diretório.

    Retorno:
    - list: Lista contendo tuplas (nome_diretorio, rosto), onde rosto é um array numpy do rosto.
    """
    rostos = list()
    for filename in listdir(diretorio_src):
        arquivo = diretorio_src + filename
        try:
            rosto = carregar_imagens(arquivo)
            rostos.append((nome_diretorio, rosto))
        except:
            print("Erro no arquivo {}".format(arquivo))
    return rostos


def carregar_fotos(diretorio_src):
    """
    Carrega todas as fotos dos diretórios.

    Parâmetros:
    - diretorio_src (str): Caminho do diretório raiz contendo os diretórios dos rostos.

    Retorno:
    - numpy.ndarray: Array numpy com as imagens dos rostos.
    - numpy.ndarray: Array numpy com os nomes dos diretórios correspondentes.
    """
    x, y = list(), list()
    for subdir in listdir(diretorio_src):
        diretorio = diretorio_src + subdir + "\\"
        if not isdir(diretorio):
            continue
        rostos = carregar_rostos(diretorio, subdir)
        labels = [subdir for _ in range(len(rostos))]

        print('> Carregados %d rostos do diretório: %s' % (len(rostos), subdir))
        
        for diretorio, rosto in rostos:
            x.append(rosto)
            y.append(diretorio)

    return asarray(x), asarray(y)


def gerar_embeddings(modelo, imagens):
    """
    Gera as embeddings das imagens usando o modelo FaceNet.

    Parâmetros:
    - modelo (keras.models.Model): Modelo FaceNet pré-treinado.
    - imagens (numpy.ndarray): Array numpy contendo as imagens dos rostos.

    Retorno:
    - list: Lista contendo as embeddings das imagens.
    """
    embeddings = []
    for imagem in imagens:
        # Normaliza os pixels da imagem
        imagem = imagem.astype('float32')
        media = imagem.mean()
        desvio_padrao = imagem.std()
        imagem = (imagem - media) / desvio_padrao
        imagem = expand_dims(imagem, axis=0)

        # Gera a embedding
        embedding = modelo.predict(imagem)
        embeddings.append(embedding.flatten())

    return embeddings


def load_model():
    """
    Carrega o modelo FaceNet.

    Retorno:
    - keras.models.Model: Modelo FaceNet pré-treinado.
    """
    model = FaceNet()
    model = model.model
    return model


modelo = load_model()

# Carrega as imagens
imagens, diretorios = carregar_fotos("Caminho para o diretório raiz contendo os diretórios dos rostos")

# Gera as embeddings
embeddings = gerar_embeddings(modelo, imagens)

# Cria o DataFrame com as embeddings e os nomes dos diretórios
df = pd.DataFrame(embeddings)

# Salva o DataFrame em um arquivo Excel
df.to_excel('embeddings.xlsx')
