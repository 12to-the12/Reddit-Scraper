
with open('D:\Projects\Computer Science\Scripts\last_uploaded.txt') as f:
    lines = f.readlines()
    last_uploaded = int(lines[0])
    print(f"{last_uploaded = }")
    current = last_uploaded + 1
    print(f"{current = }")
with open('D:\Projects\Computer Science\Scripts\last_uploaded.txt', 'w') as f:
    out = str(current)
    f.write(out)

import os
import re
final = 92

path =r'D:\Projects\Computer Science\Scripts\memes'


if current>final: quit()

file_name = 'meme ('+str(current)+').jpg'

print(f"{file_name = }")



file_path = path + '\\' + file_name

from instabot import Bot

bot = Bot()
bot.login(username="spicy_meme_roundup", password="xfwSbP7PxxC9jZk", force=True)

hashtags = ' #meme #memes #memesdaily #funny #funnymemes #cringeymemes\
 #shitmemes #ifunny #dankmemes #shitpost #cursedmeme #cursedimage #cringe\
 #  #shitposts #foryoupage #fyp #cursedmemes #cursedimages #explore #explorepage #love'
captions = [
    'Fresh memes served daily',
    'Come getcha spicy memez',
    'For legal reasons this is a joke',
    'Help I\'m stuck in a caption!',
]

import random

caption = random.choice(captions) + hashtags

bot.upload_photo(file_path, caption=caption)

bot.logout()