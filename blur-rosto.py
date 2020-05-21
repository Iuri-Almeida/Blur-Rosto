# Projeto Blur no Rosto - Python e OpenCV
# Autor: Iuri Lopes Almeida
# Perfil GitHub: https://github.com/Iuri-Almeida
# Data: 20/05/2020
# Descrição: Esse programa foi escrito em Python e usou a biblioteca OpenCV 
# 			 como base. Ele faz o famoso blur no rosto de uma pessoa, uma 
# 			 coisa que vemos em entrevistas onde o entrevistado não quer
# 			 mostrar o rosto. Enfim, ele basicamente só tem a necessidade 
# 			 de entrada de um dado por parte do usuário, que é o caminho
# 			 da imagem que deseja aplicar o blur (em vídeo não há necessidade).
# 			 Além disso, você pode fazer a alteração dos cascades para o que
# 			 melhor se encaixar para o seu uso. Esses cascades se encontram
# 			 na pasta do próprio projeto. Fora isso é só usar e fazer os 
# 			 os ajustes que julgar necessário. :)
# Forma de uso: python blur-rosto.py


# Importações necessárias para uso.
import cv2
import imutils


# Função responsável por fazer o blur em uma imagem.
def blurRostoImagem(caminhoImagem):

	print("[INFO] Iniciando o programa...")

	# Local onde o código irá se basear para detectar o que é um rosto.
	# Obs.: Cascade é um arquivo .xml que contém as características do
	# 		que é e não é um rosto humano.
	# Obs.: Tem alguns outros cascades na pasta que você pode testar e
	# 		ver qual melhor se encaixa no seu projeto.
	cascade = cv2.CascadeClassifier("cascades-rosto/haarcascade_frontalface_alt2.xml")

	print("[INFO] Lendo a imagem...")

	# Faz a leitura da imagem.
	imagem = cv2.imread(caminhoImagem)

	print("[INFO] Aperte qualquer tecla para fechar.")

	# Redimensione a imagem.
	# imagem = imutils.resize(imagem, width=600)

	# Converta a cor da imagem de BRG (padrão do OpenCV) para GRAY.
	gray_imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

	# Função responsável por detectar o que é um rosto e armazenar dentro
	# de um array (faces) as coordenadas de onde está esse possível rosto.
	# Obs.: Essa função faz a detecção do rosto dentro de um retângulo, 
	# 		logo, essas coordenadas são as de início (x e y) e o tamanho do
	# 		retângulo que está em volta do rosto (a e l).
	# Obs.: Essa detecção de faces não é muito perfeita, mas já é um bom começo.
	faces = cascade.detectMultiScale(gray_imagem)

	# Para cada x, y, a, l dentro de faces faça isso:
	# Obs.: Cada sessão do array faces contém as coordenadas do rosto identificado.
	# x -> coordenada inicial no eixo x.
	# y -> coordenada incial no eixo y.
	# a -> altura do retângulo que está em volta do rosto.
	# l -> largura do retângulo que está em volta do rosto.
	for x, y, a, l in faces:

		# Coordenadas iniciais do retângulo.
		inicioX = x
		inicioY = y

		# Coordenadas finais do retângulo.
		# Obs.: a e l não são coordenadas e sim a altura e largura do retângulo
		# 		que está em volta do rosto.
		fimX = x + a
		fimY = y + l

		# Aqui é onde ocorre o recorte da imagem onde está o rosto, a partir
		# das coordenadas dadas pela função detectMultiScale().
		corteRosto = imagem[inicioY : fimY, inicioX : fimX]

		# A função blur() faz exatamente o que o nome diz, ou seja, realiza um blur
		# na imagem que está recebendo, que nesse caso é a imagem de onde foi detectado
		# o rosto. O 2º parâmetro é a intensidade do blur na imagem.
		blur = cv2.blur(corteRosto, (25, 25))

		# Aqui é "colocado de volta" o que foi recortado da imagem inicial, mas
		# agora com o blur.
		imagem[inicioY : fimY, inicioX : fimX] = blur

	# Se quiser também pode salvar as imagens com o blur. Basta passar
	# o caminho onde quer salvar. :)
	# cv2.imwrite("imagens/obama-blur.png", imagem)

	# Mostra a imagem na tela do computador.
	cv2.imshow("Imagem", imagem)

	# Condição para terminar o programa. Se a letra "q" do teclado
	# for apertada, o programa será encerrado.
	cv2.waitKey(0) & 0xFF

	print("[INFO] Terminando o programa...")

	# Fechando todas as janelas abertas.
	cv2.destroyAllWindows()


