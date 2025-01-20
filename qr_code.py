import qrcode

try:
    website_link = 'https://github.com/amanupa786'
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(website_link)
    qr.make()

    img = qr.make_image(fill_color='black', back_color='white')
    img.save('github_qr.png')
    print("QR code generated successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
