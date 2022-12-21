import qrcode

input_url = str(input('Insira o URL\nr: '))
print('')
try:
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=4
    )
    qr_code.add_data(input_url)
    qr_code.make(fit=True)

    img = qr_code.make_image(fill_color="#111111", back_color="white")
    img.save("url_qrcode.png")
    letSet = "\033[47m  \033[m"
    statusSucess = "\033[46m Sucesso!!! \033[m" #Cyan Background
    newSetSucess = f"\033[1m{statusSucess}\033[m"
    print(f"{letSet}{newSetSucess}")

except ModuleNotFoundError:
    letSet = "\033[47m  \033[m"
    statusError = "\033[41m Error!!! \033[m" #Red Background
    newSetError = f"\033[1m{statusError}\033[m"
    print(f"{letSet}{newSetError}")