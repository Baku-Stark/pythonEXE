import os
from PIL import Image

def watermark_photo(input_image_path, watermark_image_path, output_image_path):
    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path).convert('RGBA')
    # adicionando a marca d'água
    position = base_image.size
    newSize = (int(position[0]*8/100), int(position[0]*8/100))
    watermark = watermark.resize(newSize)

    new_pos = position[0]-newSize[0]-20, position[1]-newSize[1]-20
    transparent = Image.new(mode='RGBA', size=position, color=(0, 0, 0, 0))
    transparent.paste(base_image, (0, 0))
    transparent.paste(watermark, new_pos, watermark)
    image_mode = base_image.mode
    print(image_mode)

    if image_mode == 'RGB':
        transparent = transparent.convert(image_mode)

    else:
        transparent = transparent.convert('P')
    transparent.save(output_image_path, optimize=True, quality=100)
    print(f"Imagem salva em: {output_image_path} . . .")


# ---------
folder = input('Coloque a nome da pasta\nr: ')
watermark = r"..\img\water_mark.png"
os.chdir(folder)
files = os.listdir(os.getcwd())
print('')
print(f'Arquivos da pasta: {files}')

if not os.path.isdir("output"):
    os.mkdir("output")

c = 1
for i in files:
    if os.path.isfile(os.path.abspath(i)):
        if i.endswith(".png") or i.endswith(".jpg"):
            watermark_photo(i, watermark, "output/"+i)