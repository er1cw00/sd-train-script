
import os
import torch
from PIL import Image
from modules import devices
from modules.deepbooru import DeepDanbooru

path = "/Users/wadahana/Downloads/Pic/训练集/Loretta/"


devices.dtype = torch.float32

x = DeepDanbooru()
x.load()
x.start()

images_exts = ['.png', '.jpg', '.jpeg', '.bmp']
for filename in os.listdir(path):
    t = os.path.splitext(filename)
    if len(t) != 2 : 
        print(f'unknown file: {filename}')
        continue
    if not t[1] in images_exts:
        print(f'unknown file ext: {filename}')
        continue

    img_path = os.path.join(path, filename)
    tag_path = os.path.join(path, t[0] + '.txt')
    print(f'file: {img_path}, {tag_path}')
    img = Image.open(img_path)
    tag = x.tag(img)
    if len(tag) == 0:
        print('not tag for {filename} !');
        continue
    with open(tag_path, "w", errors='ignore') as f:
        f.writelines(tag)

x.stop()