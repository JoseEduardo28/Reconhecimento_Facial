# Reconhecimento_Facial
Reconhecimento facial com, cadastro, corte da face e gerador de embeddings

Esse código contém funções para carregar imagens, gerar embeddings usando o modelo FaceNet e salvar os embeddings em um arquivo Excel. Ele depende das bibliotecas PIL, numpy, keras, keras_facenet e pandas.

O código está estruturado da seguinte maneira:

Importação das bibliotecas necessárias.
Definição da função carregar_imagens que carrega uma imagem e a converte em um array numpy.
Definição da função carregar_rostos que carrega os rostos de um diretório específico.
Definição da função carregar_fotos que carrega todas as fotos dos diretórios.
Definição da função gerar_embeddings que gera as embeddings das imagens usando o modelo FaceNet.
Definição da função load_model que carrega o modelo FaceNet pré-treinado.
Carregamento do modelo FaceNet.
Carregamento das imagens e diretórios.
Geração das embeddings das imagens.
Criação de um DataFrame com as embeddings e os nomes dos diretórios.
Salvamento do DataFrame em um arquivo Excel.
