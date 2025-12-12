import qrcode

#url="https://www.tops-int.com/"
url="Hello Studnets!Good Monrning"

qr=qrcode.make(url)
qr.save("sec.png")