user_benar = "ibnuracing"
pass_benar = "123"
percobaan = 0
while percobaan < 3:
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")
    if username == user_benar and password == pass_benar:
        print("Login berhasil, selamat datang", username + "!")
        break
    elif username != user_benar:
        print("Username salah!")
        percobaan += 1
    elif password != pass_benar:
        print("Password salah!")
        percobaan += 1
    if percobaan == 3:
        print("Anda sudah gagal login 3 kali, akun diblokir.")