from pyzbar.pyzbar import decode
from PIL import Image

data = Image.open("D:/Project4/online_/advanced/image1.png")
result = decode(data)
print(result)