# Reconhecimento_Facial

Gerador_de_embeddings.py:

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

----------------------------------------------------------------------------------------------------------------------

Cadastrar_rosto.py:

Esse código contém uma função capture_images que captura imagens usando a webcam e as salva em um diretório específico. O código está estruturado da seguinte maneira:

Importação das bibliotecas necessárias.
Definição da função capture_images que realiza a captura das imagens.
Leitura do nome do diretório onde as imagens serão salvas.
Definição do tempo de captura em segundos.
Definição do tempo de espera antes de fechar a janela em segundos.
Chamada da função capture_images para capturar e salvar as imagens.

----------------------------------------------------------------------------------------------------------------------

Crop_rosto.py:

Esse código contém funções para pré-processar imagens, detectar e extrair faces utilizando a biblioteca MTCNN. O código está estruturado da seguinte maneira:

Importação das bibliotecas necessárias.
Definição da função extract_face que extrai a face de uma imagem.
Definição da função load_photos que pré-processa e salva as fotos com as faces extraídas.
Definição da função load_directory que pré-processa e salva as fotos com as faces extraídas de um diretório e seus subdiretórios.
Definição da função flip_image que gira a imagem horizontalmente (espelha).
Verificação se o módulo está sendo executado diretamente como programa principal.
Leitura dos diretórios de origem e destino das fotos.
Chamada da função load_directory para pré-processar e salvar as fotos com as faces extraídas.
