import qrcode

data = "https://github.com/AshanManuka"

img = qrcode.make(data)
img.save("qr-one.jpg")