from PIL import Image, ImageDraw, ImageFont
import digitalio
import board
import adafruit_rgb_display.ili9341 as ili9341
import time
cs_pin = digitalio.DigitalInOut(board.D8)
dc_pin = digitalio.DigitalInOut(board.D24)
reset_pin = digitalio.DigitalInOut(board.D25)
BAUDRATE = 24000000
spi = board.SPI()
disp = ili9341.ILI9341(spi, rotation=90, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=BAUDRATE)
height = disp.width
width = disp.height
image = Image.new('RGB', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 255, 20))
disp.image(image)
print("Zelena")
time.sleep(2)
BORDER = 20
FONTSIZE = 24
draw.rectangle((BORDER, BORDER, width - BORDER - 1, height - BORDER - 1), fill=(170, 0, 136))
disp.image(image)
print("Ramecek")
time.sleep(2)
text = "Ahoj Vojto!"
font = ImageFont.truetype('/home/pi/fonts/OpenSans-Regular.ttf', FONTSIZE)
(font_width, font_height) = font.getsize(text)
draw.text((width//2 - font_width//2, height//2 - font_height//2), text, font=font, fill=(255, 255, 0))
disp.image(image)
print(text)
time.sleep(2)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 255))
disp.image(image)
print("Modra")
time.sleep(2)
