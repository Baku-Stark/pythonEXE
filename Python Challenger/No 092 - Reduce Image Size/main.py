import cv2

img = cv2.imread('img\input.jpg')

# mostrar altura, largura e canais
print(img.shape)
k = 5
width = int((img.shape[1]/k))
height = int((img.shape[0]/k))

# reajustar dimensões da imagem
scaled = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
# novo tamanho da imagem
print(scaled.shape)

cv2.imshow("img\Output", scaled)
# valor vazio deixa a janela aberta infinitamente
# waitKey(valor em segundos) para deixar a janela aberta
cv2.waitKey(500)
cv2.destroyAllWindows()

cv2.imwrite('img\image_output.jpg', scaled)