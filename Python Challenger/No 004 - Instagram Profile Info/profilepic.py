import instaloader

# FUNÇAO PARA FAZER DOWNLOAD DO ICONE DE PERFIL DO INSTAGRAM
def pp_download(username):
    try:
        ig = instaloader.Instaloader()
        ig.download_profile(username, profile_pic_only=True)
        print("\033[32mDOWNLOAD DA FOTO DE PERFIL FEITO COM SUCESSO\033[m")

    except Exception as exp:
        print('ERROR: \033[31mNÃO FOI POSSÍVEL FAZER O DOWNLOAD DA FOTO DE PERFIL\033[m')
        print(exp)