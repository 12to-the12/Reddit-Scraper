
with open('D:\Projects\Computer Science\Scripts\last_uploaded.txt') as f:
    lines = f.readlines()
    last_uploaded = int(lines[0])
    print(f"{last_uploaded = }")
    current = last_uploaded + 1
    print(f"{current = }")
with open('D:\Projects\Computer Science\Scripts\last_uploaded.txt', 'w') as f:
    out = str(current)
    f.write('0')

import os
import re
final = 92

path =r'D:\Projects\Computer Science\Scripts\memes'


if current>final: quit()

current = 87# for testing
file_name = 'meme ('+str(current)+').jpg'

print(f"{file_name = }")




from PIL import Image

file = path + '\\' + file_name
img = Image.open(file)
print(type(img))

from instabot import Bot

