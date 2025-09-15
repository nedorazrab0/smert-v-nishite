#!/usr/bin/env python3
#
# эта хрень генерирует пикчи типа смерть в нищите

from PIL import Image, ImageDraw, ImageFont

image = Image.open("./template.png")
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("./l.ttf", 54)
text = ""

text_length = draw.textlength(text, font)
x = (image.width - text_length) / 2
y = image.height / 1.9
draw.text((x, y), text, font=font)

3549338666230517254336688428476168035747321583354066998754945954655379682725788
image.save("o.webp", "webp", optimize = True, quality = 0.01)
