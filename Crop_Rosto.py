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


def extract_face(image_file, size=(160, 160)):
    """
    Extrai a face de uma imagem.

    Parâmetros:
    - image_file (str): Caminho para o arquivo da imagem.
    - size (tuple): Tamanho desejado para a face extraída.

    Retorna:
    - imagem (PIL.Image): Imagem da face extraída.
    """
    # Carrega a imagem
    img = Image.open(image_file)
    img = img.convert('RGB')
    array = asarray(img)

    # Detecta as faces na imagem
    detector = MTCNN()
    results = detector.detect_faces(array)

    # Extrai a primeira face encontrada
    x1, y1, width, height = results[0]['box']
    x2, y2 = x1 + width, y1 + height
    face = array[y1:y2, x1:x2]

    # Redimensiona a face para o tamanho desejado
    image = Image.fromarray(face)
    image = image.resize(size)

    return image


def load_photos(source_directory, target_directory):
    """
    Pré-processa e salva as fotos com as faces extraídas.

    Parâmetros:
    - source_directory (str): Diretório de origem das fotos.
    - target_directory (str): Diretório de destino das fotos com as faces extraídas.
    """
    for filename in listdir(source_directory):
        file_path = source_directory + filename
        target_path = target_directory + filename
        flipped_target_path = target_directory + "flip" + filename
        try:
            # Extrai a face da foto
            face = extract_face(file_path)

            # Gera uma versão espelhada da face
            flipped_face = flip_image(face)

            # Salva as faces nos diretórios de destino
            face.save(target_path, "JPEG", quality=100, optimize=True, progressive=True)
            flipped_face.save(flipped_target_path, "JPEG", quality=100, optimize=True, progressive=True)
        except:
            print("Erro na imagem {}".format(file_path))


def load_directory(source_directory, target_directory):
    """
    Pré-processa e salva as fotos com as faces extraídas de um diretório e seus subdiretórios.

    Parâmetros:
    - source_directory (str): Diretório de origem das fotos.
    - target_directory (str): Diretório de destino das fotos com as faces extraídas.
    """
    for subdir in listdir(source_directory):
        path = source_directory + subdir + "\\"
        target_path = target_directory + subdir + "\\"
        if not isdir(path):
            continue
        load_photos(path, target_path)


def flip_image(image):
    """
    Gira a imagem horizontalmente (espelha).

    Parâmetros:
    - image (PIL.Image): Imagem a ser espelhada.

    Retorna:
    - flipped_image (PIL.Image): Imagem espelhada.
    """
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    return flipped_image


if __name__ == '__main__':
    source_directory = "D:\\Projetos\\Python\\TCC\\fotos\\"  # Colocar o caminho até as fotos originais
    target_directory = "D:\\Projetos\\Python\\TCC\\faces\\"  # Colocar o caminho para salvar as faces extraídas
    load_directory(source_directory, target_directory)
