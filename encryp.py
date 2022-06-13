from cryptography.fernet import Fernet

import json

# some JSON:
amt = 1500
x = { 
    "name1":"John1", 
    "name2":"John2", 
    "T_id":"John2512ghoiugiuAsAS", 
    "acc":amt, 
    "amount":amt, 
    "to":"acc"
    }




# key = Fernet.generate_key()

# print(key)
# file = open('key.key', 'wb')  # Open the file as wb to write bytes
# file.write(key)  # The key is type bytes still
# file.close()


file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()
# print(key)


# ###########ENCRYPTION################
f = Fernet(key)
y = json.dumps(x)
# print(type(y))
mg = y.encode()
encry = f.encrypt(mg)

msg = str(encry)





import qrcode
from PIL import Image, ImageDraw, ImageFont

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


str_amt = str(amt)
if len(str_amt) <3:
        numWSize = 48
        numHSize = 48
        logo = Image.new('RGB', (numWSize, numHSize), color = (255, 255, 255,0))
        fnt = ImageFont.truetype('Bebas-Regular.ttf', 35)
else:
    numWSize = 44
    numHSize = 32
    logo = Image.new('RGB', (numWSize, numHSize), color = (255, 255, 255))
    fnt = ImageFont.truetype('Bebas-Regular.ttf', 25)

d = ImageDraw.Draw(logo)
w, h = fnt.getsize(str_amt)
d.text(((numWSize-w)/2,(numHSize-h-3)/2), str_amt,font = fnt, fill=(0, 0,0), stroke_fill='White', stroke_width=1)





basewidth = 80
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth,hsize), Image.ANTIALIAS)
qr_big = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)

qr_big.add_data(encry)
qr_big.make()
img_1 = qr_big.make_image(fill_color='Black', back_color="white").convert('RGB')
# img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
pos = ((img_1.size[0] - logo.size[0]) // 2, (img_1.size[1] - logo.size[1]) // 2)
img_1.paste(logo, pos)

img_1.save("1.png")



























###############Decrytion################
# decrypted = f.decrypt(encry)
# z = json.loads(decrypted)

# print(z["amount"])








