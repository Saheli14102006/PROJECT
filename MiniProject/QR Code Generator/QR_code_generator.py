import qrcode

website_link = 'https://github.com/Saheli14102006'

qr = qrcode.QRCode(version = 6, box_size = 10, border = 5)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color = 'blue', back_color = 'black')
img.save('github.png')