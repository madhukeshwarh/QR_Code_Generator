import qrcode

# Function to generate QR code for a given URL
def generate_qr_code(url, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename)

    return filename

# URL to be encoded in the QR code
url =input('enter the url:')

# Generate the QR code and save it as a file
qr_code_filename = generate_qr_code(url)

# Print the filename of the generated QR code
print("Generated QR Code:", qr_code_filename)
