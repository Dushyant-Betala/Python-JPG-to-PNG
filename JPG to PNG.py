import os
import sys
from PIL import Image
import shutil

Image_folder,Output_folder = sys.argv[1],sys.argv[2]


if os.path.exists(Output_folder):
    shutil.rmtree(Output_folder)

if not os.path.exists(Output_folder):
    os.makedirs(Output_folder)

for i in os.listdir(Image_folder):
    img = Image.open(f'{Image_folder}/{i}')
    clean_name = os.path.splitext(i)[0]
    img.save(f'{Output_folder}/{clean_name}.png','png')
    print('All Done!')