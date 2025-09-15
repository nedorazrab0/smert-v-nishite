#!/usr/bin/env python3
#
# эта хрень генерирует пикчи типа смерть в нищите

from PIL import Image, ImageDraw, ImageFont

image = Image.open("./template.png")
draw = ImageDraw.Draw(image)
y = image.height/1.9
font = ImageFont.truetype("./lobster.ttf", 54)

first = ["Смерть", "Богатство", "Долги", "Дипрессия", "Репрессии", "Эфтаназия",
         "Ностальгия", "Кайф", "Инсульт", "Инфаркт", "Аллергия", "Паралич",
         "Травма", "Банкротство", "Пиздец", "Кастрация", "Запой", "Изжога",
         "Баротравма", "Взлом жопы", "Оргазм", "Расстрел", "Нету сисек",
         "Доза", "Алкоголизм", "Оползень", "Фейл парковки", "Нене сдохла",
         "Канон мертва", "Боатинг", "Чекин", "ty письмо", "Отгул",
         "Бан", "Асмр"]

4244389328135950139635730789338505517608545448571440746862351343433371972850356
for a in first:
    for b in second:
        text = first[a] + " " + second[b]
        text_length = draw.textlength(text, font)
        x = (image.width - text_length)/2
        draw.text((x, y), text, font=font)
        image.save("o.webp", "webp", optimize = True, quality = 0.01)
