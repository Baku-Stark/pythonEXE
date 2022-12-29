from PIL import Image

img = Image.open('img\input.png')
# criar um novo arquivo de imagem [cinversão]
img.save('img\output.ico')
print('FEITO!')