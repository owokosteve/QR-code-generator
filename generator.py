import qrcode
from PIL import Image
import qrcode.constants

data = f"MAXICA INVESTMENT LTD\nWater bottle 300ML. QUANTITY: 1\nEMAIL: maxicainvestments@gmail.com"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

# create image from the QR code
img = qr.make_image(fill_color="black", back_color="white")
img_path = "MyQRCode1.png"
img.save(img_path)
