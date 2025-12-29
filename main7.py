import qrcode 
from PIL import Image

qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=40,border=4,)
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr.make(fit=True)
img = qr.make_image(fill_color="red",back_color="green")
img.save("y2.png")
print("QR code generated and saved as y2.png")
