import qrcode
portfolio_url = "https://samuel-abera-mekonn.netlify.app/"
qr = qrcode.make(portfolio_url)
qr.save("portfolio_qr.png")
print("hello qr code")