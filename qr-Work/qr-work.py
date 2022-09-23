import qrcode

#data = "https://github.com/AshanManuka"
data = input("Enter some content which include in Your QR : ")
print(data)
img = qrcode.make(data)
img.save("qr-one.jpg")