# Função responsável por fazer o blur em vídeo, usando a webcam.
def blurRostoWebcam():

	print("[INFO] Iniciando o programa...")

	# Abre a webcam. Você pode configurar para o programa rodar em
	# um vídeo de sua escolha. Basta colocar o caminho do vídeo como
	# parâmetro da função VideoCapture().
	# Obs.: O 0 significa que é para ele abrir a webcam.
	captura = cv2.VideoCapture("imagens/video.mov")

	# Local onde o código irá se basear para detectar o que é um rosto.
	# Obs.: Cascade é um arquivo .xml que contém as características do
	# 		que é e não é um rosto humano.
	# Obs.: Tem alguns outros cascades na pasta que você pode testar e
	# 		ver qual melhor se encaixa no seu projeto.
	cascade = cv2.CascadeClassifier("cascades-rosto/haarcascade_frontalface_alt2.xml")

	print("[INFO] Programa iniciado!")

	print("[INFO] Aperte a tecla 'q' para fechar.")

	# Cada loop do while represta um frame do vídeo.
	while True:

		# Faz a leitura de cada frame do vídeo.
		ret, frame = captura.read()

		# Se não houver vídeo, interrompa.
		if not ret:

			print("Erro na apresentação do vídeo.")

			break

		# Redimensione a imagem.
		frame = imutils.resize(frame, width=600)

		# Converta a cor da imagem de BRG (padrão do OpenCV) para GRAY.
		gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Função responsável por detectar o que é um rosto e armazenar dentro
		# de um array (faces) as coordenadas de onde está esse possível rosto.
		# Obs.: Essa função faz a detecção do rosto dentro de um retângulo, 
		# 		logo, essas coordenadas são as de início (x e y) e o tamanho do
		# 		retângulo que está em volta do rosto (a e l).
		# Obs.: Essa detecção de faces não é muito perfeita, mas já é um bom começo.
		faces = cascade.detectMultiScale(gray_frame)

		# Para cada x, y, a, l dentro de faces faça isso:
		# Obs.: Cada sessão do array faces contém as coordenadas do rosto identificado.
		# x -> coordenada inicial no eixo x.
		# y -> coordenada incial no eixo y.
		# a -> altura do retângulo que está em volta do rosto.
		# l -> largura do retângulo que está em volta do rosto.
		for x, y, a, l in faces:

			# Coordenadas iniciais do retângulo.
			inicioX = x
			inicioY = y

			# Coordenadas finais do retângulo.
			# Obs.: a e l não são coordenadas e sim a altura e largura do retângulo
			# 		que está em volta do rosto.
			fimX = x + a
			fimY = y + l

			# Aqui é onde ocorre o recorte da imagem onde está o rosto, a partir
			# das coordenadas dadas pela função detectMultiScale().
			corteRosto = frame[inicioY : fimY, inicioX : fimX]

			# A função blur() faz exatamente o que o nome diz, ou seja, realiza um blur
			# na imagem que está recebendo, que nesse caso é a imagem de onde foi detectado
			# o rosto. O 2º parâmetro é a intensidade do blur na imagem.
			blur = cv2.blur(corteRosto, (25, 25))

			# Aqui é "colocado de volta" o que foi recortado da imagem inicial, mas
			# agora com o blur.
			frame[inicioY : fimY, inicioX : fimX] = blur

		# Mostra a imagem na tela do computador.
		cv2.imshow("Video", frame)

		# Condição para terminar o programa. Se a letra "q" do teclado
		# for apertada, o programa será encerrado.
		key = cv2.waitKey(1) & 0xFF
		if key == ord("q"):
			break

	print("[INFO] Terminando o programa...")

	# Liberando a captura da webcam e fechando todas as janelas abertas.
	captura.release()
	cv2.destroyAllWindows()


# Função principal, onde serão chamadas todas as outras funções.
def main():

	# Chamando a função para fazer o blur pela webcam.
	blurRostoWebcam()

	# Passando o lugar onde a imagem está armazenada. Tem alguns exemplos
	# dentro da pasta imagens. :)
	# caminhoImagem = "imagens/obama.jpg"

	# Chamando a função para fazer o blur em uma imagem.
	# blurRostoImagem(caminhoImagem)


if __name__ == "__main__":
	main()